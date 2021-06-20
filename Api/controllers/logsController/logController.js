const router = require("express").Router();
const LogModel = require("../../models/LogModel");
const { HttpError } = require("../../utils/utils");
//new
router.post("/", async (req, res, next) => {
  console.log("here")
  try {
    const log = await LogModel.create({
      BikeId: req.body.BikeId,
      Time: Date(Date.now()),
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

module.exports = router;
