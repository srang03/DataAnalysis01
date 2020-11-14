# 여행력
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

print(df_corona['여행력'])

# isnull 함수를 사용하여 여행력이 없는 사람들의 수를 계산합니다.
sum_travel_no = sum(df_corona['여행력'].isnull())
print("여행력이 없는 사람의 수: {}".format(sum_travel_no))

# 전체 샘플 수를 구합니다.
sum_travel_all = len(df_corona['여행력'])
print("전체 확진자 수: {}".format(sum_travel_all))

# 여행력이 있는 사람들의 수를 계산합니다.
sum_travel_yes = sum_travel_all - sum_travel_no
print("여행력이 있는 사람의 수: {}".format(sum_travel_yes))

# matplotlib의 bar 함수를 사용하여 막대 그래프를 출력합니다.

# x축, y축 명칭을 설정합니다.
plt.ylabel('확진자 수')
plt.xlabel('여행력 여부')

# 그래프 x축에 해당되는 데이터와 y축에 해당되는 데이터를 list 형태로 입력합니다.
plt.bar(['있다', '없다'], [sum_travel_yes, sum_travel_no])
plt.savefig('example5.png')


# 여행지 분포 출력
set(df_corona['여행력'])
