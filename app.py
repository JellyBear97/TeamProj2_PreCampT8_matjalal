# 물어보기
# https://chat.openai.com/?model=text-davinci-002-render
# https://stackoverflow.com/questions?newreg=79bb94ac255544138b19b86ae17d97e5

# 캐시 삭제하기
# window: appdata>boaming>code>cache 삭제
# mac:lebrary>application support>code>cachedData

# python -m venv venv
# source 가상환경이름/Scripts/activate 가상환경 활성화
#  가상환경 켜기
# https://liebe97.tistory.com/10
# f1누르고>interpreter
# pip install flask pymongo dnspython requests beautifulsoup4
# flask = localhost에 렌더해서 회원가입하면 아이디,비밀번호를 데이터베이스에 넣는다

# 슬랙질문방
# https://app.slack.com/client/T043597JK8V/C051UPMBKH7/thread/C051UPMBKH7-1682843802.818039
# GIT HUB
# https://hackmd.io/@oW_dDxdsRoSpl0M64Tfg2g/ByfwpNJ-K

# AWS 배포하기
# deactivate
# pip install awsebcli > eb --version > python -m pip install --upgrade pip
# cd deploy
# pip install -U botocore awscli > eb init
from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi
# certifi패키지 사용하려면 터미널에 pip install certifi 입력해줘야해.

ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:0000@cluster0.e4k4r80.mongodb.net/?retryWrites=true&w=majority ', tlsCAFile=ca)
db = client.dbsparta

# FETCH = pip install bs4
import requests
from bs4 import BeautifulSoup


@app.route('/')
def home():
   return render_template("index.html")

# @app.route('/mypage')
# def mypage():
#    return render_template("mypage.html")

# post 요청 api코드
@app.route('/test', methods=['POST'])
def test_post():
   # 사용자가 적은 정보
   url_receive = request.form['url_give']
   weather_receive = request.form['weather_give']
   comment_receive = request.form['comment_give']

   print(url_receive,weather_receive,comment_receive)

# # FETCH = pip install bs4
   headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
   # url_receive 변수 넣어주기 
   data = requests.get(url_receive,headers=headers)
   soup = BeautifulSoup(data.text, 'html.parser')

   ogtitle=soup.select_one('meta[property="og:title"]')['content']
   ogimage=soup.select_one('meta[property="og:image"]')['content']
   ogdesc=soup.select_one('meta[property="og:description"]')['content']

   print(ogtitle,ogimage,ogdesc)

# # PYMONGO에 넣기
   doc={        
               # bs4에서 크롤링한거
               'title':ogtitle,
               'image':ogimage,
               'desc':ogdesc,
               #  사용자가 인풋에 적은거 
               'weather':weather_receive,
               'comment':comment_receive
                # 별점은?
            }
   db.hotplace.insert_one(doc)

   return jsonify({'msg': '저장완료'})



# GET 요청 API 코드
@app.route('/test', methods=['GET'])
def test_get():

   # title_receive = request.args.get('title_give')
   # print(title_receive)

   # 몽고DB에서 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
   all_users = list(db.hotplace.find({},{'_id':False}))
   
   
   
   # return jsonify({'result':'success', 'msg': '이 요청은 GET!'})
   return jsonify({'result':all_users,'msg': '이 요청은 GET'})




if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)



# URL = "https://map.naver.com/v5/search/%EB%A7%9B%EC%A7%91/place/1747651230?placePath=%3Fentry%253Dpll&n_ad_group_type=10&n_query=%EB%A7%9B%EC%A7%91&c=15,0,0,0,dh"
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(URL, headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')

# title=soup.select_one("#_title > span.Fc1rA").text
# image=soup.select_one("#ibu_1").text
# address=soup.select_one("#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > div > div.O8qbU.tQY7D > div > a > span.LDgIH").text

# # 별점은?

# # title["href"]
# print()

