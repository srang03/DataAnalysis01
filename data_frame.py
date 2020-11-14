import pandas as pd

# 데이터프레임도 변수로 저장이 가능

student_data = [['홍길동', 80, 70, 80],
                   ['박철수', 60, 70, 80],
                   ['김영희', 70, 90, 80]]
df = pd.DataFrame(student_data, columns=['이름', '국어', '수학', '영어'])



df = df.set_index('이름')
print(df)

df = df.set_index('국어')

print(df)