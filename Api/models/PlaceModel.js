const mongoose = require("mongoose");

const placeSchema = new mongoose.Schema({
  Name: String,
  Info: String,
  Genre: String,
  X: Number,
  Y: Number,
});

const PlaceModel = mongoose.model("Places", placeSchema);

module.exports = PlaceModel;
