# #파일 객체 = open(파일 이름, 파일 열기 모드)

# # f = open("C:/doit/py-study/py-study/newfile.py", 'w')
# with open("C:/doit/py-study/py-study/newfile1.txt", "w") as f:
#     f.write("Life is too short, you need python")
import time

print(time.asctime(time.localtime(time.time())))
print(time.ctime())
# class MyError(Exception):
#     pass


# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)
