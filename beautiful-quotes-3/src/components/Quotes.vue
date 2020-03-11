<template>
  <div>
    <new-quote @new-quote="addQuote" />
    <div class="row mt-5">
      <div class="col col-12">
        <h3>Quotes</h3>
      </div>
    </div>

    <div class="row mt-3" v-for="(quote, index) in reversedQuotes" :key="index">
      <div class="col col-12 mb-1 d-flex justify-content-between">
        <div>
          <p class="description">{{ quote.quote }}</p>
          <span v-if="cleanLink(quote.source)" class="text-muted"
            >Author:
            <a class="link" :style="quote.styling" :href="cleanLink(quote.source)">{{
              quote.author
            }}</a></span
          >
          <span v-else class="text-muted">Author: {{ quote.author }}</span>
        </div>
        <div>
          <router-link
            :to="'/make-admin/' + quote.submitter"
            tag="button"
            class="btn btn-primary admin-button"
            :disabled="!instance.me || instance.me.admin == 0"
            >Make admin</router-link
          >
        </div>
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
    ...mapState(["quotes", "instance"]),
    reversedQuotes() {
      return this.quotes.slice().reverse();
    }
  },
  methods: {
    addQuote(event) {
      this.$store.dispatch("addQuote", event);
    },
    cleanLink(url) {
      if (!url.startsWith("https://") && !url.startsWith("http://")) {
        if (url)
          console.log(
            "Source '" + url + "' is not a valid link! It should start with http:// or https://"
          );
        return "";
      }

      return url;
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

button.admin-button {
  margin: 0px;
}
</style>
