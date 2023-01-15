# list= [100,20,30,40,50]
# def sum(list_data):
#     sum =0 
#     for i in list_data:
#         sum += i
#     return sum
    

# def len(list_data):
#     cnt = 0 
#     for i in list_data:
#         cnt += i
#     return cnt
    
# list= [100,20,30,40,50]
# avg = sum(list)/len(list)
# print(f'{avg}')

#--------

# def compute_sum(end):
#     sum =0
#     for sum in range(1,end+1):
#         i += sum
#     return sum

# end = int(input("dd?"))
# sum = compute_sum(end)
# print(f"d:{sum}")

student1 = [10,20,20,20,20,20]
student2 = [10,20,20,20,20,20]
student3 = [20,20,20,20,20,20]
std_list= [student1,student2,student3]

for std in std_list:
    sum = 0 
    for score in std:
        sum += score
    avg = sum / len(std)
    print(f"{avg}점")




