<script setup>
import { useRouter } from 'vue-router'
import {
  Sparkles,
  Compass,
  Search,
  UserPlus,
  ArrowRight,
  Coins,
  Calendar,
  Shield,
  Clock,
  CheckCircle2
} from '@lucide/vue'
import { usePlatformStore } from '../stores/platformStore'
import { useAuthStore } from '../stores/authStore'
import Button from '../components/ui/Button.vue'
import Badge from '../components/ui/Badge.vue'
import Card from '../components/ui/Card.vue'

const router = useRouter()
const platformStore = usePlatformStore()
const authStore = useAuthStore()
</script>

<template>
  <div class="max-w-7xl mx-auto flex flex-col gap-12">
    <!-- Hero Section (Minimalist Shadcn) -->
    <section class="relative overflow-hidden rounded-3xl border border-border bg-card p-8 md:p-14 text-center shadow-xs">
      <div class="inline-flex items-center gap-1.5 rounded-full border border-primary/20 bg-primary/5 px-3 py-1 text-xs font-semibold text-primary mb-4">
        <Sparkles class="h-3.5 w-3.5" />
        <span>Economía colaborativa sin dinero</span>
      </div>

      <h1 class="text-4xl md:text-6xl font-black tracking-tight text-foreground max-w-3xl mx-auto leading-tight mb-4">
        Aprende enseñando lo que sabes
      </h1>
      <p class="text-base md:text-lg text-muted-foreground max-w-2xl mx-auto leading-relaxed mb-8">
        Conectamos a personas que desean compartir sus conocimientos con quienes quieren aprender.
        Intercambia directamente o utiliza créditos internos cuando no exista reciprocidad directa.
      </p>

      <div class="flex flex-wrap items-center justify-center gap-3">
        <Button size="lg" @click="router.push({ name: 'explore' })">
          <Compass class="h-4 w-4 mr-1" />
          Explorar Propuestas
        </Button>
        <Button variant="outline" size="lg" @click="router.push({ name: 'search' })">
          <Search class="h-4 w-4 mr-1" />
          Buscador de Conocimientos
        </Button>
        <Button
          v-if="authStore.isGuest"
          variant="secondary"
          size="lg"
          @click="router.push({ name: 'auth' })"
        >
          <UserPlus class="h-4 w-4 mr-1" />
          Crear Cuenta Gratis
        </Button>
      </div>
    </section>

    <!-- The 6 Steps Core Cycle (MVP V3) -->
    <section class="rounded-2xl border border-border bg-card p-6 md:p-8 shadow-xs">
      <div class="text-center mb-8">
        <Badge variant="outline" class="mb-2">Recorrido Principal</Badge>
        <h2 class="text-2xl font-bold tracking-tight text-foreground">El Ciclo de Intercambio del MVP V3</h2>
        <p class="text-xs text-muted-foreground mt-1">Así funciona de principio a fin</p>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
        <div class="flex flex-col items-center text-center p-3 rounded-xl bg-muted/40 border border-border/50">
          <div class="h-8 w-8 rounded-full bg-primary/10 text-primary flex items-center justify-center text-sm font-bold mb-2">1</div>
          <h3 class="text-xs font-bold text-foreground">Descubrir</h3>
          <p class="text-[11px] text-muted-foreground mt-1">Explora propuestas y necesidades públicas sin registrarte.</p>
        </div>
        <div class="flex flex-col items-center text-center p-3 rounded-xl bg-muted/40 border border-border/50">
          <div class="h-8 w-8 rounded-full bg-primary/10 text-primary flex items-center justify-center text-sm font-bold mb-2">2</div>
          <h3 class="text-xs font-bold text-foreground">Interesarse</h3>
          <p class="text-[11px] text-muted-foreground mt-1">Consulta detalles, reputación del autor y agenda libre.</p>
        </div>
        <div class="flex flex-col items-center text-center p-3 rounded-xl bg-muted/40 border border-border/50">
          <div class="h-8 w-8 rounded-full bg-primary/10 text-primary flex items-center justify-center text-sm font-bold mb-2">3</div>
          <h3 class="text-xs font-bold text-foreground">Compatibilidad</h3>
          <p class="text-[11px] text-muted-foreground mt-1">El sistema calcula afinidad y detecta reciprocidad.</p>
        </div>
        <div class="flex flex-col items-center text-center p-3 rounded-xl bg-muted/40 border border-border/50">
          <div class="h-8 w-8 rounded-full bg-primary/10 text-primary flex items-center justify-center text-sm font-bold mb-2">4</div>
          <h3 class="text-xs font-bold text-foreground">Acordar</h3>
          <p class="text-[11px] text-muted-foreground mt-1">Solicita la sesión eligiendo fecha, franja y método.</p>
        </div>
        <div class="flex flex-col items-center text-center p-3 rounded-xl bg-muted/40 border border-border/50">
          <div class="h-8 w-8 rounded-full bg-primary/10 text-primary flex items-center justify-center text-sm font-bold mb-2">5</div>
          <h3 class="text-xs font-bold text-foreground">Realizar</h3>
          <p class="text-[11px] text-muted-foreground mt-1">Transición: Solicitada → Confirmada → En curso.</p>
        </div>
        <div class="flex flex-col items-center text-center p-3 rounded-xl bg-muted/40 border border-border/50">
          <div class="h-8 w-8 rounded-full bg-primary/10 text-primary flex items-center justify-center text-sm font-bold mb-2">6</div>
          <h3 class="text-xs font-bold text-foreground">Calificarse</h3>
          <p class="text-[11px] text-muted-foreground mt-1">Al finalizar se liquidan créditos y se califica.</p>
        </div>
      </div>
    </section>

    <!-- Key Principles Pillars -->
    <section class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <Card class="p-6">
        <div class="h-10 w-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center mb-4">
          <Coins class="h-5 w-5" />
        </div>
        <h3 class="text-base font-bold text-foreground mb-1">Créditos Internos</h3>
        <p class="text-xs text-muted-foreground leading-relaxed">
          Cada hora de enseñanza otorga 1 crédito, y cada hora de aprendizaje consume 1 crédito.
          <strong>No representan dinero</strong> ni pueden convertirse a dinero.
        </p>
      </Card>

      <Card class="p-6">
        <div class="h-10 w-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center mb-4">
          <Calendar class="h-5 w-5" />
        </div>
        <h3 class="text-base font-bold text-foreground mb-1">Agenda Clara por Horas</h3>
        <p class="text-xs text-muted-foreground leading-relaxed">
          Sin recurrencias complicadas: se cargan franjas horarias concretas de 1 hora.
          La agenda pública solo expone horarios libres, garantizando total privacidad.
        </p>
      </Card>

      <Card class="p-6">
        <div class="h-10 w-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center mb-4">
          <Shield class="h-5 w-5" />
        </div>
        <h3 class="text-base font-bold text-foreground mb-1">Confianza y Moderación</h3>
        <p class="text-xs text-muted-foreground leading-relaxed">
          Calificaciones únicas tras sesiones finalizadas, rankings comunitarios transparentes y
          panel de moderación para proteger la comunidad.
        </p>
      </Card>
    </section>

    <!-- Featured Offers -->
    <section class="rounded-2xl border border-border bg-card p-6 md:p-8 shadow-xs">
      <div class="flex items-center justify-between mb-6">
        <div>
          <h2 class="text-xl font-bold tracking-tight text-foreground">Propuestas Destacadas</h2>
          <p class="text-xs text-muted-foreground">Conocimientos disponibles para coordinar hoy</p>
        </div>
        <Button variant="ghost" size="sm" @click="router.push({ name: 'explore' })">
          Ver todas
          <ArrowRight class="h-3.5 w-3.5 ml-1" />
        </Button>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <Card
          v-for="offer in platformStore.offers.slice(0, 3)"
          :key="offer.id"
          class="p-5 flex flex-col justify-between hover:border-primary/40 hover:shadow-md transition-all"
        >
          <div>
            <div class="flex items-center justify-between mb-3">
              <Badge variant="secondary">{{ offer.category }}</Badge>
              <span class="text-xs text-muted-foreground flex items-center gap-1">
                <Clock class="h-3 w-3" />
                {{ offer.durationMinutes }} min
              </span>
            </div>
            <h3 class="text-base font-bold text-foreground mb-2 leading-snug">{{ offer.title }}</h3>
            <p class="text-xs text-muted-foreground line-clamp-3 mb-4 leading-relaxed">{{ offer.description }}</p>
          </div>

          <div class="pt-4 border-t border-border flex items-center justify-between">
            <span class="text-xs font-medium text-muted-foreground">Por {{ offer.userName }}</span>
            <Button
              variant="outline"
              size="sm"
              @click="router.push({ name: 'offer-detail', params: { id: offer.id } })"
            >
              Ver Detalle
            </Button>
          </div>
        </Card>
      </div>
    </section>
  </div>
</template>
