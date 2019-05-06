$(document).on("click", ".orders__order.order", function(e) {
  var closeParent = $(e.target).closest("li");
  if(!closeParent.hasClass("checked"))
  closeParent.addClass("checked");
  else
  closeParent.removeClass("checked");
});