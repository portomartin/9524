export const formatDuration = (minutes) => `${minutes} min`

export const formatPublishedAt = (date) => new Intl.DateTimeFormat('es-AR', {
  day: 'numeric', month: 'long', year: 'numeric',
}).format(new Date(date))
