// Seed data inicial conforme a MVP V3 (proyecto-sdd/mvp-v3.md)
export const initialUsers = [
  {
    id: 'usr-1',
    name: 'Juan Carlos Pérez',
    email: 'juancarlos@example.com',
    password: 'password123',
    role: 'USER',
    bio: 'Desarrollador web frontend apasionado por Vue y la accesibilidad. Busco mejorar mi inglés técnico.',
    skillsToTeach: ['Vue 3', 'JavaScript Moderno', 'CSS / Tailwind', 'Diseño Accesible'],
    skillsToLearn: ['Inglés para IT', 'Docker Básico', 'Python'],
    level: 'AVANZADO',
    modality: 'VIRTUAL',
    reputationScore: 4.9,
    reviewsCount: 14,
    creditBalance: 4,
    agendaPublic: true,
    status: 'ACTIVO'
  },
  {
    id: 'usr-2',
    name: 'Elena Rostova',
    email: 'elena@example.com',
    password: 'password123',
    role: 'USER',
    bio: 'Traductora e instructora de inglés técnico para profesionales de software. Quiero aprender Vue.',
    skillsToTeach: ['Inglés para IT', 'Conversación fluida', 'Entrevistas en inglés'],
    skillsToLearn: ['Vue 3', 'Desarrollo Frontend'],
    level: 'AVANZADO',
    modality: 'VIRTUAL',
    reputationScore: 4.8,
    reviewsCount: 19,
    creditBalance: 6,
    agendaPublic: true,
    status: 'ACTIVO'
  },
  {
    id: 'usr-3',
    name: 'Carlos Mendoza',
    email: 'carlos@example.com',
    password: 'password123',
    role: 'USER',
    bio: 'Ingeniero de infraestructura y DevOps. Me encanta enseñar Linux y Docker.',
    skillsToTeach: ['Docker Básico', 'Linux Sysadmin', 'Git y GitHub'],
    skillsToLearn: ['Diseño Accesible', 'Figma'],
    level: 'INTERMEDIO',
    modality: 'VIRTUAL',
    reputationScore: 4.6,
    reviewsCount: 8,
    creditBalance: 2,
    agendaPublic: true,
    status: 'ACTIVO'
  },
  {
    id: 'usr-admin',
    name: 'Laura Moderadora',
    email: 'admin@example.com',
    password: 'adminpassword',
    role: 'ADMIN',
    bio: 'Administradora de la plataforma y defensora de la comunidad.',
    skillsToTeach: [],
    skillsToLearn: [],
    level: 'AVANZADO',
    modality: 'VIRTUAL',
    reputationScore: 5.0,
    reviewsCount: 0,
    creditBalance: 10,
    agendaPublic: false,
    status: 'ACTIVO'
  }
];

export const initialOffers = [
  {
    id: 'off-1',
    userId: 'usr-1',
    userName: 'Juan Carlos Pérez',
    title: 'Desarrollo de SPAs modernas con Vue 3 y Vite',
    description: 'Sesión práctica individual para dominar Composition API, reactividad profunda, Pinia y mejores prácticas de arquitectura frontend.',
    category: 'Programación',
    level: 'INTERMEDIO',
    modality: 'VIRTUAL',
    durationMinutes: 60,
    status: 'PUBLICADA',
    createdAt: '2026-10-01T10:00:00Z'
  },
  {
    id: 'off-2',
    userId: 'usr-2',
    userName: 'Elena Rostova',
    title: 'Inglés técnico para entrevistas de trabajo en IT',
    description: 'Simulación 1 a 1 de entrevistas técnicas en inglés, preparación de preguntas situacionales y vocabulario clave de la industria.',
    category: 'Idiomas',
    level: 'TODOS',
    modality: 'VIRTUAL',
    durationMinutes: 60,
    status: 'PUBLICADA',
    createdAt: '2026-10-02T14:30:00Z'
  },
  {
    id: 'off-3',
    userId: 'usr-3',
    userName: 'Carlos Mendoza',
    title: 'Fundamentos de Docker y Contenedores desde cero',
    description: 'Aprende a crear Dockerfiles optimizados, gestionar volúmenes, redes y levantar entornos con docker-compose paso a paso.',
    category: 'DevOps',
    level: 'PRINCIPIANTE',
    modality: 'VIRTUAL',
    durationMinutes: 60,
    status: 'PUBLICADA',
    createdAt: '2026-10-03T11:15:00Z'
  },
  {
    id: 'off-4',
    userId: 'usr-1',
    userName: 'Juan Carlos Pérez',
    title: 'Fundamentos de Accesibilidad Web (WCAG 2.1)',
    description: 'Cómo diseñar interfaces usables para todos: contraste de colores, navegación por teclado y semántica HTML accesible.',
    category: 'Diseño',
    level: 'PRINCIPIANTE',
    modality: 'VIRTUAL',
    durationMinutes: 60,
    status: 'PUBLICADA',
    createdAt: '2026-10-04T09:00:00Z'
  }
];

