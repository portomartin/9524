import {
  initialUsers,
  initialOffers,
  initialNeeds,
  initialAvailabilitySlots,
  initialSessions,
  initialCreditMovements,
  initialReviews,
  initialReports
} from './mockData'

const STORAGE_KEY = 'intercambia_mvp_v3_state'

class MockStorageService {
  constructor() {
    this.loadState()
  }

  loadState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY)
      if (raw) {
        const parsed = JSON.parse(raw)
        this.users = parsed.users || [...initialUsers]
        this.offers = parsed.offers || [...initialOffers]
        this.needs = parsed.needs || [...initialNeeds]
        this.slots = parsed.slots || [...initialAvailabilitySlots]
        this.sessions = parsed.sessions || [...initialSessions]
        this.credits = parsed.credits || [...initialCreditMovements]
        this.reviews = parsed.reviews || [...initialReviews]
        this.reports = parsed.reports || [...initialReports]
        return
      }
    } catch {
      // LocalStorage no disponible o corrupto, cargar datos base
    }

    this.users = JSON.parse(JSON.stringify(initialUsers))
    this.offers = JSON.parse(JSON.stringify(initialOffers))
    this.needs = JSON.parse(JSON.stringify(initialNeeds))
    this.slots = JSON.parse(JSON.stringify(initialAvailabilitySlots))
    this.sessions = JSON.parse(JSON.stringify(initialSessions))
    this.credits = JSON.parse(JSON.stringify(initialCreditMovements))
    this.reviews = JSON.parse(JSON.stringify(initialReviews))
    this.reports = JSON.parse(JSON.stringify(initialReports))
    this.saveState()
  }

  saveState() {
    try {
      const state = {
        users: this.users,
        offers: this.offers,
        needs: this.needs,
        slots: this.slots,
        sessions: this.sessions,
        credits: this.credits,
        reviews: this.reviews,
        reports: this.reports
      }
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state))
    } catch {
      // Ignore
    }
  }

  resetToDefaults() {
    localStorage.removeItem(STORAGE_KEY)
    this.loadState()
  }

  // --- Auth & Users ---
  findUserByEmail(email) {
    return this.users.find(u => u.email.toLowerCase() === email.toLowerCase())
  }

  findUserById(id) {
    return this.users.find(u => u.id === id)
  }

  registerUser({ name, email, password }) {
    if (this.findUserByEmail(email)) {
      throw new Error('Ya existe una cuenta registrada con este correo electrónico.')
    }
    const newUser = {
      id: `usr-${Date.now()}`,
      name,
      email,
      password,
      role: 'USER',
      bio: '',
      skillsToTeach: [],
      skillsToLearn: [],
      level: 'PRINCIPIANTE',
      modality: 'VIRTUAL',
      reputationScore: 5.0,
      reviewsCount: 0,
      creditBalance: 3, // Saldo inicial de bienvenida
      agendaPublic: true,
      status: 'ACTIVO'
    }
    this.users.push(newUser)

    // Movimiento inicial de créditos
    this.credits.push({
      id: `cm-${Date.now()}`,
      userId: newUser.id,
      amount: 3,
      type: 'INICIAL',
      description: 'Créditos iniciales de bienvenida a la plataforma',
      date: new Date().toISOString()
    })

    this.saveState()
    return newUser
  }

  updateProfile(userId, patch) {
    const user = this.findUserById(userId)
    if (!user) throw new Error('Usuario no encontrado')
    Object.assign(user, patch)
    this.saveState()
    return { ...user }
  }

  // --- Public Offers & Needs ---
  getPublicOffers() {
    return this.offers.filter(o => o.status === 'PUBLICADA')
  }

  getPublicOfferById(id) {
    return this.offers.find(o => o.id === id && o.status === 'PUBLICADA')
  }

  getUserOffers(userId) {
    return this.offers.filter(o => o.userId === userId)
  }

  createOffer(userId, offerData) {
    const user = this.findUserById(userId)
    const newOffer = {
      id: `off-${Date.now()}`,
      userId,
      userName: user ? user.name : 'Usuario',
      title: offerData.title,
      description: offerData.description,
      category: offerData.category || 'General',
      level: offerData.level || 'TODOS',
      modality: offerData.modality || 'VIRTUAL',
      durationMinutes: 60,
      status: offerData.status || 'PUBLICADA',
      createdAt: new Date().toISOString()
    }
    this.offers.unshift(newOffer)
    this.saveState()
    return newOffer
  }

  updateOffer(offerId, patch) {
    const offer = this.offers.find(o => o.id === offerId)
    if (!offer) throw new Error('Propuesta no encontrada')
    Object.assign(offer, patch)
    this.saveState()
    return { ...offer }
  }

  deleteOffer(offerId) {
    this.offers = this.offers.filter(o => o.id !== offerId)
    this.saveState()
  }

  // Needs
  getPublicNeeds() {
    return this.needs.filter(n => n.status === 'ACTIVA')
  }

  getUserNeeds(userId) {
    return this.needs.filter(n => n.userId === userId && n.status !== 'ELIMINADA')
  }

  createNeed(userId, needData) {
    const user = this.findUserById(userId)
    const newNeed = {
      id: `nd-${Date.now()}`,
      userId,
      userName: user ? user.name : 'Usuario',
      title: needData.title,
      goal: needData.goal,
      category: needData.category || 'General',
      level: needData.level || 'PRINCIPIANTE',
      modality: needData.modality || 'VIRTUAL',
      status: 'ACTIVA',
      createdAt: new Date().toISOString()
    }
    this.needs.unshift(newNeed)
    this.saveState()
    return newNeed
  }

  updateNeed(needId, patch) {
    const need = this.needs.find(n => n.id === needId)
    if (!need) throw new Error('Aprendizaje buscado no encontrado')
    Object.assign(need, patch)
    this.saveState()
    return { ...need }
  }

  deleteNeed(needId) {
    const need = this.needs.find(n => n.id === needId)
    if (need) {
      need.status = 'ELIMINADA'
      this.saveState()
    }
  }

  // --- Availability Slots ---
  getUserSlots(userId) {
    return this.slots.filter(s => s.userId === userId)
  }

  getPublicUserSlots(userId) {
    const user = this.findUserById(userId)
    if (!user || !user.agendaPublic) return []
    // Solo franjas libres, sin datos de acuerdos privados
    return this.slots
      .filter(s => s.userId === userId && !s.isCommitted)
      .map(s => ({
        id: s.id,
        date: s.date,
        startTime: s.startTime,
        durationHours: s.durationHours
      }))
  }

  addSlot(userId, { date, startTime }) {
    // Verificar si ya existe franja en esa fecha/hora
    const exists = this.slots.some(s => s.userId === userId && s.date === date && s.startTime === startTime)
    if (exists) {
      throw new Error('Ya tienes una franja horaria cargada para esa misma fecha y hora.')
    }
    const newSlot = {
      id: `slot-${Date.now()}-${Math.random().toString(36).substring(2, 6)}`,
      userId,
      date,
      startTime,
      durationHours: 1,
      isCommitted: false,
      sessionId: null
    }
    this.slots.push(newSlot)
    this.saveState()
    return newSlot
  }

  batchAddSlots(userId, { dates, hours }) {
    let added = 0
    dates.forEach(date => {
      hours.forEach(startTime => {
        const exists = this.slots.some(s => s.userId === userId && s.date === date && s.startTime === startTime)
        if (!exists) {
          this.slots.push({
            id: `slot-${Date.now()}-${Math.random().toString(36).substring(2, 6)}`,
            userId,
            date,
            startTime,
            durationHours: 1,
            isCommitted: false,
            sessionId: null
          })
          added++
        }
      })
    })
    this.saveState()
    return added
  }

  deleteSlot(slotId) {
    const slot = this.slots.find(s => s.id === slotId)
    if (slot && slot.isCommitted) {
      throw new Error('No se puede eliminar una franja comprometida con una sesión activa.')
    }
    this.slots = this.slots.filter(s => s.id !== slotId)
    this.saveState()
  }

  toggleAgendaVisibility(userId, isPublic) {
    const user = this.findUserById(userId)
    if (user) {
      user.agendaPublic = isPublic
      this.saveState()
    }
  }

  // --- Sessions & Workflow ---
  getUserSessions(userId) {
    return this.sessions.filter(s => s.teacherId === userId || s.studentId === userId)
  }

  createSessionRequest({ teacherId, studentId, offerId, topic, date, time, modality, exchangeType }) {
    const teacher = this.findUserById(teacherId)
    const student = this.findUserById(studentId)

    if (exchangeType === 'CREDITS' && student.creditBalance < 1) {
      throw new Error('No posees suficientes créditos internos para solicitar esta sesión (requiere 1 crédito).')
    }

    const newSession = {
      id: `ses-${Date.now()}`,
      teacherId,
      teacherName: teacher.name,
      studentId,
      studentName: student.name,
      offerId: offerId || null,
      topic,
      date,
      time,
      durationMinutes: 60,
      modality: modality || 'VIRTUAL',
      exchangeType: exchangeType || 'CREDITS',
      status: 'SOLICITADA',
      cancellationReason: null,
      createdAt: new Date().toISOString(),
      creditsTransferred: false,
      isRated: false
    }

    this.sessions.unshift(newSession)
    this.saveState()
    return newSession
  }

  confirmSession(sessionId) {
    const session = this.sessions.find(s => s.id === sessionId)
    if (!session) throw new Error('Sesión no encontrada')
    session.status = 'CONFIRMADA'

    // Comprometer la franja del profesor si coincide
    const slot = this.slots.find(s => s.userId === session.teacherId && s.date === session.date && s.startTime === session.time)
    if (slot) {
      slot.isCommitted = true
      slot.sessionId = session.id
    }

    this.saveState()
    return session
  }

  startSession(sessionId) {
    const session = this.sessions.find(s => s.id === sessionId)
    if (!session) throw new Error('Sesión no encontrada')
    if (session.status !== 'CONFIRMADA') throw new Error('Solo una sesión confirmada puede pasar a en curso.')
    session.status = 'EN_CURSO'
    this.saveState()
    return session
  }

  completeSession(sessionId) {
    const session = this.sessions.find(s => s.id === sessionId)
    if (!session) throw new Error('Sesión no encontrada')
    if (session.status !== 'EN_CURSO') throw new Error('Solo una sesión en curso puede ser completada.')

    session.status = 'FINALIZADA'

    // Ejecutar transferencia de créditos si fue acordada por créditos
    if (session.exchangeType === 'CREDITS' && !session.creditsTransferred) {
      const student = this.findUserById(session.studentId)
      const teacher = this.findUserById(session.teacherId)

      if (student && teacher) {
        student.creditBalance = Math.max(0, student.creditBalance - 1)
        teacher.creditBalance = teacher.creditBalance + 1

        this.credits.unshift({
          id: `cm-${Date.now()}-1`,
          userId: student.id,
          amount: -1,
          type: 'SESION_RECIBIDA',
          description: `Participación en sesión de aprendizaje: "${session.topic}"`,
          date: new Date().toISOString()
        })

        this.credits.unshift({
          id: `cm-${Date.now()}-2`,
          userId: teacher.id,
          amount: 1,
          type: 'SESION_DICTADA',
          description: `Enseñanza brindada en sesión: "${session.topic}"`,
          date: new Date().toISOString()
        })

        session.creditsTransferred = true
      }
    }

    // Liberar la franja
    const slot = this.slots.find(s => s.sessionId === session.id)
    if (slot) {
      slot.isCommitted = false
      slot.sessionId = null
    }

    this.saveState()
    return session
  }

  cancelSession(sessionId, reason) {
    const session = this.sessions.find(s => s.id === sessionId)
    if (!session) throw new Error('Sesión no encontrada')
    session.status = 'CANCELADA'
    session.cancellationReason = reason || 'Cancelada por el participante'

    // Liberar la franja de disponibilidad si estaba comprometida
    const slot = this.slots.find(s => s.sessionId === session.id)
    if (slot) {
      slot.isCommitted = false
      slot.sessionId = null
    }

    this.saveState()
    return session
  }

  // --- Ratings & Reputation ---
  submitRating({ sessionId, fromUserId, toUserId, rating, comment }) {
    const session = this.sessions.find(s => s.id === sessionId)
    if (!session) throw new Error('Sesión no encontrada')
    if (session.isRated) throw new Error('Esta sesión ya fue calificada previamente.')

    const fromUser = this.findUserById(fromUserId)
    const review = {
      id: `rev-${Date.now()}`,
      sessionId,
      fromUserId,
      fromUserName: fromUser ? fromUser.name : 'Usuario',
      toUserId,
      rating: Number(rating),
      comment: comment || '',
      createdAt: new Date().toISOString()
    }
    this.reviews.unshift(review)
    session.isRated = true

    // Recalcular reputación del usuario evaluado
    const targetUser = this.findUserById(toUserId)
    if (targetUser) {
      const userReviews = this.reviews.filter(r => r.toUserId === toUserId)
      const sum = userReviews.reduce((acc, curr) => acc + curr.rating, 0)
      targetUser.reviewsCount = userReviews.length
      targetUser.reputationScore = Number((sum / userReviews.length).toFixed(1))
    }

    this.saveState()
    return review
  }

  getUserReviews(userId) {
    return this.reviews.filter(r => r.toUserId === userId)
  }

  // --- Reports & Moderation (Admin) ---
  submitReport({ reporterId, targetType, targetId, targetTitle, reason, details }) {
    const reporter = this.findUserById(reporterId)
    const report = {
      id: `rep-${Date.now()}`,
      reporterId,
      reporterName: reporter ? reporter.name : 'Usuario anónimo',
      targetType, // 'OFFER' | 'USER'
      targetId,
      targetTitle,
      reason,
      details,
      status: 'PENDIENTE',
      createdAt: new Date().toISOString()
    }
    this.reports.unshift(report)
    this.saveState()
    return report
  }

  getAllReports() {
    return [...this.reports]
  }

  resolveReport(reportId, action) {
    const report = this.reports.find(r => r.id === reportId)
    if (!report) throw new Error('Denuncia no encontrada')

    if (action === 'HIDE_OFFER' && report.targetType === 'OFFER') {
      const offer = this.offers.find(o => o.id === report.targetId)
      if (offer) offer.status = 'OCULTA'
      report.status = 'RESUELTA'
    } else if (action === 'SUSPEND_USER' && report.targetType === 'USER') {
      const user = this.findUserById(report.targetId)
      if (user) user.status = 'SUSPENDIDO'
      report.status = 'RESUELTA'
    } else if (action === 'DISMISS') {
      report.status = 'DESESTIMADA'
    }

    this.saveState()
    return report
  }

  toggleUserSuspension(userId) {
    const user = this.findUserById(userId)
    if (!user) throw new Error('Usuario no encontrado')
    user.status = user.status === 'ACTIVO' ? 'SUSPENDIDO' : 'ACTIVO'
    this.saveState()
    return user
  }

  hideOffer(offerId) {
    const offer = this.offers.find(o => o.id === offerId)
    if (!offer) throw new Error('Propuesta no encontrada')
    offer.status = offer.status === 'OCULTA' ? 'PUBLICADA' : 'OCULTA'
    this.saveState()
    return offer
  }

  // --- Compatibilities Engine ---
  calculateCompatibilities(currentUserId) {
    const currentUser = this.findUserById(currentUserId)
    if (!currentUser) return []

    const userCanTeach = (currentUser.skillsToTeach || []).map(s => s.toLowerCase())
    const userWantsToLearn = (currentUser.skillsToLearn || []).map(s => s.toLowerCase())

    const otherOffers = this.getPublicOffers().filter(o => o.userId !== currentUserId)

    return otherOffers.map(offer => {
      const author = this.findUserById(offer.userId) || {}
      const authorCanTeach = (author.skillsToTeach || []).map(s => s.toLowerCase())
      const authorWantsToLearn = (author.skillsToLearn || []).map(s => s.toLowerCase())

      // 1. Coincidencia directa de interés
      const offerTitleLower = offer.title.toLowerCase()
      const offerCategoryLower = (offer.category || '').toLowerCase()

      const topicMatch = userWantsToLearn.some(topic =>
        offerTitleLower.includes(topic) || offerCategoryLower.includes(topic) || topic.includes(offerCategoryLower)
      )

      // 2. Reciprocidad: ¿El usuario puede enseñar algo que el autor busca aprender?
      const reciprocalMatch = authorWantsToLearn.some(wants =>
        userCanTeach.some(teaches => teaches.includes(wants) || wants.includes(teaches))
      )

      // 3. Nivel y modalidad
      const modalityMatch = !currentUser.modality || currentUser.modality === offer.modality || offer.modality === 'TODOS'

      let score = 50
      const reasons = []

      if (topicMatch) {
        score += 30
        reasons.push('Coincide con tus temas de aprendizaje buscados')
      }
      if (reciprocalMatch) {
        score += 20
        reasons.push('¡Posible intercambio recíproco directo! Puedes enseñarle lo que busca')
      }
      if (modalityMatch) {
        score += 10
        reasons.push(`Modalidad compatible (${offer.modality})`)
      }

      return {
        offer,
        author,
        score: Math.min(score, 98),
        isReciprocal: reciprocalMatch,
        reasons
      }
    }).sort((a, b) => b.score - a.score)
  }

  // --- Trust & Community Rankings ---
  getCommunityRankings() {
    return [...this.users]
      .filter(u => u.role === 'USER' && u.status === 'ACTIVO')
      .sort((a, b) => b.reputationScore - a.reputationScore || b.reviewsCount - a.reviewsCount)
  }

  getTrendingTopics() {
    const counts = {}
    this.offers.forEach(o => {
      counts[o.category] = (counts[o.category] || 0) + 1
    })
    return Object.entries(counts)
      .map(([category, count]) => ({ category, count }))
      .sort((a, b) => b.count - a.count)
  }

  getRecentActivity() {
    return [
      ...this.sessions.map(s => ({
        type: 'SESION',
        date: s.createdAt,
        title: `Sesión ${s.status.toLowerCase()}: ${s.topic}`,
        user: s.teacherName
      })),
      ...this.reviews.map(r => ({
        type: 'CALIFICACION',
        date: r.createdAt,
        title: `Calificación otorgada: ${r.rating} ⭐`,
        user: r.fromUserName
      }))
    ].sort((a, b) => new Date(b.date) - new Date(a.date)).slice(0, 8)
  }
}

export const mockStorage = new MockStorageService()
