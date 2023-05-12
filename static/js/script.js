$(document).ready(function () {
  set_temp();
  post();
  show_order();
  post_modal();
});

function post() {
  // 음식 추천하기 버튼
  $('#post-start').on('click', function () {
    $('#post-box').toggle();
    $('.post-bg').css('display', 'flex');
  });

  // CLOSE 버튼
  $('#post-close').on('click', function () {
    $('#post-box').hide();
    window.location.reload();
  });
}

function post_modal() {
  // 게시글 세부내용 오픈하기
  $('.card').on('click', function () {
    $('#post-modal-wrap').toggle();
    $('#post-modal-wrap').css('display', 'flex');
  });
  // CLOSE버튼
  $('#post-modal-close').on('click', function () {
    $('#post-modal-wrap').hide();
  });
}

function posting() {
  let weather = $('#select-weather input[type="radio"]:checked').val();
  let foodtype = $('#select-foodtype input[type="radio"]:checked').val();
  let menu = $('#menu_title').val();
  let img = $('#food_img_url').val();
  let comment = $('#comment').val();

  // form의 유효성 검사
  if (!weather) {
    alert('날씨를 선택해주세요.');
    return;
  }
  if (!foodtype) {
    alert('음식 종류를 선택해주세요.');
    return;
  }
  if (!menu) {
    alert('메뉴를 입력해주세요.');
    return;
  }
  if (!img) {
    alert('이미지 URL을 입력해주세요.');
    return;
  }
  if (!comment) {
    alert('한줄평을 입력해주세요.');
    return;
  }

  let formData = new FormData();
  formData.append('weather_give', weather);
  formData.append('menu_give', menu);
  formData.append('img_give', img);
  formData.append('comment_give', comment);
  formData.append('foodtype_give', foodtype);

  fetch('/foodlist', { method: 'POST', body: formData })
    .then((res) => res.json())
    .then((data) => {
      alert(data['msg']);
      window.location.reload();
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

// ! 아래 주석처리된 함수는 html에서 날씨카테고리 클릭시 -> 페이지 이동으로 바뀌어 필요없을 것 같아 주석처리!
//* (혹시나 필요할수도 있으니 놔둘게여)
// weather 카테고리 클릭시 - foodlist 불러오기
// fetch('/foodlist/weather');
// function showByWeather(weather_value) {
//   fetch(`/foodlist/weather?weather_value=${weather_value}`)
//     .then((res) => res.json())
//     .then((data) => {
//       console.log(data);

//       let rows = data['result'];
//       console.log(rows);

//       $('.cards').empty();
//       rows.forEach((a) => {
//         console.log(a);
//         let menu = a['menu'];
//         let img = a['img'];
//         let comment = a['comment'];
//         let p_id = a['_id'];
//         let weather = a['weather'];
//         let weather_span = '';
//         let weather_i = '';
//         if (weather == 1) {
//           weather_span = 'sunny';
//           weather_i = 'sun';
//         } else if (weather == 2) {
//           weather_span = 'cloudy';
//           weather_i = 'cloud';
//         } else if (weather == 3) {
//           weather_span = 'rainy';
//           weather_i = 'umbrella';
//         } else if (weather == 4) {
//           weather_span = 'snowy';
//           weather_i = 'snowflake';
//         }

//         console.log(weather, menu, comment, img, p_id, weather_span, weather_i);

//         let temp_html = `
//                     <div class="col" id="card">
//                       <div class="card">
//                         <span class="card-weather">
//                           <i class="fa-solid fa-${weather_i}"></i>
//                         </span>
//                         <div class="card-img-wrap">
//                           <img
//                             src="${img}"
//                             class="card-img"
//                             alt="음식 대표사진" />
//                         </div>
//                         <div class="card-body">
//                           <h5 class="card-title">${menu}</h5>
//                           <span class="card-foodtype">${comment}</span>
//                           <p class="card-comment">오늘 추천하고 싶은 메뉴는 바로바로바로~~~!</p>
//                           <p class="more" id=${p_id}><i class="fa-solid fa-plus"></i>더보기</p>
//                         </div>
//                       </div>
//                     </div>
//                       `;
//         $('#cards').prepend(temp_html);
//       });
//     });
// }

// foodtype 카테고리 클릭시 - foodlist 불러오기
// * 카테고리 버튼에 weather와 foodtype_value 정보 필요!
function showByfoodtype(weather, foodtype_value) {
  // fetch('/foodlist/weather')
  fetch(`/cate-${weather}-foodtype?foodtype_value=${foodtype_value}`)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      // alert(data["msg"]);

      let rows = data['result'];
      console.log(rows);

      $('.cards').empty();
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
                    <div class="col" id="card">
                      <div class="card">
                        <span class="card-weather">
                          <i class="fa-solid fa-${weather_i}"></i>
                        </span>
                        <div class="card-img-wrap">
                          <img
                            src="${img}"
                            class="card-img"
                            alt="음식 대표사진" />
                        </div>
                        <div class="card-body">
                          <h5 class="card-title">${menu}</h5>
                          <span class="card-foodtype">${comment}</span>
                          <p class="card-comment">오늘 추천하고 싶은 메뉴는 바로바로바로~~~!</p>
                          <p class="more" id=${p_id}><i class="fa-solid fa-plus"></i>더보기</p>
                        </div>
                      </div>
                    </div>
                      `;
        $('#cards').prepend(temp_html);
      });
    });
}
