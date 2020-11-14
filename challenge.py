import folium
import pandas as pd
import io
from PIL import Image
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import seaborn as sns



# # font load #
# path = 'C:/Users/W15 208/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothic.ttf'
# font_name = fm.FontProperties(fname=path, size=10).get_name()
# plt.rc('font', family='font_name')
# fm._rebuild()
# # font load #

# plt.figure(figsize=(10,5))
# # font setting #
# sns.set(font=font_name,
#         rc={"axes.unicode_minus":False},
#         style='darkgrid')
# # font setting #

df = pd.read_csv('./world_corona_201104.csv')
print(df.head())
df = df.drop(colums=['male_smoker'])
