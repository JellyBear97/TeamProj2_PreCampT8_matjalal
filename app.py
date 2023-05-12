from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
# certifi패키지 사용하려면 터미널에 pip install certifi 입력해줘야해.

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.stsxpsg.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# 경로 지정
# main page
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/main')
def main():
   return render_template('index.html')

# login page
@app.route('/login')
def login():
   return render_template('login.html')

# category sunny page
@app.route('/cate-sunny')
def cateSunny():
   return render_template('sunny.html')

# category cloudy page
@app.route('/cate-cloudy')
def cateCloudy():
   return render_template('cloudy.html')

# category rainy page
@app.route('/cate-rainy')
def cateRainy():
   return render_template('rainy.html')

# category snowy page
@app.route('/cate-snowy')
def cateSnowy():
   return render_template('snowy.html')

# pymongo에 db 저장하기  
@app.route("/foodlist", methods=["POST"])
def foodlist_post():
    weather_receive = request.form["weather_give"]
    foodtype_receive = request.form["foodtype_give"]
    menu_receive = request.form["menu_give"]
    img_receive = request.form["img_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'weather': weather_receive,
        'foodtype' : foodtype_receive,
        'menu': menu_receive,
        'img': img_receive,
        'comment': comment_receive
    }

    db.foodlist.insert_one(doc)
    return jsonify({'msg':'게시물 등록완료 💖!'})

# category sunny foodlist -all 보내주기 부분
@app.route('/cate-sunny-all', methods=["GET"])
def cateSunnyAll_get():
    results = []

    all_foodlist = list(db.foodlist.find({'weather' : '1'}))

    print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})

# category cloudy foodlist -all 보내주기 부분
@app.route('/cate-cloudy-all', methods=["GET"])
def catecloudyAll_get():
    results = []

    all_foodlist = list(db.foodlist.find({'weather' : '2'}))

    print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})

# category rainy foodlist -all 보내주기 부분
@app.route('/cate-rainy-all', methods=["GET"])
def caterainyAll_get():
    results = []

    all_foodlist = list(db.foodlist.find({'weather' : '3'}))

    print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})

# category snowy foodlist -all 보내주기 부분
@app.route('/cate-snowy-all', methods=["GET"])
def catesnowyAll_get():
    results = []

    all_foodlist = list(db.foodlist.find({'weather' : '4'}))

    print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})


# category sunny foodlist - foodtype 별 보내주기 부분
@app.route('/cate-sunny-foodtype', methods=["GET"])
def cateSunny_get():
    # 🖌1얘랑
    foodtype_value = request.args.get('foodtype_value')
    # print(weather_value)
    results = []
    # 🖌2얘 피드백..받음
    all_foodlist = []
    if (foodtype_value == 'all_type'):
        all_foodlist = list(db.foodlist.find({'weather' : '1'}))
    elif (foodtype_value == 'korean'):
        all_foodlist = list(db.foodlist.find({'weather' : '1', 'foodtype': '2'}))
    elif (foodtype_value == 'western'):
        all_foodlist = list(db.foodlist.find({'weather' : '1', 'foodtype': '3'}))
    elif (foodtype_value == 'china'):
        all_foodlist = list(db.foodlist.find({'weather' : '1', 'foodtype': '4'}))
    elif (foodtype_value == 'japan'):
        all_foodlist = list(db.foodlist.find({'weather' : '1', 'foodtype': '5'}))
    elif (foodtype_value == 'esc_type'):
        all_foodlist = list(db.foodlist.find({'weather' : '1', 'foodtype': '6'}))

    # print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})


