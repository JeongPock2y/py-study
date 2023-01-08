# for i in range(10):
#     if i % 2 ==0:
#         continue
#     print(i)
# #===========================

# a = list(range(10))
# print(a)
#
#=============================

# sum =0
# number = int(input("숫자를 입력하세요: "))
# for i in range(1,number+1):
#     sum += i 
# print(sum)



fri = [0,1,2,3,4]
name= ["민","철","개","똥","철"]

for f,n in zip(fri,name):
    print(f,n)

print(list(enumerate(name,0)))
print(list(enumerate(name)))
    # enumerate  함수


for num,name in enumerate(name,1):
    print(f'num = {num},{name}')


for i in range(10):
    print(i, end= '-')


#C = ['Pass'if a >= 60 else 'Fail' for a in A]




