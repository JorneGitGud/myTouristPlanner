const mongoose = require("mongoose");

const bikeSchema = new mongoose.Schema({
  bikeId: Number,
  X: Number,
  Y: Number,
});

const BikeModel = mongoose.model("Bikes", bikeSchema);

module.exports = BikeModel;
