<template>
  <section>
    <!-- Default form login -->
    <template v-if="credentials.status !== 'created'">
      <div class="text-center px-5 pb-5">
        <p class="h4 mb-4">Sign in</p>

        <div v-if="credentials.status == 'invalid'" class="alert alert-danger" role="alert">
          Your username or password is incorrect.
        </div>

        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" class="form-control" id="username" rows="3" v-model="username" />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" class="form-control" id="password" v-model="password" />
        </div>

        <!-- Sign in button -->
        <button id="button-sign-in" class="btn btn-info btn-block my-4 mx-0" @click="signIn()">
          Sign in
        </button>
      </div>

      <div class="text-center px-5">
        <!-- Register -->
        <p class="h4 my-4">Create a new sandbox</p>

        <button class="btn btn-success btn-block" @click="newInstance">New sandbox</button>
      </div>
      <!-- Default form login -->
    </template>
    <template v-else>
      <div class="text-center px-5 pb-5">
        <p class="h4 mb-4">Your credentials</p>
        <p><b>Username:</b> {{ credentials.username }}</p>
        <p><b>Password:</b> {{ credentials.password }}</p>
        <button @click="continueToPage" class="btn btn-info btn-block my-4 mx-0">Continue</button>
      </div>
    </template>
  </section>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  computed: {
    ...mapState(["credentials"])
  },
  methods: {
    newInstance() {
      this.$store.dispatch("createInstance");
    },
    signIn() {
      this.$store.dispatch("logIn", { username: this.username, password: this.password });
    },
    continueToPage() {
      this.$store.dispatch("continueAfterRegister");
    }
  }
};
</script>
