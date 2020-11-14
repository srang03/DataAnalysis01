# 지도 출력을 위한 라이브러리 folium을 import 합니다.
import folium
import pandas as pd
import io
from PIL import Image
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import seaborn as sns

# font load #
path = 'C:/Users/W15 208/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothic.ttf'
font_name = fm.FontProperties(fname=path, size=10).get_name()
plt.rc('font', family='font_name')
fm._rebuild()
# font load #

plt.figure(figsize=(10,5))
# font setting #
sns.set(font=font_name,
        rc={"axes.unicode_minus":False},
        style='darkgrid')
# font setting #

# Map 함수를 사용하여 지도를 출력합니다.
map_osm = folium.Map(location=[37.529622, 126.984307], zoom_start=11)

CRS = pd.read_csv('서울시 행정구역 시군구 정보.csv')
print(CRS)

df_corona = pd.read_csv('서울시 코로나19 확진자 현황.csv')

# print(df_corona)

# print(df_corona.head())
# print(df_corona.info())

df_corona.drop(columns = ['국적', '환자정보', '조치사항'], inplace=True)

corona_seoul = df_corona.drop(df_corona[df_corona['지역'] == '타시도'].index)
corona_seoul = corona_seoul.drop(corona_seoul[corona_seoul['지역'] == '기타'].index)

# 서울 가운데 좌표를 잡아 지도를 출력합니다.
map_osm = folium.Map(location=[37.529622, 126.984307],
                     zoom_start=12)

# 지역 정보를 set 함수를 사용하여 25개 고유의 지역을 뽑아냅니다.
for region in set(corona_seoul['지역']):

    # 해당 지역의 데이터 개수를 count에 저장합니다.
    count = len(corona_seoul[corona_seoul['지역'] == region])
    print(region , " : ", count)
    # 해당 지역의 데이터를 CRS에서 뽑아냅니다.
    CRS_region = CRS[CRS['시군구명_한글'] == region]
    lat = float(CRS_region['위도'])
    lng = float(CRS_region['경도'])

    # # CircleMarker를 사용하여 지역마다 원형마커를 생성합니다.
    folium.CircleMarker(location=[lat, lng], # 위치
                        radius=count/5 + 10,
                        fill=True,
                        fill_color='#3186cc').add_to(map_osm)

map_osm.save('map1.html')
