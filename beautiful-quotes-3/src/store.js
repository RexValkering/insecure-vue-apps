import Vue from "vue";
import Vuex from "vuex";
import api from "@/api.js";

Vue.use(Vuex);

var defaultQuotes = function() {
  return [
    {
      quote: "Have you tried turning it off and on again?",
      author: "The IT-crowd",
      source: "https://en.wikipedia.org/wiki/The_IT_Crowd",
      styling: "font-weight: bold",
      submitter: ""
    },
    {
      quote: "2b || !2b",
      author: "Anonymous",
      source: "",
      styling: "font-family: monospace",
      submitter: ""
    }
  ];
};

export default new Vuex.Store({
  state: {
    quotes: [],
    project: {
      id: "beautiful-quotes-3",
      name: "Beautiful Quotes 3"
    },
    instance: {
      instanceId: localStorage.getItem("instance-id") || "",
      authToken: localStorage.getItem("auth-token") || "",
      flag: null,
      me: null
    },
    credentials: {
      username: "",
      password: "",
      status: null
    }
  },
  getters: {
    isAuthenticated: state => state.instance.authToken !== "",
    getHeaders: state => {
      return { headers: { Authorization: "bearer " + state.instance.authToken } };
    },
    getUsername: state => state.instance.username
  },
  mutations: {
    setToken: (state, token) => {
      state.instance.authToken = token;
      localStorage.setItem("auth-token", token);
    },

    setInstance: (state, instance) => {
      state.instance.instanceId = instance;
      localStorage.setItem("instance_id", instance);
    },

    setGreeting: (state, greeting) => {
      state.instance.greeting = greeting;
    },

    setUsername: (state, username) => {
      state.instance.username = username;
    },

    addQuote: (state, quote) => {
      state.quotes.push(quote);
    },

    setQuotes: (state, quotes) => {
      state.quotes = quotes;
    },

    setCredentials: (state, { username, password }) => {
      state.credentials.username = username;
      state.credentials.password = password;
      state.credentials.status = "created";
    },

    clearCredentials: state => {
      state.credentials.username = "";
      state.credentials.password = "";
      state.credentials.status = null;
    },

    setCredentialsStatus: (state, status) => {
      state.credentials.status = status;
    },

    setUser: (state, user) => {
      state.instance.me = user;
    },

    setFlag: (state, flag) => {
      state.instance.flag = flag;
    }
  },
  actions: {
    fetchQuotes: ({ commit, getters }) => {
      return api.get("/data", getters.getHeaders).then(response => {
        let quotes = defaultQuotes();
        quotes.push(...response.data);
        commit("setQuotes", quotes);
      });
    },
    addQuote: ({ commit, dispatch, getters }, { author, quote, source, styling }) => {
      const data = { author, quote, source, styling };
      return api.post(`/data`, data, getters.getHeaders).then(response => {
        return dispatch("fetchQuotes");
      });
    },
    resetQuotes: ({ dispatch, getters }) => {
      return api.delete("/data", getters.getHeaders).then(response => dispatch("fetchQuotes"));
    },
    createInstance: ({ state, commit, dispatch }) => {
      return api.post(`/instances`, { project_id: state.project.id }).then(response => {
        commit("setCredentials", response.data);
        return dispatch("logIn", {
          username: state.credentials.username,
          password: state.credentials.password
        });
      });
    },
    logIn: ({ commit }, { username, password }) => {
      return api
        .post("/login", { username, password })
        .then(response => {
          commit("setToken", response.data.token);
          commit("setInstance", response.data.instance_id);
          commit("setGreeting", response.data.greeting);
        })
        .catch(() => {
          commit("setCredentialsStatus", "invalid");
        });
    },
    continueAfterRegister: ({ commit }) => {
      return commit("clearCredentials");
    },
    logOut: ({ commit }) => {
      commit("setToken", "");
      commit("setInstance", "");
      commit("setUsername", "");
      commit("setGreeting", "Log in to continue");
      commit("clearCredentials");
    },
    loadUser: ({ commit, getters }) => {
      return api.get("/login", getters.getHeaders).then(response => {
        commit("setUser", response.data);
      });
    },
    loadFlag: ({ commit, getters }) => {
      return api
        .get("/flag", getters.getHeaders)
        .then(response => commit("setFlag", response.data.flag));
    },
    makeAdmin: ({ getters }, submitter) => {
      return api.post("/makeadmin", { username: submitter }, getters.getHeaders);
    }
  }
});
