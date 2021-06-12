const router = require("express").Router();
const bikeController = require("./bikesController/bikeController");

router.use("/bikes", bikeController);

module.exports = router;
