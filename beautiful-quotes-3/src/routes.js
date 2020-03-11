import Quotes from "./components/Quotes.vue";

export const routes = [
  {
    path: "/",
    component: Quotes
  },
  {
    path: "/make-admin/:username",
    component: Quotes,
    props: true
  }
];
