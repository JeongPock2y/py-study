# mon = 12222
# print(f'매출액 {mon:12}')


a = 'Jeong yeon wooJ'

len(a)   ##열 개수  띄어쓰기 포함
print(len(a))
print(a.count('y'))


## .find(path) command 
#print(a.find('o'))

#print(a.lower())  #소문자
#print(a.upper())  #대문자

#print(a.strip('J'))
#print(a.replace('J',input()))
print(a.split(','))
print(a.split())

b = "a:b:c:d"
b.split(':')
['a', 'b', 'c', 'd']

odd = [1, 3, 5, 7, 9]
print(odd[0] + odd[2])    # -1 은 맨끝, 즉 9

sc = [90,80,65]
p = sum(sc) / len(sc)
print(round(p,1))

##list slicing##

#doc
do = {"김연아":"피겨스케이팅", "류현진":"야구", "손흥민":"축구", "귀도":"파이썬"}
print(do['김연아'])



My = True

print(type(My),"|",bool(My))




ll = [1,2,3]
print(ll[0])
del ll[0]









