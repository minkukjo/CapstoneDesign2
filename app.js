const express = require("express");
const path = require("path");
const cors = require("cors");

const { sequelize } = require("./models");

const homeRouter = require("./routes/home");

const app = express();

var port = 8080;

sequelize.sync();

app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");
//app.set("port", process.env.PORT || 8001);

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use("/", homeRouter);

app.use((req, res, next) => {
  const err = new Error("Not Found");
  err.status = 404;
  next(err);
});

// app.use((err, req, res) => {
//   res.locals.message = err.message;
//   res.locals.error = req.app.get("env") === "development" ? err : {};
//   res.status(err.status || 500);
//   res.render("error");
// });

// app.listen(app.get("port"), () => {
//   console.log(app.get("port"), "번 포트에서 대기 중");
// });

//app.post("/", (req, res) => {
//  console.log(req.body.word);
//   res.render("show", { word: req.body.word });
//   res.render("show", {
//     word: req.body.word
//});
// app.use((req, res, next) => {
//   const err = new Error("Not Found");
//   err.status = 404;
//   next(err);
// });

app.listen(8080, () => {
  console.log(8080, "번 포트에서 대기중");
});
