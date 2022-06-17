<script lang="ts">
  import { onMount } from 'svelte'
  import { ShortenURL } from '$lib/URLShortnerService'
  import { variables } from '../variables'

  let res = 'Loading...'
  let err: string = ''
  let url = 'http://google.com'
  let url_textfield: any

  let r: any

  onMount(async () => {
    await import('@material/mwc-button')
    await import('@material/mwc-textfield')
    await import('@material/mwc-linear-progress')
    res = 'Loaded'

    fetch(variables.BACKEND_API_URL)
      .then(a => a.json())
      .then(a => (r = a))
  })

  const generate_url = async (e: any) => {
    // check if url is valid
    if (url_textfield.value.length > 0 && url_textfield.checkValidity()) {
      url = url_textfield.value
      e.target.disabled = true
      url_textfield.disabled = true
      try {
        let u = await ShortenURL(url)
        console.log(u)
      } catch (error) {
        err = 'Error creating your URL. Please try again.'
      }
      e.target.disabled = false
      url_textfield.disabled = false
      return
    } else {
      err = 'Please enter a valid URL.'
      return
    }
  }
</script>

<h1 class="title">URL Shortner</h1>
<mwc-linear-progress indeterminate />

<div class="url-widget">
  <mwc-textfield bind:this={url_textfield} label="URL" type="url" outlined />

  <mwc-button on:click={generate_url} label="generate url" />
</div>

{#if err.length > 0}
  <div class="error">
    {err}
  </div>
{/if}

{#if res === 'Loading...'}
  <p>Loading...</p>
{/if}

{#if r}
  {JSON.stringify(r)}
{/if}

<style>
  .url-widget {
    display: flex;
    flex-direction: column;
    width: min(calc(100% - 2rem), 500px);
    gap: 1rem;
  }

  mwc-linear-progress {
    position: absolute;
    top: 0;
    width: 100%;
  }

  .error {
    color: var(--error-color, hsl(0, 100%, 60%));
    position: absolute;
    top: 1rem;
  }
</style>
