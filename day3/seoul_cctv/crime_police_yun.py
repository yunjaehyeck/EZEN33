import pandas as pd
import googlemaps


ctx = '../data/'
filename = 'crime_in_Seoul.csv'
# 텍스트 인코딩 타입을 지정 함.
df_crime = pd.read_csv(ctx+filename, sep=',', encoding='euc-kr')

# print(df_crime)
# 구글 맵 API 키값.
gmaps_key = 'AIzaSyDu0g9aIb-1mPMnNsLe0nzk1YpDUDZL1AE'
gmaps = googlemaps.Client(key=gmaps_key)

# print(df_crime.columns)

"""
Index(['관서명', '살인 발생', '살인 검거', '강도 발생', '강도 검거', '강간 발생', '강간 검거', '절도 발생',
       '절도 검거', '폭력 발생', '폭력 검거'],
      dtype='object')
"""
# 구글맵 으로 부터 "서울중부경찰서" 에 관한 위치 정보를 얻어 엄.
# print(gmaps.geocode('서울중부경찰서', language='ko'))

station_name = []
for name in df_crime['관서명']:
    station_name.append('서울'+str(name[:-1])+'경찰서')   # " -1 " 은 모든 데이터를 의미

station_addr = []
station_lat = []  # 위도
station_lng = []  # 경도

for name in station_name:
    tmp = gmaps.geocode(name, language='ko')
    station_addr.append(tmp[0].get('formatted_address'))  # 구글에서 정의한 이름 'forma.....'
    tmp_loc = tmp[0].get('geometry')
    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    # print(name + '------------------->'+tmp[0].get('formatted_address'))

gu_names = []
for name in station_addr:
    tmp = name.split()
    tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]  # '구라는 글자가 있는 모든 데이터를 추출 함.
    gu_names.append(tmp_gu)

print("---------------------------------  1  -------------------------------------")
print(len(df_crime['관서명']))

df_crime['구별'] = gu_names
print("---------------------------------  2  -------------------------------------")
print(df_crime['관서명'])

# 금천경찰서는 관악구에 있어서 금천서를 찾아서 관악구라고 수작업으로 변경 해야 함.
df_crime.loc[df_crime['관서명'] == '금천서', ['구별']] == '금천구'
print("---------------------------------  3  -------------------------------------")
print(df_crime)

# CCTV 숫자가 경찰서가 동일하게 있다고(능력) 가정했을 때, 범죄 검거율과 어떤 관계가 있는지 분석
# 추출한 결과를 파일로 저장하여 crime_rate에 활용
df_crime.to_csv(ctx+'crime_police.csv')