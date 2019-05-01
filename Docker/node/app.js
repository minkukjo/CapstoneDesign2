const express = require("express");
const app = express();
const path = require("path");
const cors = require("cors");

var port = 8080;
var str;


app.use(express.json());
app.use(cors());
app.use(express.urlencoded({ extended: false}));

app.get("/",(req,res)=>{
	if(!str)
	{
		console.log("Empty");
		res.send("Empty");

	}
	else
	{
		res.send(str);
		str = null;
	}
});

app.post("/",(req,res)=>{
	str = req.body.word;
	console.log(str);
	res.send("back");
});

app.listen(8080,() => {
	console.log(8080,"is Waiting");
});

