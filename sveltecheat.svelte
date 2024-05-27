<script type="ts">
  let disableControls = false
  let selectedOption = "one"
  let isChecked = false
  const myArray = ['one', 'two', 'three']
  const myObject = {
    'first': 123,
    'second': 3.14,
    'third': 'threeeee'
  }

  // displaying the value changed in time + computing the running time
  const startTime = Date.now()
  let ms = 250
  let runtime = 0
  const incr = () => (runtime = (Date.now()-startTime)/1000.)
  let clear
  $: {
    clearInterval(clear)
    clear = setInterval(incr, ms)
  }
</script>

<style>
  /* gradient: percents are center points of the color - color is mixed between the two adjacent points */
</style>

<svelte:head><title>Testing page</title></svelte:head>
<h1>Testing page</h1>

<p>
  Running time: {runtime}
</p>

<!-- Iterating -->
{#each myArray as name, index}
  <li>#{index}: {name}</li>
{/each}
{#each Object.entries(myObject) as [key, value], index (key)}
  <li>#{index}: {key}: {value}</li>
{/each}

<!-- Forms and inputs -->
<select bind:value={selectedOption} disabled={disableControls}>
  <option value="one">First</option>
  <option value="two">Second</option>
  <option value="three">Third</option>
</select>
<label>
  <input type="checkbox" bind:checked={isChecked} disabled={disableControls}>
  Checkbox testing
</label>
<label>
  <input type="range" min="1" max="100" value="50">
  Slider
</label>
<button on:click={() => alert('Button clicked!')}>Click me!</button>