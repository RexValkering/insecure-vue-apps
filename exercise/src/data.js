const exerciseData = require("@/assets/exercises.json");

const getData = name => {
  return exerciseData[name];
};

export { getData };
