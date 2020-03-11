<template>
  <exercise-template
    :title="title"
    :description="description"
    :hints="hints"
    :instructions="instructions"
    :websiteUrl="websiteUrl"
  />
</template>

<script>
import ExerciseTemplate from "./Exercise.vue";

export default {
  components: {
    ExerciseTemplate: ExerciseTemplate
  },
  data() {
    return {
      title: "Bonus Exercise: Beautiful Regex (coming soon)",
      description: `You were successful in your efforts: the Administrator has given up on their
      beautiful quotes website. However, there is still one website of theirs you can attack.
      While this website is not vulnerable to cross-site scripting, you have one final trick up your
      sleeve. Will you succeed in making the website unusable?`,
      websiteUrl: "Coming soon!",
      hints: [],
      instructions: []
    };
  }
};
</script>
