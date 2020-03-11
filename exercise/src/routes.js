import Home from "./components/Home.vue";
import Tips from "./components/Tips.vue";
import ExerciseOne from "./components/ExerciseOne.vue";
import ExerciseTwo from "./components/ExerciseTwo.vue";
import ExerciseThree from "./components/ExerciseThree.vue";
import ExerciseBonus from "./components/ExerciseBonus.vue";
import Sandbox from "./components/Sandbox.vue";

export const routes = [
  {
    path: "/",
    component: Home
  },
  {
    path: "/tips",
    component: Tips
  },
  {
    path: "/exercise-1",
    component: ExerciseOne
  },
  {
    path: "/exercise-2",
    component: ExerciseTwo
  },
  {
    path: "/exercise-3",
    component: ExerciseThree
  },
  {
    path: "/exercise-regex",
    component: ExerciseBonus
  },
  {
    path: "/sandbox",
    component: Sandbox
  }
];
