#pip install SomePackage 
#SomePackage는 내려받을 수 있는 특정 패키지


#pip install Faker
#faker는 테스트용 가짜 데이터를 생성할 때 사용하는 라이브러리

# from faker import Faker
# fake = Faker()
# fake.name()
# # 'Matthew Estrada'
# >>> fake = Faker('ko-KR')
# >>> fake.name()
# '김하은'

# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다.
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

result = 0
for n in range(1,10):
    if n % 3 == 0 or n % 5 ==0:
        result += n
        
print(result)
