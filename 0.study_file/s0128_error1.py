# 파일명: s0128_error1.py

a, b = 5, 0
A = [1, 3, 5, 7]
try:
    file = open('school.csv', 'r')    
    print(a / b)
    print(A[3])
except FileNotFoundError:
    print("없는 파일입니다.")
else:
    print(file.read())
finally:
    print("프로그램을 종료합니다.")