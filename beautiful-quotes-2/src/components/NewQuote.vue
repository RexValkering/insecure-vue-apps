<template>
  <div>
    <div class="row">
      <div class="col col-12">
        <h3>Add a new quote</h3>
        <p>
          After sharing your quote, the administrator will log in to read it and check the link, if
          provided.
        </p>
      </div>
    </div>
    <div class="form-group">
      <label for="quote">Quote</label>
      <textarea class="form-control" id="quote" rows="3" v-model="quote"></textarea>
    </div>
    <div class="form-group">
      <label for="author">Author</label>
      <input type="text" class="form-control" id="author" v-model="author" />
    </div>
    <div class="form-group">
      <label for="author">Source</label>
      <input type="text" class="form-control" id="source" v-model="source" />
    </div>
    <button @click="addQuote" role="button" class="btn btn-primary">Submit quote</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      quote: "",
      author: "",
      source: ""
    };
  },
  methods: {
    clearQuote() {
      this.quote = "";
      this.author = "";
      this.source = "";
    },
    addQuote() {
      this.$emit("new-quote", {
        quote: this.quote,
        author: this.author ? this.author : "Anonymous",
        source: this.source
      });
      this.clearQuote();
    }
  }
};
</script>