export const initialNeeds = [
  {
    id: 'nd-1',
    userId: 'usr-1',
    userName: 'Juan Carlos Pérez',
    title: 'Inglés conversacional fluido para reuniones de equipo',
    goal: 'Mejorar pronunciación y vocabulario para participar activamente en dailies y demos en inglés.',
    category: 'Idiomas',
    level: 'INTERMEDIO',
    modality: 'VIRTUAL',
    status: 'ACTIVA',
    createdAt: '2026-10-01T12:00:00Z'
  },
  {
    id: 'nd-2',
    userId: 'usr-2',
    userName: 'Elena Rostova',
    title: 'Aprender Vue 3 y Composition API',
    goal: 'Poder construir un portfolio interactivo propio sin depender de plantillas prediseñadas.',
    category: 'Programación',
    level: 'PRINCIPIANTE',
    modality: 'VIRTUAL',
    status: 'ACTIVA',
    createdAt: '2026-10-02T16:00:00Z'
  },
  {
    id: 'nd-3',
    userId: 'usr-3',
    userName: 'Carlos Mendoza',
    title: 'Principios de Diseño y Accesibilidad UI',
    goal: 'Entender qué hace que un panel web se vea intuitivo y cómo validar accesibilidad básica.',
    category: 'Diseño',
    level: 'PRINCIPIANTE',
    modality: 'VIRTUAL',
    status: 'ACTIVA',
    createdAt: '2026-10-03T18:00:00Z'
  }
];

export const initialAvailabilitySlots = [
  // Franjas de Juan Carlos (usr-1)
  { id: 'slot-1', userId: 'usr-1', date: '2026-10-15', startTime: '10:00', durationHours: 1, isCommitted: false, sessionId: null },
  { id: 'slot-2', userId: 'usr-1', date: '2026-10-15', startTime: '11:00', durationHours: 1, isCommitted: false, sessionId: null },
  { id: 'slot-3', userId: 'usr-1', date: '2026-10-16', startTime: '15:00', durationHours: 1, isCommitted: false, sessionId: null },
  { id: 'slot-4', userId: 'usr-1', date: '2026-10-17', startTime: '09:00', durationHours: 1, isCommitted: true, sessionId: 'ses-1' },
  // Franjas de Elena (usr-2)
  { id: 'slot-5', userId: 'usr-2', date: '2026-10-15', startTime: '14:00', durationHours: 1, isCommitted: false, sessionId: null },
  { id: 'slot-6', userId: 'usr-2', date: '2026-10-15', startTime: '15:00', durationHours: 1, isCommitted: false, sessionId: null },
  { id: 'slot-7', userId: 'usr-2', date: '2026-10-16', startTime: '10:00', durationHours: 1, isCommitted: false, sessionId: null },
  { id: 'slot-8', userId: 'usr-2', date: '2026-10-17', startTime: '11:00', durationHours: 1, isCommitted: true, sessionId: 'ses-2' },
  // Franjas de Carlos (usr-3)
  { id: 'slot-9', userId: 'usr-3', date: '2026-10-18', startTime: '16:00', durationHours: 1, isCommitted: false, sessionId: null },
  { id: 'slot-10', userId: 'usr-3', date: '2026-10-18', startTime: '17:00', durationHours: 1, isCommitted: false, sessionId: null }
];

