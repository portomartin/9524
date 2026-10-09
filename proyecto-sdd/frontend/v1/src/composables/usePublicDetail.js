import { ref } from 'vue'

export function usePublicDetail(loader) {
  const item = ref(null)
  const isLoading = ref(false)
  const error = ref(null)

  async function load() {
    isLoading.value = true
    error.value = null
    try {
      item.value = await loader()
    } catch (detailError) {
      item.value = null
      error.value = detailError
    } finally {
      isLoading.value = false
    }
  }

  return { item, isLoading, error, load }
}
