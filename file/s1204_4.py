# 파일명: s1204_4.py

text = "20221124Sunny"
date = text[:8]
weather = text[8:]
print("날짜:", date)
print("날씨:", weather)
print()
rrn = "940725-1234567"
year = "19" + rrn[0:2]
month = rrn[2:4]
day = rrn[4:6]
print("생년:", year)
print("생월:", month)
print("생일:", day)