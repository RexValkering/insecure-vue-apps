import Vue from "vue";
import Vuex from "vuex";
import api from "@/api.js";

Vue.use(Vuex);

var defaultQuotes = function() {
  return [
    {
      quote:
        "The best thing about a boolean is even if you are wrong, you are only <i>off by a bit</i>.",
      author: "Anonymous"
    },
    {
      quote: "It's not a <strong>bug</strong> – it’s an undocumented <strong>feature</strong>.",
      author: "Anonymous"
    },
    {
      quote: "Deleted code is debugged code.",
      author: "Jeff Sickel"
    },
    {
      quote: "One man’s crappy software is another man’s <u>full-time job</u>.",
      author: "Jessica Gaston"
    }
  ];
};

export default new Vuex.Store({
  state: {
    quotes: [],
    project: {
      id: "beautiful-quotes",
      name: "Beautiful Quotes"
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
    }
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

    addQuote: (state, quote) => {
      state.quotes.push(quote);
    },

    setQuotes: (state, quotes) => {
      state.quotes = quotes;
    },

    setCredentials: (state, { username, password, isAdmin }) => {
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
    addQuote: ({ commit, getters }, { author, quote }) => {
      const data = { author, quote };
      return api.post(`/data`, data, getters.getHeaders).then(response => {
        commit("addQuote", data);
        return response;
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
    logIn: ({ commit, dispatch }, { username, password }) => {
      return api
        .post("/login", { username, password })
        .then(response => {
          commit("setToken", response.data.token);
          commit("setInstance", response.data.instance_id);

          return dispatch("loadUser");
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
    }
  }
});
