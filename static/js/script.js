$(document).ready(function () {
  set_temp();
  post();
  show_order();
});

function post() {
  // 음식 추천하기 버튼
  $('#post-start').on('click', function () {
    $('#post-box').toggle();
  });
  // CLOSE 버튼
  $('#post-close').on('click', function () {
    $('#post-box').hide();
  });
}

function posting() {
  let weather = $('#select-weather input[type="radio"]:checked').val();
  let menu = $('#menu_title').val();
  let img = $('#food_img_url').val();
  let comment = $('#comment').val();

  // form의 유효성 검사
  if (!weather) {
    alert('날씨를 선택해주세요.');
    return;
  }
  if (!menu) {
    alert('메뉴를 입력해주세요.');
    return;
  }
  // if (!img) {
  //   alert("이미지 URL을 입력해주세요.");
  //   return;
  // }
  if (!comment) {
    alert('한줄평을 입력해주세요.');
    return;
  }

  let formData = new FormData();
  formData.append('weather_give', weather);
  formData.append('menu_give', menu);
  formData.append('img_give', img);
  formData.append('comment_give', comment);

  fetch('/foodlist', { method: 'POST', body: formData })
    .then((res) => res.json())
    .then((data) => {
      alert(data['msg']);
      window.location.reload();
    });
}

// 카테고리 상관없이 모든 foodlist 가져오기
function show_order() {
  fetch('/foodlist')
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      // alert(data["msg"]);

      let rows = data['result'];
      console.log(rows);

      // ! 잠시 none
      $('.cards  ').empty();
      rows.forEach((a) => {
        console.log(a);
        let menu = a['menu'];
        let img = a['img'];
        let comment = a['comment'];
        let p_id = a['_id'];
        let weather = a['weather'];
        let weather_span = '';
        let weather_i = '';
        if (weather == 1) {
          weather_span = 'sunny';
          weather_i = 'sun';
        } else if (weather == 2) {
          weather_span = 'cloudy';
          weather_i = 'cloud';
        } else if (weather == 3) {
          weather_span = 'rainy';
          weather_i = 'umbrella';
        } else if (weather == 4) {
          weather_span = 'snowy';
          weather_i = 'snowflake';
        }

        console.log(weather, menu, comment, img, p_id, weather_span, weather_i);

        let temp_html = `
                        <div class="col" id=${p_id}>
                          <div class="card h-80">
                            <span class="card-weather ${weather_span}">
                              <i class="fa-solid fa-${weather_i}"></i>
                            </span>
                            <img
                              src="${img}"
                              class="card-img-top"
                              alt="음식 대표사진" />

                            <div class="card-body">
                              <h5 class="card-title">${menu}</h5>
                              <p class="card-comment">${comment}</p>
                            </div>
                            <div class="card-footer more">
                              <small class="text-muted"><i class="fa-solid fa-plus"></i>더보기</small>
                            </div>
                          </div>
                        </div>
                        `;
        $('#cards').append(temp_html);
      });
    });
}

// weather 카테고리 클릭시 - foodlist 불러오기
function showByWeather(weather_value) {
  // fetch('/foodlist/weather')
  fetch(`/foodlist/weather?weather_value=${weather_value}`)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      // alert(data["msg"]);

      let rows = data['result'];
      console.log(rows);

      // ! 잠시 none
      $('.cards  ').empty();
      rows.forEach((a) => {
        console.log(a);
        let menu = a['menu'];
        let img = a['img'];
        let comment = a['comment'];
        let p_id = a['_id'];
        let weather = a['weather'];
        let weather_span = '';
        let weather_i = '';
        if (weather == 1) {
          weather_span = 'sunny';
          weather_i = 'sun';
        } else if (weather == 2) {
          weather_span = 'cloudy';
          weather_i = 'cloud';
        } else if (weather == 3) {
          weather_span = 'rainy';
          weather_i = 'umbrella';
        } else if (weather == 4) {
          weather_span = 'snowy';
          weather_i = 'snowflake';
        }

        console.log(weather, menu, comment, img, p_id, weather_span, weather_i);

        let temp_html = `
                      <div class="col" id=${p_id}>
                        <div class="card h-80">
                          <span class="card-weather ${weather_span}">
                            <i class="fa-solid fa-${weather_i}"></i>
                          </span>
                          <img
                            src="${img}"
                            class="card-img-top"
                            alt="음식 대표사진" />

                          <div class="card-body">
                            <h5 class="card-title">${menu}</h5>
                            <p class="card-comment">${comment}</p>
                          </div>
                          <div class="card-footer more">
                            <small class="text-muted"><i class="fa-solid fa-plus"></i>더보기</small>
                          </div>
                        </div>
                      </div>
                      `;
        $('#cards').append(temp_html);
      });
    });
}

// 날씨 불러오기
function set_temp() {
  fetch('http://spartacodingclub.shop/sparta_api/weather/seoul')
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      let temp = data['temp'].toFixed(1);
      let city = data['city'];
      let clouds = data['clouds'];
      let iconurl = data['icon'];

      $('#temp').text(temp);
      $('#city').text(city);
      $('#clouds').text(clouds);
      $('#icon').attr('src', iconurl);
    });
}
