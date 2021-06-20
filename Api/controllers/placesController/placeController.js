const router = require("express").Router();
const PlaceModel = require("../../models/PlaceModel");
const { HttpError } = require("../../utils/utils");
//new
router.post("/", async (req, res, next) => {
  try {
    const place = await PlaceModel.create({
      Name: req.body.Name,
      Info: req.body.Info,
      Genre: req.body.Genre,
      X: req.body.X,
      Y: req.body.Y,
    });
    res.json(place);
  } catch (error) {
    next(error);
  }
});
// //get all
router.get("/", async (req, res, next) => {
  console.log(req.body.X);
  try {
    const place = await PlaceModel.find();
    res.json(place);
  } catch (error) {
    next(error);
  }
});
//get by id
router.get("/:id", async (req, res, next) => {
  try {
    const result = await PlaceModel.findById(req.params.id);
    if (!result) {
      return next(new HttpError(404, "Place not found"));
    }
    res.json(result);
  } catch (error) {
    next(error);
  }
});

//get by X and Y Json
router.get("/", async (req, res, next) => {
  console.log(req.body.X);
  try {
    const result = await PlaceModel.findOne({ X: req.body.X, Y: req.body.Y });
    if (!result) {
      return next(new HttpError(404, "Place not found"));
    }
    res.json(result);
  } catch (error) {
    next(error);
  }
});

//get by X and Y
router.get("/:X/:Y", async (req, res, next) => {
  console.log(req.body.X);
  try {
    const result = await PlaceModel.findOne({
      X: req.params.X,
      Y: req.params.Y,
    });
    if (!result) {
      return next(new HttpError(404, "Place not found"));
    }
    res.json(result);
  } catch (error) {
    next(error);
  }
});

//update
router.put("/:id", async (req, res, next) => {
  try {
    const place = await PlaceModel.findOneAndUpdate(
      { _id: req.params.id },
      {
        Name: req.body.Name,
        Info: req.body.Info,
        Genre: req.body.Genre,
        X: req.body.X,
        Y: req.body.Y,
      },
      { new: true, useFindAndModify: false } //upsert: true  if you want to add it when none exists
    );
    res.json(place);
  } catch (error) {
    next(error);
  }
});
//delete

router.delete("/:id", async (req, res, next) => {
  try {
    const result = await PlaceModel.deleteOne({ _id: req.params.id });
    res.json({
      error: false,
      deleted_count: result.deletedCount,
    });
  } catch (error) {
    next(error);
  }
});

module.exports = router;