export const initialSessions = [
  {
    id: 'ses-1',
    teacherId: 'usr-1',
    teacherName: 'Juan Carlos Pérez',
    studentId: 'usr-2',
    studentName: 'Elena Rostova',
    offerId: 'off-1',
    topic: 'Desarrollo de SPAs modernas con Vue 3 y Vite',
    date: '2026-10-17',
    time: '09:00',
    durationMinutes: 60,
    modality: 'VIRTUAL',
    exchangeType: 'RECIPROCAL',
    status: 'CONFIRMADA',
    cancellationReason: null,
    createdAt: '2026-10-06T11:00:00Z',
    creditsTransferred: false,
    isRated: false
  },
  {
    id: 'ses-2',
    teacherId: 'usr-2',
    teacherName: 'Elena Rostova',
    studentId: 'usr-3',
    studentName: 'Carlos Mendoza',
    offerId: 'off-2',
    topic: 'Inglés técnico para entrevistas de trabajo en IT',
    date: '2026-10-17',
    time: '11:00',
    durationMinutes: 60,
    modality: 'VIRTUAL',
    exchangeType: 'CREDITS',
    status: 'SOLICITADA',
    cancellationReason: null,
    createdAt: '2026-10-07T09:30:00Z',
    creditsTransferred: false,
    isRated: false
  },
  {
    id: 'ses-3',
    teacherId: 'usr-2',
    teacherName: 'Elena Rostova',
    studentId: 'usr-1',
    studentName: 'Juan Carlos Pérez',
    offerId: 'off-2',
    topic: 'Práctica de conversación técnica en inglés',
    date: '2026-10-05',
    time: '10:00',
    durationMinutes: 60,
    modality: 'VIRTUAL',
    exchangeType: 'RECIPROCAL',
    status: 'FINALIZADA',
    cancellationReason: null,
    createdAt: '2026-10-04T12:00:00Z',
    creditsTransferred: true,
    isRated: true
  }
];

export const initialCreditMovements = [
  {
    id: 'cm-1',
    userId: 'usr-1',
    amount: 3,
    type: 'INICIAL',
    description: 'Créditos iniciales de bienvenida a la plataforma',
    date: '2026-10-01T08:00:00Z'
  },
  {
    id: 'cm-2',
    userId: 'usr-1',
    amount: 1,
    type: 'SESION_DICTADA',
    description: 'Crédito recibido por dictar sesión "Vue 3 Básico"',
    date: '2026-10-04T15:00:00Z'
  },
  {
    id: 'cm-3',
    userId: 'usr-2',
    amount: 3,
    type: 'INICIAL',
    description: 'Créditos iniciales de bienvenida a la plataforma',
    date: '2026-10-01T08:00:00Z'
  },
  {
    id: 'cm-4',
    userId: 'usr-2',
    amount: 3,
    type: 'SESION_DICTADA',
    description: 'Sesiones de inglés dictadas con éxito',
    date: '2026-10-05T12:00:00Z'
  }
];

export const initialReviews = [
  {
    id: 'rev-1',
    sessionId: 'ses-3',
    fromUserId: 'usr-1',
    fromUserName: 'Juan Carlos Pérez',
    toUserId: 'usr-2',
    rating: 5,
    comment: '¡Excelente sesión! Elena explicó modismos técnicos de forma muy clara y dinámica.',
    createdAt: '2026-10-05T11:15:00Z'
  },
  {
    id: 'rev-2',
    sessionId: 'ses-old-1',
    fromUserId: 'usr-3',
    fromUserName: 'Carlos Mendoza',
    toUserId: 'usr-1',
    rating: 5,
    comment: 'Juan Carlos es un gran pedagogo, resolvió todas mis dudas de maquetación.',
    createdAt: '2026-10-04T16:00:00Z'
  }
];

export const initialReports = [
  {
    id: 'rep-1',
    reporterId: 'usr-1',
    reporterName: 'Juan Carlos Pérez',
    targetType: 'OFFER',
    targetId: 'off-3',
    targetTitle: 'Fundamentos de Docker y Contenedores desde cero',
    reason: 'Spam o Publicidad indebida',
    details: 'Contiene enlaces externos hacia cursos pagos comerciales ajenos a la comunidad.',
    status: 'PENDIENTE',
    createdAt: '2026-10-07T14:00:00Z'
  }
];
