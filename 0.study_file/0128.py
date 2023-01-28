#filter func
A = [3,4,5,2,7,6,9]
B= []
def even(item):
    return item % 2 ==0        
filter(even,A)
B = list(filter(even,A))
print(B)

