const mongoose = require("mongoose");

const logSchema = new mongoose.Schema({
  BikeId: Number,
  Time: Date, //2021-06-11T22:00:00.000+00:00
  X: Number,
  Y: Number,
});

const LogModel = mongoose.model("Logs", logSchema);

module.exports = LogModel;
