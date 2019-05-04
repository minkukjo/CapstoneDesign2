var len = 0;
$(document).ready(function() {
  len = $("#tb tr").length;
  console.log(len);
});
setInterval(function() {
  $.ajax({
    type: "GET",
    url: "/ajax",
    async: true,
    dataType: "json",

    success: function(data) {
      console.log(data.length);
      if (len < data.length) {
        $("#tb").append(
          "<tr><td>" +
            data[data.length - 1].id +
            "</td><td>" +
            data[data.length - 1].content +
            "</td><td>" +
            data[data.length - 1].createdAt +
            "</td></tr>"
        );
        len = data.length;
      }
    }
  });
}, 3000);
