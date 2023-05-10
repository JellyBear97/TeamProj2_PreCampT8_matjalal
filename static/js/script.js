//   김선아
$(document).ready(function (event) {
   show_order();
  set_temp();
  post();
});

//   이지은님 헤더쪽
function post() {
  $("#post-close").on("click", function () {
    $("#post-box").hide();
  });
  $("#post-start").on("click", function () {
    $("#post-box").show();
  });
}

// // 날씨 API FETCH로 가져오기
function set_temp() {
  fetch("http://spartacodingclub.shop/sparta_api/weather/seoul")
    .then((res) => res.json())
    .then((data) => {
      let temp = data["temp"];
      let city = data["city"];
      let clouds = data["clouds"];
      let icon = data["icon"];
      temp_html = ``;
      if (temp > 20) {
        temp_html = `

`;
      } else {
        temp_html = `

`;
      }

      $("#temp").text(temp);
    });
}
function show_order() {
  // GET 요청 확인 fetch 코드 (READ)
  fetch("/test")
    .then((res) => res.json())
    .then((data) => {
      console.log(data);//'msg': '이 요청은 GET!'
      // alert(data["msg"]); //'msg': '이 요청은 GET!'

      let rows = data["result"];
      console.log(rows);
      $(".cards  ").empty();
      rows.forEach((a) => {
        console.log(a);
        let desc = a["desc"];
        let image = a["image"];
        let title = a["title"];
        let comment = a["comment"];
        let weather=a["weather"]
        let star = a["star"];
        let star_num = "⭐".repeat(star);
        console.log(desc, image, title, comment, star_num);

        let temp_html = `<div class="col">
        <div class="card h-80">
          <span class="card-weather sunny">
            <i class="fa-solid fa-sun"></i>
          </span>
          <img src="${image}">

          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <p class="card-star">${star_num}</p>
            <p class="card-address">${star_num}</p>
            <p class="card-comment">
            ${comment}
            </p>
          </div>
          <div class="card-footer more">
            <small class="text-muted"><i class="fa-solid fa-plus"></i>더보기</small>
          </div>
        </div>
      </div>
      `;
        $(".cards  ").append(temp_html);
      });
    });
}

// 날씨에 따른 맛집 평점 가져오기
function save_order(){
// event.preventDefault();
let url = $("#restaurant-url").val();
// https://congsong.tistory.com/42
let weather = $('input[type="radio"]:checked').val(); // 체크된 값(checked value)
let comment = $("#restaurant-comment").val();

console.log(url, weather, comment);
// post 요청 확인 fetch 코드(CREATE,UPDATE,DELATE)
let formData = new FormData();
formData.append("url_give", url);
formData.append("weather_give", weather);
formData.append("comment_give", comment);

fetch("/test", { method: "POST", body: formData })
  .then((res) => res.json())
  .then((data) => {
    // console.log(data["msg"]);
    // alert(data["msg"]);
//  window.location.reload()
});

// JSON 자료 불러와서 자료형으로 나누기
// fetch("http://spartacodingclub.shop/sparta_api/seoulair")
//   .then((res) => res.json())
//   .then((data) => {
//     let rows = data["RealtimeCityAir"]["row"];
//     rows.forEach((a) => {
//       let gue_name = a["MSRSTE_NM"];
//       let gue_mise = a["IDEX_MVL"];

//       //   별점
//       // let star_num="⭐".repeat(star)
//       //   별점

//       console.log(gue_name, gue_mise);
//       let temp_html = ``;

//       if (gue_mise > 40) {
//         temp_html = `<li class=bad>${gue_name} : ${gue_mise}</li>`;
//       } else {
//         temp_html = `<li >${gue_name} : ${gue_mise}</li>`;
//       }

//       $("#names-q1").append(temp_html);
//     });
//   });


}