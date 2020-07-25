import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

for page in range(1,5):
    params = {'pg':page}
    data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', params= params, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    # body-content > div.newest-list > div > table > tbody > tr:nth-child(19) > td.info > a.title.ellipsis

    for song in songs:
        rank = song.select_one('td.number').contents[0].strip()
        title = song.select_one("td.info > a.title.ellipsis").text.strip()
        artist = song.select_one('td.info > a.artist.ellipsis').text.strip()
        print(rank, title, artist)


