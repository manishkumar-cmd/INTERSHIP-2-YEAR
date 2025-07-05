#name = "Gfted"
# last = "kuMAR"
# print("len of string :-",len(name))
# print("type of string :-",type(name))
# print("upper case:-",name.upper()) #capital all
# print("lowwer case:-",last.lower()) #lower all
# print("tittle:-",name.title())    #capitals 1st element 
# print("capitalize string:-",name.capitalize()) # same as the tittle
# print("swap case:-",name.swapcase()) #convert in upper case
# print(last.swapcase())
#print("count of a :-",name.count('a'))

# #print("my company name is ",name)

# first = "manish"
# last = "jangir"
# print(f"my fist name {first} and \nmy last name is {last}" )
# print(first+" "+last)
# #print(name-last)
# #print(name*last)
# #print(name/last)



#>>>>>>>>>>>>>>>>>>>>>>>>>>> #LIST >>>>>>>>>


# lst = [1,2,3,4,5,5,5,6]

# print("len of list:-",len(lst))
# print("type of list:-",type(lst))
# # indexing
# print(lst[0])
# print(lst[3])

# name = "manish"

# print(type(name))

# print(lst[1:3])

# lst.append(7)
# print(lst)
# # lst.pop()
# print(lst)
# lst.pop(5)
# print(lst)

# lst.insert(2,99)
# print(lst)

# lst.remove(2)
# print(lst)
# lst.clear()
# print(lst )
# lst.reverse()
# print(lst)

# lst.sort()
# print(lst)

#deep copy
# copy

# >>>>>>>>>> tuple >>>>>>>>

# tpl = (1,2,3,4,"mania",2.25)
# print("type of tuple:-",type(tpl))
# print("len of tuple:-",len(tpl))

#indexing
 
# print(tpl[0]) 
# print(tpl[3])

# #slicing

# print(tpl[1:3])    # 1 is starting point and end on 3
# print(tpl[::-1])    # this will reverse th tuple

# print(2 in tpl)     # this shows true and false only 
# print(99 in tpl)

# tpl1 = (1,2,3,4,5,6,7,8,9,99)

# print(max(tpl1))
# print(min(tpl1))
# print(sum(tpl1))

# a = 1,2,3,5,6,7,4,4,6
#print(type(a))
#print(a)
#print(len(a))
  
# a=int(input("emter u r no.1"))
# b=int(input("emter u r no.2"))  
# print(type(a))
# print(type(b))

# print(a*b)


# abc =1,2,3
# a ,b, c=abc
# print(a)
# print(b)
# print(c)


# tpl1=(1,2,3,4,5)
# tpl2=(1,2,3,4,5)
# print(tpl1+tpl2)
# print(tpl1*tpl2)
# print(tpl*3)
#                  <<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>

# tpl1 = (1,2,3,5,8,8,[1,2,7,8])   # need to access 7,8 in tuple 
# print(tpl1[6][2])
# print(tpl1[6][3]) 


# >>>>>>>>>>>>>>>>>>dictonary<<<<<<<<<<<<<<<<

# dct = {"name": "manish","age":21,"no.":12345}
# dct.update({"age":99,"city":"AYODHYA"})
# print(dct)

# print(dct)
# print("type of dict",type(dct))

# # print(dct["name"])
# # print(dct['age'])

# print(dct.get("name"))/

# dct['address']="sikar"
# print(dct)

# task 3 dict value updation 

# dct['age'] = 22
# print(dct)

# del dct ['no.']
# print(dct)



# print(dct.keys())
# print(dct.values())
# print(dct.items())

# print("name" in dct)
# print("hello" in dct)

# dct1 ={}
# print(dct1)
# print(type(dct1))




#>>>>>>>>>>>>>>>>>  set   <<<<<<<<<<<<

# s={20,'ram',2.24}
# print(s)

# print(type(s))
# s.add(22)
# print(s)

# s.remove(20)
# print(s)

# s.discard(99)
# print(s)

# mylist = [1,2,3,4,5]
# print(type(mylist))
# print(mylist)
# mys=(mylist)
# print(type(mys))
# print(mys)
 
#>>>>>>>>>>>>>>>copy<<<<<<<<<<

# import copy 
# list1 = [[1,2],[3,4]]
# list2 = copy.copy(list1)

# list2[1][1] = 88
# print(list1)
# print(list2)


#>>>>>>>>>>>>deep copy<<<<<<<<<<<<<<<

# import copy 
# list1 = [[1,2],[3,4]]
# list2 = copy.deepcopy(list1)
# """list3 = [1,2]"""
# list2[1][1] = 77
# print(list1)
# print(list2)


#>>>>>>>>>>>>>>>>>>>>>>>operators<<<<<<<<<<<<<<
# # 1. Arithmetic Operators
# a = 10
# b = 3

# print("Arithmetic Operators:")
# print("a + b =", a + b)    # 13
# print("a - b =", a - b)    # 7
# print("a * b =", a * b)    # 30
# print("a / b =", a / b)    # 3.333...
# print("a % b =", a % b)    # 1
# print("a // b =", a // b)  # 3
# print("a ** b =", a ** b)  # 1000
# print()

# # 2. Comparison Operators
# print("Comparison Operators:")
# print("a == b:", a == b)   # False
# print("a != b:", a != b)   # True
# print("a > b:", a > b)     # True
# print("a < b:", a < b)     # False
# print("a >= b:", a >= b)   # True
# print("a <= b:", a <= b)   # False
# print()

# # 3. Logical Operators
# x = True
# y = False

# print("Logical Operators:")
# print("x and y:", x and y)  # False
# print("x or y:", x or y)    # True
# print("not x:", not x)      # False
# print()

# # 4. Assignment Operators
# print("Assignment Operators:")
# c = 5
# print("c =", c)
# c += 2
# print("c += 2 ->", c)
# c *= 3
# print("c *= 3 ->", c)
# c -= 4
# print("c -= 4 ->", c)
# c //= 2
# print("c //= 2 ->", c)
# c **= 2
# print("c **= 2 ->", c)
# print()

# # 5. Bitwise Operators
# print("Bitwise Operators:")
# p = 5       # 0101
# q = 3       # 0011
# print("p & q =", p & q)     # 0001 -> 1
# print("p | q =", p | q)     # 0111 -> 7
# print("p ^ q =", p ^ q)     # 0110 -> 6
# print("~p =", ~p)           # -(p+1) -> -6
# print("p << 1 =", p << 1)   # 1010 -> 10
# print("p >> 1 =", p >> 1)   # 0010 -> 2
# print()

# # 6. Membership Operators
# print("Membership Operators:")
# list1 = [1, 2, 3, 4]
# print("2 in list1:", 2 in list1)        # True
# print("5 not in list1:", 5 not in list1)  # True
# print()

# # 7. Identity Operators
# print("Identity Operators:")
# m = [1, 2, 3]
# n = m
# o = [1, 2, 3]
# print("m is n:", m is n)         # True
# print("m is o:", m is o)         # False
# print("m == o:", m == o)         # True (values are equal)
# print("m is not o:", m is not o) # True






