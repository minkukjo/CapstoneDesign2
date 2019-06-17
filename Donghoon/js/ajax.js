$(document).ready(function() {
  len = $(".orders__order.order").length;
  console.log(len);
});
setInterval(function() {
  $.ajax({
    type: "GET",
    url: "/ajax",
    async: true,
    dataType: "json",
    success: function(data) {
      let createdString = new Date(data[data.length-1].createdAt);
      let LocaleTime = createdString.toLocaleTimeString('ko-KR');
      if (len < data.length) {
        $(".orders__list").append(
          `<li class="orders__order order"  onClick="doCheck()">
        <div class="orders__column">
          <div class="order__number item">${data[data.length-1].id}
          </div>
          <div class="order__content item">
            ${data[data.length-1].content}
          </div>
          <div class="order__createdAt item">
            ${LocaleTime}
          </div>
          <div class="order__buttons item">
            <form id="form-delete" action="/delete/${data[data.length-1].id}" method="post">
              <button class="order__delete" onClick="">Delete</button>
            </form>
          </div>
        </div>
      </li>`
        );
        len = data.length;
      }
    }
  });
}, 3000);
