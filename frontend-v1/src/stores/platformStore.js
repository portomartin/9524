import { computed, reactive } from 'vue'
import { publicLearningNeeds, publicOffers } from '../mocks/publicCatalogData'

const STORAGE_KEY = 'intercambia-mock-state-v1'

const initialState = {
  currentUserId: null,
  users: [
    { id: 'usr-demo', email: 'demo@9524.test', password: 'demo1234', role: 'USER', status: 'ACTIVE', name: 'Martín Demo', description: 'Me gusta aprender y compartir herramientas digitales.', generalLocation: 'Buenos Aires', teachingTopics: ['Gestión de proyectos', 'Planillas'], learningTopics: ['Inglés', 'Fotografía'] },
    { id: 'usr-admin', email: 'admin@9524.test', password: 'admin1234', role: 'ADMIN', status: 'ACTIVE', name: 'Administración 9524', description: '', generalLocation: '', teachingTopics: [], learningTopics: [] },
  ],
  offers: publicOffers,
  learningNeeds: publicLearningNeeds,
  ownOffers: [],
  ownLearningNeeds: [],
  availability: [],
  availabilityPublic: false,
  publicAgendas: [
    { id: 'pub-av-1', userName: 'Lucía M.', date: '2026-10-15', startTime: '17:00', durationMinutes: 60 },
    { id: 'pub-av-2', userName: 'Elena P.', date: '2026-10-18', startTime: '10:00', durationMinutes: 90 },
  ],
  sessions: [
    { id: 'ses-demo-finished', offerId: 'offer-conversation-english', title: 'Conversación en inglés para entrevistas', counterpart: 'Tomás R.', proposedDate: '2026-10-01', startTime: '18:00', durationMinutes: 45, modality: 'Virtual', exchangeType: 'CREDITS', creditCost: 1, status: 'FINALIZADA', participantIds: ['usr-demo', 'usr-tomas'], rated: false },
    { id: 'ses-demo-requested', offerId: 'offer-vue-basics', title: 'Introducción práctica a Vue 3', counterpart: 'Lucía M.', proposedDate: '2026-10-15', startTime: '17:00', durationMinutes: 60, modality: 'Virtual', exchangeType: 'RECIPROCAL', creditCost: 0, status: 'SOLICITADA', participantIds: ['usr-demo', 'usr-lucia'], rated: false },
  ],
  creditBalance: 5,
  creditMovements: [
    { id: 'mov-1', date: '2026-10-01', description: 'Sesión de conversación en inglés', amount: -1 },
    { id: 'mov-2', date: '2026-09-28', description: 'Sesión enseñada: gestión de proyectos', amount: 2 },
  ],
  ratings: [
    { id: 'rating-1', userId: 'usr-lucia', userName: 'Lucía M.', score: 4.8, count: 12 },
    { id: 'rating-2', userId: 'usr-tomas', userName: 'Tomás R.', score: 4.7, count: 9 },
    { id: 'rating-3', userId: 'usr-elena', userName: 'Elena P.', score: 4.6, count: 7 },
  ],
  reports: [
    { id: 'rep-1', targetType: 'OFFER', targetId: 'offer-urban-garden', targetLabel: 'Tu primera huerta urbana', reasonCode: 'OTHER', description: 'Revisar información de modalidad.', status: 'OPEN' },
  ],
}

function loadState() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY)
    return saved ? { ...structuredClone(initialState), ...JSON.parse(saved) } : structuredClone(initialState)
  } catch {
    return structuredClone(initialState)
  }
}

const state = reactive(loadState())
const currentUser = computed(() => state.users.find(({ id }) => id === state.currentUserId) || null)
const isAuthenticated = computed(() => Boolean(currentUser.value))
const isAdmin = computed(() => currentUser.value?.role === 'ADMIN')

const persist = () => localStorage.setItem(STORAGE_KEY, JSON.stringify(state))
const wait = (milliseconds = 250) => new Promise((resolve) => setTimeout(resolve, milliseconds))
const makeId = (prefix) => `${prefix}-${Date.now()}-${Math.random().toString(16).slice(2)}`

