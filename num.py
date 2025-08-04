# list1=[11,22,33,44,55,22,33,33,44,55,55,55,44,55,33]
# unique_list=list(set(list1))
# for each_element in unique_list:
#     counting=list1.count(each_element)
#     print(each_element,"----->",counting)

# tuple1=([1,2,3,4,5],{"key":"value"})
# tuple1[0].append(7)
# print(tuple1)

# my_tuple = ([1, 2, 3],{"key": "value"})
# my_tuple[0].append(4)  # Modifies the list inside the tuple
# print(my_tuple)  # Output: ([1, 2, 3, 4], {'key': 'value'})

# l1 = [3,4,5,7,3,6,7,9,67]
# indexing = l1.index(67,4)
# print (indexing)

num = int(input("enter a number "))
count=0
divisors=[]
prime=True
if num >0:
    if num in [1,2]:
        print(f"given number {num} is prime ")
    else:
        for i in range(2,int(num*0.5)+1):
            if num%i==0:
                count +=1
                divisors.append(i)
                prime = False
        else:
            if prime == False:
                print(f"given number {num} is composite number  ")
                print(f"count of given number {num} is ---> {count}")
                print(divisors)
            else:
                print(f"given number {num} is prime ")
else:
    print("enter a valid number ")