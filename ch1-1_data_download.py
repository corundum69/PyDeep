# 웹상에서 정보를 추출하는 방법 
## urllib.request를 이용한 다운로드 (download-png1.py)
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url, savename)
print("저장되었습니다")

## urlopen()으로 파일에 저장하는 방법 (download-png2.py)
import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

mem = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(mem)
    print("저장되었습니다")

# 웹에서 데이터 추출하기
## 클라이언트 접속 정보 출력해 보기 (download-ip.py)
import urllib.request

url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)

## 매개변수를 추가해 요청을 전송하는 방법 (download-forecast.py)
import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId' : '108'
}

params = urllib.parse.urlencode(values)

url = API + "?" + params
print("url=", url)

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)

## 매개변수를 명령줄에서 지정하기 (download-forecast-argv.py)
import sys  # 명령줄 매개변수를 추출할 때 사용하는 모듈
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:  # 명령줄에 몇 개의 매개변수가 지정돼 있는지 len(sys.argv)로 확인한다
    print("USAGE: download-forecast-argv <Region Number")
    sys.exit()   # 파이썬 프로그램을 중단할 때 사용
regionNumber = sys.argv[1]  # sys.argv[1] 이후에 명령줄 매개변수 설정된다

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : regionNumber
}
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)