async function login(email, password) {
  await wait()
  const user = state.users.find((candidate) => candidate.email.toLowerCase() === email.toLowerCase() && candidate.password === password)
  if (!user || user.status !== 'ACTIVE') throw new Error('Credenciales inválidas o cuenta no disponible.')
  state.currentUserId = user.id
  persist()
  return user
}

async function register(email, password) {
  await wait()
  if (state.users.some((user) => user.email.toLowerCase() === email.toLowerCase())) throw new Error('Ya existe una cuenta con ese correo.')
  const user = { id: makeId('usr'), email, password, role: 'USER', status: 'ACTIVE', name: email.split('@')[0], description: '', generalLocation: '', teachingTopics: [], learningTopics: [] }
  state.users.push(user)
  state.currentUserId = user.id
  persist()
  return user
}

function logout() { state.currentUserId = null; persist() }

function updateProfile(profile) { Object.assign(currentUser.value, profile); persist() }

function saveOffer(offer) {
  const existing = state.ownOffers.find((item) => item.id === offer.id)
  const normalized = { ...offer, id: offer.id || makeId('offer'), authorDisplayName: currentUser.value.name, publishedAt: offer.publishedAt || new Date().toISOString() }
  if (existing) Object.assign(existing, normalized); else state.ownOffers.push(normalized)
  if (normalized.status === 'PUBLISHED' && !state.offers.some(({ id }) => id === normalized.id)) state.offers.push(normalized)
  persist(); return normalized
}

function saveLearningNeed(item) {
  const existing = state.ownLearningNeeds.find((candidate) => candidate.id === item.id)
  const normalized = { ...item, id: item.id || makeId('need'), authorDisplayName: currentUser.value.name, publishedAt: item.publishedAt || new Date().toISOString() }
  if (existing) Object.assign(existing, normalized); else state.ownLearningNeeds.push(normalized)
  persist(); return normalized
}

function removeLearningNeed(id) { state.ownLearningNeeds = state.ownLearningNeeds.filter((item) => item.id !== id); persist() }
function setLearningNeedStatus(id, status) { const item = state.ownLearningNeeds.find((candidate) => candidate.id === id); if (item) item.status = status; persist() }
function addAvailability(slot) { state.availability.push({ ...slot, id: makeId('av'), status: 'FREE' }); persist() }
function removeAvailability(id) { state.availability = state.availability.filter((item) => item.id !== id); persist() }
function setAvailabilityVisibility(value) { state.availabilityPublic = value; persist() }

function createSession(payload) {
  const offer = [...state.offers, ...state.ownOffers].find(({ id }) => id === payload.offerId)
  if (!offer) throw new Error('La propuesta seleccionada ya no está disponible.')
  const session = { id: makeId('ses'), title: offer.title, counterpart: offer.authorDisplayName, status: 'SOLICITADA', participantIds: [currentUser.value.id, `owner-${offer.id}`], rated: false, ...payload }
  state.sessions.unshift(session); persist(); return session
}

function transitionSession(id, status) {
  const session = state.sessions.find((item) => item.id === id)
  if (!session) throw new Error('No se encontró la sesión.')
  session.status = status; persist(); return session
}

function rateSession(id, score, comment) {
  const session = state.sessions.find((item) => item.id === id)
  if (!session || session.status !== 'FINALIZADA' || session.rated) throw new Error('Esta sesión no puede calificarse.')
  session.rated = true; session.rating = { score, comment }; persist()
}

function report(payload) { state.reports.unshift({ id: makeId('rep'), status: 'OPEN', ...payload }); persist() }
function resolveReport(id) { const item = state.reports.find((reportItem) => reportItem.id === id); if (item) item.status = 'REVIEWED'; persist() }
function setUserStatus(id, status) { const user = state.users.find((item) => item.id === id); if (user) user.status = status; persist() }
function hideOffer(id) { state.offers = state.offers.filter((item) => item.id !== id); persist() }

export function usePlatformStore() {
  return {
    state, currentUser, isAuthenticated, isAdmin, login, register, logout, updateProfile,
    saveOffer, saveLearningNeed, removeLearningNeed, setLearningNeedStatus, addAvailability, removeAvailability,
    setAvailabilityVisibility, createSession, transitionSession, rateSession, report,
    resolveReport, setUserStatus, hideOffer,
  }
}
