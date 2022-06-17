<main>
  <slot />
</main>

<style>
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  :global(h1.title) {
    font-size: 3rem;
    font-weight: 100;
    text-align: center;
    margin-bottom: 1rem;
  }
</style>