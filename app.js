const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");

var port = 8080;

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.use(express.json());
app.use(cors());
app.use(express.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  res.render("show");
});

app.post("/", (req, res) => {
  console.log(req.body.word);
  //   res.render("show", { word: req.body.word });
  //   res.render("show", {
  //     word: req.body.word
});
// app.use((req, res, next) => {
//   const err = new Error("Not Found");
//   err.status = 404;
//   next(err);
// });

app.listen(8080, () => {
  console.log(8080, "번 포트에서 대기중");
});
