<template>
  <div>
    <new-quote @new-quote="addQuote" />
    <div class="row mt-5">
      <div class="col col-12">
        <h3>Quotes</h3>
      </div>
    </div>

    <div class="row mt-3" v-for="(quote, index) in reversedQuotes" :key="index">
      <div class="col col-12 mb-1">
        <p class="description">{{ quote.quote }}</p>
        <span v-if="quote.source" class="text-muted"
          >Author: <a class="link" :href="quote.source">{{ quote.author }}</a></span
        >
        <span v-else class="text-muted">Author: {{ quote.author }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import NewQuote from "./NewQuote.vue";

export default {
  components: {
    NewQuote
  },
  computed: {
    ...mapState(["quotes"]),
    reversedQuotes() {
      return this.quotes.slice().reverse();
    }
  },
  methods: {
    addQuote(event) {
      this.$store.dispatch("addQuote", event);
    }
  },
  created() {
    this.$store.dispatch("fetchQuotes");
  }
};
</script>

<style scoped>
.description {
  margin-bottom: 0px;
}

a.link {
  text-decoration: underline;
}
</style>
