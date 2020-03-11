<template>
  <section>
    <h3>{{ title }}</h3>
    <div class="alert alert-info my-4">
      <strong>{{ description }}</strong>
    </div>

    <p>
      <strong>Website URL: </strong><a :href="websiteUrl">{{ websiteUrl }}</a>
    </p>
    <p v-translate>Click on 'Create a new sandbox' to create an isolated instance to hack.</p>
    <h4 class="mt-4">Expert difficulty: no hints!</h4>
    <p>
      Can you solve this challenge without hints? Don't forget to look at the
      <router-link to="/tips">Tips page</router-link>
      for examples.
    </p>

    <h4 class="mt-4">Hard difficulty: solve with hints.</h4>
    <p>Click the button below to reveal some hints to help you on your way.</p>
    <section v-if="numberOfHints > 0">
      <ol>
        <li v-for="(hint, index) in shownHints" :key="`hint-${index}`">{{ hint.text }}</li>
      </ol>
    </section>
    <button v-if="numberOfHints < hints.length" class="btn btn-primary" @click="numberOfHints++">
      Reveal next hint
    </button>

    <h4 class="mt-4">Normal difficulty: solve with step-by-step instructions</h4>
    <p>Click the button below to reveal step-by-step instructions.</p>
    <section v-if="numberOfInstructions > 0">
      <ol>
        <li v-for="(hint, index) in shownInstructions" :key="`instruction-${index}`">
          {{ hint.text }}
          <div v-if="hint.code != ''" class="mt-3">
            <pre>{{ hint.code }}</pre>
          </div>
        </li>
      </ol>
    </section>
    <button
      v-if="numberOfInstructions < instructions.length"
      class="btn btn-primary"
      @click="numberOfInstructions++"
    >
      Reveal next instruction
    </button>
  </section>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: null
    },
    description: {
      type: String,
      default: null
    },
    websiteUrl: {
      type: String,
      default: null
    },
    hints: {
      type: Array,
      default: null
    },
    instructions: {
      type: Array,
      default: null
    }
  },
  data() {
    return {
      numberOfHints: 0,
      numberOfInstructions: 0
    };
  },
  computed: {
    shownHints() {
      return this.hints.slice(0, this.numberOfHints);
    },
    shownInstructions() {
      return this.instructions.slice(0, this.numberOfInstructions);
    }
  }
};
</script>
