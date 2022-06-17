import { variables } from '../variables'

const ShortenURL = async (url: string): Promise<string> => {
  return fetch(variables.BACKEND_API_URL + '/api/v1/create', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ url })
  })
  .then(r => r.json())
}

export {
  ShortenURL
}