# category cloudy foodlist - foodtype 별 보내주기 부분
@app.route('/cate-cloudy-foodtype', methods=["GET"])
def cateCloudy_get():
    # 🖌1얘랑
    foodtype_value = request.args.get('foodtype_value')
    # print(weather_value)
    results = []
    # 🖌2얘 피드백..받음
    all_foodlist = []
    if (foodtype_value == 'all_type'):
        all_foodlist = list(db.foodlist.find({'weather' : '2'}))
    elif (foodtype_value == 'korean'):
        all_foodlist = list(db.foodlist.find({'weather' : '2', 'foodtype': '2'}))
    elif (foodtype_value == 'western'):
        all_foodlist = list(db.foodlist.find({'weather' : '2', 'foodtype': '3'}))
    elif (foodtype_value == 'china'):
        all_foodlist = list(db.foodlist.find({'weather' : '2', 'foodtype': '4'}))
    elif (foodtype_value == 'japan'):
        all_foodlist = list(db.foodlist.find({'weather' : '2', 'foodtype': '5'}))
    elif (foodtype_value == 'esc_type'):
        all_foodlist = list(db.foodlist.find({'weather' : '2', 'foodtype': '6'}))

    # print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})

# category rainy foodlist - foodtype 별 보내주기 부분
@app.route('/cate-rainy-foodtype', methods=["GET"])
def cateRainy_get():
    # 🖌1얘랑
    foodtype_value = request.args.get('foodtype_value')
    # print(weather_value)
    results = []
    # 🖌2얘 피드백..받음
    all_foodlist = []
    if (foodtype_value == 'all_type'):
        all_foodlist = list(db.foodlist.find({'weather' : '3'}))
    elif (foodtype_value == 'korean'):
        all_foodlist = list(db.foodlist.find({'weather' : '3', 'foodtype': '2'}))
    elif (foodtype_value == 'western'):
        all_foodlist = list(db.foodlist.find({'weather' : '3', 'foodtype': '3'}))
    elif (foodtype_value == 'china'):
        all_foodlist = list(db.foodlist.find({'weather' : '3', 'foodtype': '4'}))
    elif (foodtype_value == 'japan'):
        all_foodlist = list(db.foodlist.find({'weather' : '3', 'foodtype': '5'}))
    elif (foodtype_value == 'esc_type'):
        all_foodlist = list(db.foodlist.find({'weather' : '3', 'foodtype': '6'}))

    # print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})


# category snowy foodlist - foodtype 별 보내주기 부분
@app.route('/cate-snowy-foodtype', methods=["GET"])
def cateSnowy_get():
    # 🖌1얘랑
    foodtype_value = request.args.get('foodtype_value')
    # print(weather_value)
    results = []
    # 🖌2얘 피드백..받음
    all_foodlist = []
    if (foodtype_value == 'all_type'):
        all_foodlist = list(db.foodlist.find({'weather' : '4'}))
    elif (foodtype_value == 'korean'):
        all_foodlist = list(db.foodlist.find({'weather' : '4', 'foodtype': '2'}))
    elif (foodtype_value == 'western'):
        all_foodlist = list(db.foodlist.find({'weather' : '4', 'foodtype': '3'}))
    elif (foodtype_value == 'china'):
        all_foodlist = list(db.foodlist.find({'weather' : '4', 'foodtype': '4'}))
    elif (foodtype_value == 'japan'):
        all_foodlist = list(db.foodlist.find({'weather' : '4', 'foodtype': '5'}))
    elif (foodtype_value == 'esc_type'):
        all_foodlist = list(db.foodlist.find({'weather' : '4', 'foodtype': '6'}))

    # print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})







# 카테고리 상관없이 모든 foodlist 보내주기부분
@app.route("/foodlist", methods=["GET"])
def foodlist_get():
    results = []
    all_foodlist = list(db.foodlist.find({}))
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})


# weather 카테고리 클릭시 foodlist 보내주기부분
@app.route("/foodlist/weather", methods=["GET"])
def foodlistByweather_get():
    # 🖌1얘랑
    weather_value = request.args.get('weather_value')
    # print(weather_value)
    results = []
    # 🖌2얘 피드백..받음
    all_foodlist = []
    if (weather_value == 'sunny'):
        all_foodlist = list(db.foodlist.find({'weather' : '1'}))
    elif (weather_value == 'cloudy'):
        all_foodlist = list(db.foodlist.find({'weather' : '2'}))
    elif (weather_value == 'rainy'):
        all_foodlist = list(db.foodlist.find({'weather' : '3'}))
    elif (weather_value == 'snowy'):
        all_foodlist = list(db.foodlist.find({'weather' : '4'}))

    # print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})




if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)