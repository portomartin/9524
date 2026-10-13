<script setup>
defineProps({
  /**
   * Variantes de íconos Hand-Drawn (trazo orgánico tipo boceto editorial en tinta):
   * - 'hero'      -> Bloque 1: Aprender enseñando (Libro abierto + bombilla/chispa bocetada)
   * - 'explore'   -> Bloque 2: Explorar, filtrar y reservar (Brújula / mapa trazado a mano)
   * - 'teach'     -> Tarjetas de Propuesta / Enseñar dentro de Explorar (Cuaderno + pluma/chispa)
   * - 'learn'     -> Tarjetas de Busca Aprender dentro de Explorar (Diana / telescopio bocetado)
   * - 'exchanges' -> Bloque 3: Intercambios en vivo (Lazo recíproco de trueque 1 a 1)
   * - 'simulator' -> Bloque 4: Simulador 1 a 1 (Imán / alquimia de afinidad trazada a mano)
   * - 'community' -> Bloque 5: Comunidad y confianza (Escudo orgánico con corazón / apretón)
   */
  name: {
    type: String,
    required: true
  },
  size: {
    type: String,
    default: 'md' // 'xs' | 'sm' | 'md' | 'lg' | 'xl'
  }
})

const sizeClasses = {
  xs: 'w-3.5 h-3.5',
  sm: 'w-4 h-4',
  md: 'w-5 h-5',
  lg: 'w-7 h-7',
  xl: 'w-9 h-9'
}
</script>

