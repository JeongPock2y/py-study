# 파일명: s1204_5.py

name = "홍길동"
min  = 1
sec  = 25
avg  = 94.3579

print("내 이름은 '" + name + "'입니다.")
print("내 이름은 '" , name , "'입니다.", sep = "")
print("내 이름은 '%s'입니다."%name)
print("내 이름은 '{}'입니다.".format(name))
print(f"내 이름은 '{name}'입니다.")

print("잠수시간은 " + str(min) + "분 " + str(sec) + "초입니다.")
print("잠수시간은 " , min , "분 " , sec , "초입니다.", sep = "")
print("잠수시간은 %d분 %d초입니다."%(min, sec))
print("잠수시간은 {}분 {}초입니다.".format(min, sec))
print(f"잠수시간은 {min}분 {sec}초입니다.")