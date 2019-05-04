function doCheck() {
  console.log("hey");
  let check = document.getElementsByClassName("orders__order order")[0]
    .classList;
  console.log(check);
  if (check.contains("checked")) {
    check.remove("checked");
  } else check.add("checked");
}
