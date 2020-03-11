<template>
  <div id="app" class="text-left mt-3 mt-md-5 mb-md-5 pt-md-5">
    <div class="container">
      <div class="row">
        <div class="col col-md-3 col-sm-6 col-12">
          <h3 class="mt-4 mb-4"><strong>Insecure Vue Apps</strong></h3>
          <p><router-link to="/">Home</router-link></p>
          <p><router-link to="/sandbox">Sandbox</router-link></p>
          <p><router-link to="/tips">Tips and useful pieces of code</router-link></p>
          <hr />
          <p><router-link to="/exercise-1">Exercise 1: Abusing v-html</router-link></p>
          <p><router-link to="/exercise-2">Exercise 2: Abusing v-href</router-link></p>
          <p><router-link to="/exercise-3">Exercise 3: Clickjacking</router-link></p>
          <p><router-link to="/exercise-regex">Bonus exercise: Beautiful Regex</router-link></p>
        </div>

        <div class="col col-md-9 pl-md-5">
          <transition name="slide" mode="out-in">
            <router-view :key="$route.fullPath"></router-view>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style>
a {
  color: #246b81;
}

.slide-enter-active {
  animation: slide-in 200ms ease-out forwards;
}

.slide-leave-active {
  animation: slide-out 200ms ease-out forwards;
}

@keyframes slide-in {
  from {
    transform: translateY(-30px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes slide-out {
  from {
    transform: translateY(0px);
    opacity: 1;
  }
  to {
    transform: translateY(-30);
    opacity: 0;
  }
}
</style>
