var express = require("express");
var router = express.Router();
var { Order } = require("../models");

router.get("/", function(req, res, next) {
  Order.findAll({}).then(result => {
    res.render("home", {
      orders: result
    });
  });
});

router.get("/ajax", function(req, res, next) {
  Order.findAll({}).then(result => {
    res.send(result);
  });
});

router.post("/", async (req, res, next) => {
  try {
    const order = await Order.create({
      content: req.body.word
    });
    console.log("데이터 추가 완료");
    console.log(req.body.word);
    res.redirect("/");
  } catch (error) {
    console.log("데이터 추가 실패");
    next(error);
  }
});

router.post("/delete/:id", function(req, res, next) {
  let orderID = req.params.id;

  Order.destroy({
    where: { id: orderID }
  })
    .then(result => {
      res.redirect("/");
    })
    .catch(err => {
      console.log("데이터 삭제 실패");
    });
});

module.exports = router;
