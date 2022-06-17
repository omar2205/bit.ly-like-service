<script lang="ts">
  import { onMount } from 'svelte'
  import { variables } from '../variables'

  let res = 'Loading...'

  onMount(() => {
    fetch(variables.BACKEND_API_URL)
    .then(r => r.json())
    .then(r => res = r)
  })
</script>

<h1>Welcome to SvelteKit!</h1>
<p>
  Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation
</p>

{#if res === 'Loading...'}
  <p>Loading...</p>
{:else}
<pre>
{JSON.stringify(res, null, 2)}
</pre>
{/if}