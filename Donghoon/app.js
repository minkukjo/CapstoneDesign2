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
app.use(express.static(path.join(__dirname, "/")));

app.use("/", homeRouter);

app.use((req, res, next) => {
  const err = new Error("Not Found");
  err.status = 404;
  next(err);
});

app.listen(8080, () => {
  console.log(8080, "번 포트에서 대기중");
});
