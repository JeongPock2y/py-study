treeHit = 0
while treeHit < 10:
     treeHit = treeHit +1
     print("나무를 %d번 찍었습니다." % treeHit)
     if treeHit == 10:
         print("나무 넘어갑니다.")




# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first +last) 

print(first + last)
