import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm


df_corona = pd.read_csv('서울시 코로나19 확진자 현황.csv')

# print(df_corona)

# print(df_corona.head())
# print(df_corona.info())

df_corona.drop(columns = ['국적', '환자정보', '조치사항'], inplace=True)
print(df_corona.info())

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


ax = sns.countplot(x='확진달', data=df_corona, palette="Set2")
plt.savefig('example.png')




# series의 plot 함수를 사용한 출력 방법도 있습니다.
plt.figure(figsize=(10,5))
sns.set(font=font_name,
        rc={"axes.unicode_minus":False},
        style='darkgrid')
df_corona['확진달'].value_counts().plot(kind='bar')
plt.savefig('example2.png')


# seaborn의 countplot 함수를 사용하여 출력합니다.
plt.figure(figsize=(20,10))
ax = sns.countplot(x="확진일", data=df_corona[df_corona['확진달'] == 8], palette="rocket_r")
plt.savefig('example3.png')

plt.figure(figsize=(20,10))
ax = sns.countplot(x="지역", data=df_corona, palette="Set2")
plt.savefig('example4.png')
