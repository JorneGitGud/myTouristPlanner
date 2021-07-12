const router = require("express").Router();
const BikeModel = require("../../models/BikeModel");
const { HttpError } = require("../../utils/utils");
//new
router.post("/", async (req, res, next) => {
  console.log("Bikes")
  try {
    const bike = await BikeModel.create({
      BikeId: req.body.BikeId,
      X: req.body.X,
      Y: req.body.Y,
    });
    res.json(bike);
  } catch (error) {
    next(error);
  }
});
//get all
router.get("/", async (req, res, next) => {
  try {
    const bikes = await BikeModel.find();
    res.json(bikes);
  } catch (error) {
    next(error);
  }
});
//get by id
router.get("/:id", async (req, res, next) => {
  try {
    const result = await BikeModel.findById(req.params.id);
    if (!result) {
      return next(new HttpError(404, "Bike not found"));
    }
    res.json(result);
  } catch (error) {
    next(error);
  }
});

//update
router.put("/:id", async (req, res, next) => {
  try {
    const bike = await BikeModel.findOneAndUpdate(
      { _id: req.params.id },
      {
        BikeId: req.body.BikeId,
        X: req.body.X,
        Y: req.body.Y,
      },
      { new: true, useFindAndModify: false } //upsert: true  if you want to add it when none exists
    );
    res.json(bike);
  } catch (error) {
    next(error);
  }
});
//delete

router.delete("/:id", async (req, res, next) => {
  try {
    const result = await BikeModel.deleteOne({ _id: req.params.id });
    res.json({
      error: false,
      deleted_count: result.deletedCount,
    });
  } catch (error) {
    next(error);
  }
});

module.exports = router;
