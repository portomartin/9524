<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import {
  ShieldAlert,
  Flag,
  Users,
  BookOpen,
  CheckCircle2,
  AlertTriangle,
  EyeOff,
  UserX,
  UserCheck
} from 'lucide-vue-next'
import { usePlatformStore } from '../stores/platformStore'
import { useAuthStore } from '../stores/authStore'
import { mockStorage } from '../services/mockStorage'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'
import Card from '../components/ui/Card.vue'

const router = useRouter()
const platformStore = usePlatformStore()
const authStore = useAuthStore()

const activeTab = ref('reports') // 'reports' | 'users' | 'offers'

const reports = computed(() => platformStore.reports)
const users = computed(() => mockStorage.users)
const allOffers = computed(() => mockStorage.offers)

const pendingReports = computed(() => reports.value.filter(r => r.status === 'PENDIENTE'))

function handleResolveReport(reportId, action) {
  platformStore.resolveReport(reportId, action)
}

function handleToggleUserSuspension(userId) {
  if (confirm('¿Confirmas cambiar el estado de activación de este usuario?')) {
    platformStore.toggleUserSuspension(userId)
  }
}

function handleHideOffer(offerId) {
  platformStore.hideOffer(offerId)
}
</script>

<template>
  <div class="max-w-7xl mx-auto flex flex-col gap-8 pb-12">
    <!-- Header -->
    <div class="rounded-3xl border border-destructive/20 bg-card p-6 md:p-8 shadow-xs flex flex-wrap items-center justify-between gap-6">
      <div>
        <Badge variant="destructive" class="mb-2">
          <ShieldAlert class="h-3 w-3 mr-1" />
          Espacio Restringido · Rol ADMIN
        </Badge>
        <h1 class="text-2xl sm:text-3xl font-black tracking-tight text-foreground">Panel Administrativo de Moderación</h1>
        <p class="text-xs text-muted-foreground mt-0.5">
          Supervisa reportes comunitarios, modera contenidos publicados y gestiona el estado de las cuentas.
        </p>
      </div>

      <div class="flex items-center gap-3">
        <div class="rounded-2xl border border-destructive/20 bg-destructive/5 p-4 text-center min-w-[120px]">
          <span class="text-[10px] font-bold uppercase tracking-wider text-destructive block">Denuncias Pendientes</span>
          <span class="text-2xl font-black text-destructive block my-0.5">{{ pendingReports.length }}</span>
        </div>
        <div class="rounded-2xl border border-border bg-muted/40 p-4 text-center min-w-[120px]">
          <span class="text-[10px] font-bold uppercase tracking-wider text-muted-foreground block">Usuarios Totales</span>
          <span class="text-2xl font-black text-foreground block my-0.5">{{ users.length }}</span>
        </div>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="flex gap-2 border-b border-border pb-2">
      <button
        class="flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold transition-all cursor-pointer border border-transparent"
        :class="activeTab === 'reports' ? 'bg-destructive text-white font-bold' : 'bg-muted/60 text-muted-foreground hover:text-foreground'"
        @click="activeTab = 'reports'"
      >
        <Flag class="h-3.5 w-3.5" />
        <span>Denuncias y Reportes ({{ reports.length }})</span>
      </button>

      <button
        class="flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold transition-all cursor-pointer border border-transparent"
        :class="activeTab === 'users' ? 'bg-destructive text-white font-bold' : 'bg-muted/60 text-muted-foreground hover:text-foreground'"
        @click="activeTab = 'users'"
      >
        <Users class="h-3.5 w-3.5" />
        <span>Gestión de Cuentas ({{ users.length }})</span>
      </button>

      <button
        class="flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold transition-all cursor-pointer border border-transparent"
        :class="activeTab === 'offers' ? 'bg-destructive text-white font-bold' : 'bg-muted/60 text-muted-foreground hover:text-foreground'"
        @click="activeTab = 'offers'"
      >
        <BookOpen class="h-3.5 w-3.5" />
        <span>Moderación de Propuestas ({{ allOffers.length }})</span>
      </button>
    </div>

    <!-- TAB 1: DENUNCIAS (Subtarea 6.2.4) -->
    <Card v-if="activeTab === 'reports'" class="p-6">
      <h2 class="text-lg font-bold text-foreground mb-4">Revisión Humana de Denuncias</h2>

      <div v-if="reports.length > 0" class="flex flex-col gap-3">
        <div
          v-for="rep in reports"
          :key="rep.id"
          class="p-4 rounded-xl border flex flex-col md:flex-row items-start md:items-center justify-between gap-4 transition-all"
          :class="rep.status === 'PENDIENTE' ? 'border-destructive/30 bg-destructive/5' : 'border-border bg-card opacity-70'"
        >
          <div>
            <div class="flex items-center gap-2 mb-1">
              <Badge :variant="rep.status === 'PENDIENTE' ? 'destructive' : 'secondary'">{{ rep.status }}</Badge>
              <span class="text-xs font-bold text-foreground">Motivo: {{ rep.reason }}</span>
              <span class="text-xs text-muted-foreground">· Por {{ rep.reporterName }}</span>
            </div>
            <h3 class="text-sm font-bold text-foreground mb-1">
              {{ rep.targetType === 'OFFER' ? 'Propuesta:' : 'Usuario:' }} {{ rep.targetTitle }}
            </h3>
            <p class="text-xs text-muted-foreground">{{ rep.details || 'Sin detalles adicionales.' }}</p>
          </div>

          <div v-if="rep.status === 'PENDIENTE'" class="flex items-center gap-2 shrink-0">
            <Button
              v-if="rep.targetType === 'OFFER'"
              variant="destructive"
              size="sm"
              @click="handleResolveReport(rep.id, 'HIDE_OFFER')"
            >
              <EyeOff class="h-3.5 w-3.5 mr-1" />
              Ocultar Propuesta
            </Button>
            <Button
              v-if="rep.targetType === 'USER'"
              variant="destructive"
              size="sm"
              @click="handleResolveReport(rep.id, 'SUSPEND_USER')"
            >
              <UserX class="h-3.5 w-3.5 mr-1" />
              Suspender Usuario
            </Button>
            <Button
              variant="outline"
              size="sm"
              @click="handleResolveReport(rep.id, 'DISMISS')"
            >
              Desestimar
            </Button>
          </div>
          <div v-else class="text-xs font-semibold text-muted-foreground">
            Caso resuelto
          </div>
        </div>
      </div>
      <div v-else class="text-center p-8 text-xs text-muted-foreground">
        No hay denuncias registradas en el sistema.
      </div>
    </Card>

    <!-- TAB 2: USUARIOS (Subtarea 6.2.3) -->
    <Card v-if="activeTab === 'users'" class="p-6">
      <h2 class="text-lg font-bold text-foreground mb-4">Cuentas Registradas</h2>

      <div class="flex flex-col gap-2.5">
        <div
          v-for="u in users"
          :key="u.id"
          class="p-3.5 rounded-xl border border-border flex items-center justify-between flex-wrap gap-2 text-xs"
        >
          <div>
            <div class="flex items-center gap-2 mb-0.5">
              <span class="font-bold text-sm text-foreground">{{ u.name }}</span>
              <Badge variant="secondary">{{ u.role }}</Badge>
              <Badge :variant="u.status === 'ACTIVO' ? 'success' : 'destructive'">{{ u.status }}</Badge>
            </div>
            <span class="text-muted-foreground">{{ u.email }} · Reputación: {{ u.reputationScore }} ({{ u.reviewsCount }} calificaciones)</span>
          </div>

          <div v-if="u.role !== 'ADMIN'">
            <Button
              :variant="u.status === 'ACTIVO' ? 'destructive' : 'outline'"
              size="sm"
              @click="handleToggleUserSuspension(u.id)"
            >
              <component :is="u.status === 'ACTIVO' ? UserX : UserCheck" class="h-3.5 w-3.5 mr-1" />
              {{ u.status === 'ACTIVO' ? 'Suspender Cuenta' : 'Reactivar Cuenta' }}
            </Button>
          </div>
        </div>
      </div>
    </Card>

    <!-- TAB 3: PROPUESTAS (Subtarea 6.2.2) -->
    <Card v-if="activeTab === 'offers'" class="p-6">
      <h2 class="text-lg font-bold text-foreground mb-4">Moderación de Propuestas de Enseñanza</h2>

      <div class="flex flex-col gap-2.5">
        <div
          v-for="off in allOffers"
          :key="off.id"
          class="p-3.5 rounded-xl border border-border flex items-center justify-between flex-wrap gap-2 text-xs"
        >
          <div>
            <div class="flex items-center gap-2 mb-0.5">
              <span class="font-bold text-sm text-foreground">{{ off.title }}</span>
              <Badge :variant="off.status === 'PUBLICADA' ? 'success' : 'destructive'">{{ off.status }}</Badge>
            </div>
            <span class="text-muted-foreground">Por {{ off.userName }} · Categoría: {{ off.category }}</span>
          </div>

          <Button
            variant="outline"
            size="sm"
            :class="off.status === 'OCULTA' ? 'text-emerald-600' : 'text-destructive'"
            @click="handleHideOffer(off.id)"
          >
            {{ off.status === 'OCULTA' ? 'Restaurar Propuesta' : 'Ocultar Propuesta' }}
          </Button>
        </div>
      </div>
    </Card>
  </div>
</template>