<template>
  <svg
    :class="['inline-block shrink-0 select-none', sizeClasses[size] || sizeClasses.md]"
    viewBox="0 0 36 36"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true"
  >
    <!-- 1. HERO: Aprender Enseñando (Libro abierto + chispa de luz trazada a mano) -->
    <g v-if="name === 'hero'" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <!-- Sombra de boceto desplazada -->
      <path
        d="M5.5 26.5C10 24.5 14.5 25.5 18 28C21.5 25.5 26 24.5 30.5 26.5"
        stroke-width="1.3"
        stroke-dasharray="2 2"
        opacity="0.45"
      />
      <!-- Libro abierto con trazo orgánico -->
      <path
        d="M18 13.5C14.8 11.2 9.5 10.8 5.2 12.4C4.8 16.8 4.9 21.2 5.3 25.2C9.8 23.6 14.6 24.2 18 26.8C21.4 24.2 26.2 23.6 30.7 25.2C31.1 21.2 31.2 16.8 30.8 12.4C26.5 10.8 21.2 11.2 18 13.5Z"
        stroke-width="2.1"
      />
      <path d="M18 13.8V26.5" stroke-width="1.8" />
      <!-- Líneas escritas a mano -->
      <path d="M8.5 16.2C11 15.8 13.2 16.1 14.8 16.9" stroke-width="1.5" opacity="0.75" />
      <path d="M8.5 19.8C10.8 19.4 12.8 19.7 14.5 20.4" stroke-width="1.5" opacity="0.75" />
      <path d="M21.2 16.9C22.8 16.1 25 15.8 27.5 16.2" stroke-width="1.5" opacity="0.75" />
      <path d="M21.5 20.4C23.2 19.7 25.2 19.4 27.5 19.8" stroke-width="1.5" opacity="0.75" />
      <!-- Chispa / Idea superior dibujada a mano -->
      <path d="M18 4.2V8.2" stroke-width="2" />
      <path d="M11.5 6.5L13.8 9.2" stroke-width="1.9" />
      <path d="M24.5 6.5L22.2 9.2" stroke-width="1.9" />
    </g>

    <!-- 2. EXPLORE: Explorar, Filtrar y Reservar (Brújula de exploración bocetada a mano) -->
    <g v-else-if="name === 'explore'" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <!-- Círculo exterior doble tipo boceto a mano alzada -->
      <path
        d="M18.2 4.3C26.1 4.1 31.9 10.2 31.7 18.1C31.5 25.9 25.3 31.8 17.6 31.7C9.8 31.6 4.1 25.4 4.3 17.5C4.5 9.9 10.5 4.5 18.2 4.3Z"
        stroke-width="2.1"
      />
      <path
        d="M6.8 13.2C8.9 8.1 14.2 5.8 19.8 6.4"
        stroke-width="1.2"
        stroke-dasharray="2 2.5"
        opacity="0.55"
      />
      <!-- Aguja de brújula dibujada a mano -->
      <path
        d="M23.8 12.2L20.2 20.2L12.2 23.8L15.8 15.8L23.8 12.2Z"
        stroke-width="2"
        fill="currentColor"
        fill-opacity="0.16"
      />
      <circle cx="18" cy="18" r="1.8" fill="currentColor" />
      <!-- Marcas cardinales tipo sketch -->
      <path d="M18 4.5V7.2" stroke-width="1.8" />
      <path d="M18 28.8V31.5" stroke-width="1.8" />
      <path d="M4.5 18H7.2" stroke-width="1.8" />
      <path d="M28.8 18H31.5" stroke-width="1.8" />
    </g>

    <!-- 2A. TEACH: Entidad Visual ENSEÑAR (Faro/Bombilla de Sabiduría + Libro Abierto con Rayos Fuertes) -->
    <g v-else-if="name === 'teach'" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <!-- Halo de fondo bocetado -->
      <circle cx="18" cy="14" r="9.5" fill="currentColor" fill-opacity="0.16" stroke="none" />
      <!-- Rayos potentes de enseñanza / transmisión de conocimiento -->
      <path d="M18 2.2V5.2" stroke-width="2.6" />
      <path d="M7.2 6.2L9.8 8.4" stroke-width="2.5" />
      <path d="M28.8 6.2L26.2 8.4" stroke-width="2.5" />
      <path d="M4.2 14.5H7.2" stroke-width="2.5" />
      <path d="M31.8 14.5H28.8" stroke-width="2.5" />
      <!-- Bombilla de mentoría trazada a mano con línea gruesa -->
      <path
        d="M12.2 14.2C12.2 10.6 14.8 8.2 18 8.2C21.2 8.2 23.8 10.6 23.8 14.2C23.8 16.6 22.1 18.3 21.1 19.8H14.9C13.9 18.3 12.2 16.6 12.2 14.2Z"
        stroke-width="2.5"
        fill="currentColor"
        fill-opacity="0.28"
      />
      <!-- Filamento interior en V (chispa activa) -->
      <path d="M16.2 15.2L18 12.6L19.8 15.2" stroke-width="2.1" />
      <!-- Libro abierto sólido en la base (símbolo de enseñar) -->
      <path
        d="M6.5 24.2C10.5 22.8 14.8 23.5 18 25.8C21.2 23.5 25.5 22.8 29.5 24.2V31.2C25.5 29.8 21.2 30.4 18 32.6C14.8 30.4 10.5 29.8 6.5 31.2V24.2Z"
        stroke-width="2.4"
        fill="currentColor"
        fill-opacity="0.22"
      />
      <path d="M18 25.8V32.4" stroke-width="2.2" />
    </g>

    <!-- 2B. LEARN: Entidad Visual APRENDER (Diana de Objetivo + Flecha Audaz + Destello de Descubrimiento) -->
    <g v-else-if="name === 'learn'" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <!-- Anillo exterior potente -->
      <path
        d="M16.8 5.2C23.9 5 29.5 10.7 29.2 17.9C28.9 25 23.2 30.5 16.1 30.2C9 29.9 3.8 24.1 4.2 17C4.5 10.2 10 5.4 16.8 5.2Z"
        stroke-width="2.5"
        fill="currentColor"
        fill-opacity="0.12"
      />
      <!-- Segundo anillo interior definido -->
      <circle
        cx="16.7"
        cy="17.7"
        r="7.2"
        stroke-width="2.2"
        fill="currentColor"
        fill-opacity="0.2"
      />
      <!-- Centro sólido (Blanco del objetivo) -->
      <circle cx="16.7" cy="17.7" r="3.1" fill="currentColor" />
      <!-- Flecha grande y potente clavada en el centro -->
      <path d="M32.5 3.5L17.5 17" stroke-width="2.8" />
      <!-- Punta de la flecha -->
      <path d="M17.2 11.8L16.9 17.5L22.6 17.2" stroke-width="2.5" />
      <!-- Plumas de la flecha arriba a la derecha -->
      <path d="M28.2 3.2L32.8 3.2L32.8 7.8" stroke-width="2.4" />
      <path d="M25.8 5.8L29.8 5.8V9.8" stroke-width="2" />
    </g>

    <!-- 3. EXCHANGES: Intercambios en Vivo (Dos flechas orgánicas en ciclo + chispa central) -->
    <g v-else-if="name === 'exchanges'" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <!-- Arco superior de dar -->
      <path
        d="M6.5 15.5C8.2 8.8 14.5 5.2 21.5 6.2C25.2 6.8 28.2 9.1 29.8 12.2"
        stroke-width="2.2"
      />
      <path d="M25.2 12.2H30.2V7.2" stroke-width="2.1" />
      <!-- Arco inferior de recibir -->
      <path
        d="M29.5 20.5C27.8 27.2 21.5 30.8 14.5 29.8C10.8 29.2 7.8 26.9 6.2 23.8"
        stroke-width="2.2"
      />
      <path d="M10.8 23.8H5.8V28.8" stroke-width="2.1" />
      <!-- Rombo/chispa de reciprocidad en el centro -->
      <path
        d="M18 12.8L20.2 16.2L23.5 18L20.2 19.8L18 23.2L15.8 19.8L12.5 18L15.8 16.2L18 12.8Z"
        stroke-width="1.8"
        fill="currentColor"
        fill-opacity="0.2"
      />
    </g>

    <!-- 4. SIMULATOR: Simulador 1 a 1 (Dos piezas/nodos conectando con rayo de afinidad) -->
    <g v-else-if="name === 'simulator'" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <!-- Nodo izquierdo (Lo que enseño) -->
      <circle cx="10.2" cy="18.5" r="5.2" stroke-width="2" fill="currentColor" fill-opacity="0.15" />
      <!-- Nodo derecho (Lo que aprendo) -->
      <circle cx="25.8" cy="18.5" r="5.2" stroke-width="2" fill="currentColor" fill-opacity="0.15" />
      <!-- Puente punteado dibujado a mano -->
      <path d="M15.2 16.2C17.2 14.2 18.8 14.2 20.8 16.2" stroke-width="1.8" />
      <path d="M20.8 20.8C18.8 22.8 17.2 22.8 15.2 20.8" stroke-width="1.8" />
      <!-- Chispa/Rayo de Match arriba -->
      <path
        d="M19.2 4.5L15.5 10.2H19.5L16.8 15.2"
        stroke-width="2.1"
      />
      <!-- Estrellas bocetadas a los lados -->
      <path d="M7.5 8.5L9.2 10.2M9.2 8.5L7.5 10.2" stroke-width="1.6" opacity="0.7" />
      <path d="M26.8 8.5L28.5 10.2M28.5 8.5L26.8 10.2" stroke-width="1.6" opacity="0.7" />
    </g>

    <!-- 5. COMMUNITY: Comunidad y Confianza (Escudo artesanal con corazón trazado a mano) -->
    <g v-else stroke="currentColor" stroke-linecap="round" stroke-linejoin="round">
      <!-- Escudo orgánico de trazo cálido -->
      <path
        d="M18 4.5C13.2 6.8 8.8 7.5 6.2 8.2C5.8 16.5 7.5 24.2 18 31.5C28.5 24.2 30.2 16.5 29.8 8.2C27.2 7.5 22.8 6.8 18 4.5Z"
        stroke-width="2.1"
        fill="currentColor"
        fill-opacity="0.12"
      />
      <!-- Borde interno punteado tipo costura / sello -->
      <path
        d="M18 7.8C14.4 9.3 11.2 9.9 9.2 10.4C9 16.5 10.4 22 18 27.6C25.6 22 27 16.5 26.8 10.4C24.8 9.9 21.6 9.3 18 7.8Z"
        stroke-width="1.2"
        stroke-dasharray="2.5 2.5"
        opacity="0.6"
      />
      <!-- Corazón / Confianza en el centro -->
      <path
        d="M18 22.5C18 22.5 12.8 18.9 12.8 15.6C12.8 13.9 14.1 12.8 15.6 12.8C16.7 12.8 17.5 13.4 18 14.3C18.5 13.4 19.3 12.8 20.4 12.8C21.9 12.8 23.2 13.9 23.2 15.6C23.2 18.9 18 22.5 18 22.5Z"
        stroke-width="1.9"
        fill="currentColor"
        fill-opacity="0.25"
      />
    </g>
  </svg>
</template>
