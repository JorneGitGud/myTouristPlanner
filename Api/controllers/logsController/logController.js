const router = require("express").Router();
const LogModel = require("../../models/LogModel");
const { HttpError } = require("../../utils/utils");
//new
router.post("/", async (req, res, next) => {
  try {
    const log = await LogModel.create({
      BikeId: req.body.BikeId,
      // Time: req.body.Time,
      X: req.body.X,
      Y: req.body.Y,
    });
    res.json(log);
  } catch (error) {
    next(error);
  }
});
//get all
router.get("/", async (req, res, next) => {
  try {
    const logs = await LogModel.find();
    res.json(logs);
  } catch (error) {
    next(error);
  }
});
//get by id
router.get("/:id", async (req, res, next) => {
  try {
    const result = await LogModel.findById(req.params.id);
    if (!result) {
      return next(new HttpError(404, "log not found"));
    }
    res.json(result);
  } catch (error) {
    next(error);
  }
});

//update
router.put("/:id", async (req, res, next) => {
  try {
    const log = await LogModel.findOneAndUpdate(
      { _id: req.params.id },
      {
        BikeId: req.body.BikeId,
        Time: req.body.Time,
        X: req.body.X,
        Y: req.body.Y,
      },
      { new: true, useFindAndModify: false } //upsert: true  if you want to add it when none exists
    );
    res.json(log);
  } catch (error) {
    next(error);
  }
});
//delete

router.delete("/:id", async (req, res, next) => {
  try {
    const result = await LogModel.deleteOne({ _id: req.params.id });
    res.json({
      error: false,
      deleted_count: result.deletedCount,
    });
  } catch (error) {
    next(error);
  }
});

module.exports = router;
