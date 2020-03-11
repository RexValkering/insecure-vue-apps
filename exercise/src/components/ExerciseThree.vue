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
import { getData } from "@/data";

export default {
  components: {
    ExerciseTemplate: ExerciseTemplate
  },
  data() {
    return getData("Exercise 3");
  }
};
</script>
