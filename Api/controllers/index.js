const router = require("express").Router();
const bikeController = require("./bikesController/bikeController");
const placeController = require("./placesController/placeController");
const logController = require("./logsController/logController");

router.use("/bikes", bikeController);
router.use("/places", placeController);
router.use("/logs", logController);

module.exports = router;
