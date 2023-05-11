from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
# certifi패키지 사용하려면 터미널에 pip install certifi 입력해줘야해.

ca = certifi.where()

client = MongoClient('mongodb+srv://sparta:test@cluster0.stsxpsg.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# 경로 지정
@app.route('/')
def home():
   return render_template('index.html')
@app.route('/login')
def login():
   return render_template('login.html')


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
    return jsonify({'msg':'이번엔 진짜 성공!'})

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
    print(weather_value)
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

    print(all_foodlist)
    for food in all_foodlist:
        food['_id'] = str(food['_id'])    ## object_id -> string으로 변환
        results.append(food)

    return jsonify({'result':results})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5001, debug=True)