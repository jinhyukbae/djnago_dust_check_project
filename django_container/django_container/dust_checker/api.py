from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

serviceKey = "YjYXl60H6X%2BAxzXryyQ051bmAZHsi%2FwVKCPL4PW%2BeUV7s7mCIKLs2Afk3ssHJBluwXYmP%2B%2BQ5az1pGz6KLP2pQ%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8') # 공공데이터는 인코딩된 상태이므로 디코딩해줘야함

def check_air():
    station = [] # 서울
    pm10 = [] # 
    url = "https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    returnType="xml"
    numOfRows="100"
    pageNo="1"
    sidoName="서울"
    ver="1.0"

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('sidoName') : sidoName, quote_plus('ver') : ver })
    res = requests.get(url + queryParams)
    xml = res.text # 공공데이터 포털로부터 수신된 XML 저장
    soup = BeautifulSoup(xml, 'html.parser') # html parser를 사용하여 수신된 XML 파일을 파싱
    for tag in soup.find_all('stationname'): # 청계천로 광진구 등 모든 stationname tags의 값을 검색해서 station 리스트에 바인딩
        station.append(tag.text)
    for tag in soup.find_all('pm10value'): # 모든 pm10 tags의 값(12, 9, …)을 검색하여 pm10 리스트에 저장
        pm10.append(tag.text)
    res = dict(zip(station, pm10))
    return res

# qureyparams 
# https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=YjYXl60H6X%2BAxzXryyQ051bmAZHsi%2FwVKCPL4PW%2BeUV7s7mCIKLs2Afk3ssHJBluwXYmP%2B%2BQ5az1pGz6KLP2pQ%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0 르