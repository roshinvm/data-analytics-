# x=int (input('enter a number'))
# y=int(input('enter a number'))
# print(x/y)
# x=1,2,3,4
# z=5+3j
# print(type(x))
# print(type(z))
# x,y=y,x
# print(x,y)
# z=int(input('enter a number'))
# for i in range(1,11,1):
#     print(z,'x',i,"=",z*i)
#     print(f"{z}x{i}={z*i}")
# a=int(input('enter a number'))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(-10,0,1):
#     print(i)
# b=int(input('enter a number'))
# # rows=b
# # for i in range(1,b+1):
# #    print(" "*(rows-i)+ "* " * i)
# c=int(input('enter a number'))
# i=1
# while (i<11):
#     print(c*i)
#     i=i+1
# s=int(input('enter a number'))
# a=1
# while a<=11:
#     if a==5:
#         a+=1
#         break
#     print(s*a)
#     a=a+1
# x=int(input('enter a number'))
# a=1
# while a<=11:
#     m=5*a
#     if a==5:
#         print('x is a multiple of 5')
#     else:
#         print('x is not a multiple of 5')
#     a=a+1
# a=int(input('enter a number'))
# if a%2==0:
#     print('multiple of 2')
# else:
#     print('it is not a multiple of 2')
# a=int(input('enter a number'))
# if a%2==0 and a%3==0:
#     print('divisibility of 2 and 3')
# else:
#     print('not divisible of 2 and 3')
# x=('atheeva')
# rev=""
# for i in x:
#     rev=i+rev
# print(rev)
# print("hello".upper())
# print("HELLO".lower())
# print("python language".title())
# print("atheeva".count("v"))
# print("atheeva".startswith("at"))
# print("atheeva".endswith("bc"))
# print("atheeva".replace("a","A"))
# print(" atheeva ".strip())
# print("a,n,d".split(","))
# a=[1,2,3]
# print(a[1])
# print(len(a))
# print(a[0:2])
# print(a.append(4))
# print(a.pop())
# print(a.pop(1))
# b=[1,2,3]
# (b.remove(2))
# print(b)
# print(a.index(1))
# print(a.count(1))
# print(2 in a)
# a=int(input('enter the length of a list'))
# l=[]
# for i in range(a):
#     b=int(input('enter the numbers'))
#     l.append(b)
# print(l)
# for i in range(0,a,1):
#     for j in range(0,a-i-1,1):
#         if(l[j]>l[j+1]):
#             temp=l[j]
#             l[j]=l[j+1]
#             l[j+1]=temp
# print(l)
# a=[1,2,3,4]
# print(list("abc"))
# print(a*2)
# a=input('enter the length of a string')
# v=0
# c=0
# for i in a:
#     if i.isalpha()==True:
#         if i in'aeiou':
#             v=v+1
#         else:
#             c=c+1
#print(f"vowels:{v},conconent:{c}")
# numbers=frozenset([1,2,3,4])
# print(numbers)
# s={1,2,3}
# print(s)
# print(len(s))
# print(type(s))
# s.add(4)
# print(s)
# s.update([5,6])
# print(s)
# s.remove(2)
# print(s)
# s.discard(2)
# print(s)
# s.pop()
# print(s)
# s.clear()
# print(s)
# a={1,2,3,4}
# b={2,4,6,8}
# print(a|b)
# print(a&b)
# print(a-b)
# print(a^b)
# print(a.issubset(b))
# print(a.issuperset(b))
# print(b.issuperset(a))
# b=a.copy()
# print(b)
# print(sorted(b))
# print(max(a))
# print(min(b))
# d={"name":"Atheeva","age":19}
# print(d["name"])
# print(d["age"])
# d={"a":1,"b":2}
# print(d)
# print(d["a"])
# d["c"]=3
# print(d)
# print(d.update({"b":5}))
# print(d.setdefault("d",4))
# print(d.pop("a"))
# print(d.popitem())
# print(d.clear())
# print(d.keys())
# print(d.values())
# print(d.items())
# a=dict([(1,'a')])
# print(a)
# print("a" in d)
# print("x not in d")
# for k in d:
#     print(k)
# for v in d.values():
#     print(k)
# for k,v in d.items():
#     print(k)
# x=('apple',[1,2,3,4,5],2.5,7,{'a':25,'b':74})
# x=['name','age','qualification']
# y=['atheeva',19,'b-tech']
# d={}
# for i in range (len(x)):
        
#         d={i,j}
#         print(d) 
# d={}
# x='apple'
# for i in x:
#     d.update()
# x=10
# result="Even" if x%2==0 else "Odd"
# print(result)
# a=5
# b=8
# maximum = a if a>b  else b
# print(maximum)
# c=["hai" if i%2==0 else i for i in range(10)]
# print(c)
# d = 5
# e = 8
# f = 3
# max = d if (d > e and d > f) else (e if e > f else f)
# print(max)
# python_students={"Arun","Megha","Rahul","Sneha"}
# analytics_students={"Sneha","Rahul","Aman","Diya"}
# print(python_students&analytics_students)
# print(python_students-analytics_students)
# print(analytics_students-python_students)
# print(python_students|analytics_students)
# print(python_students^analytics_students)
# customer1 = {"Samsung", "Apple", "OnePlus", "Realme"} 
# customer2 = {"Apple", "Vivo", "Oppo", "Samsung"}
# print(customer1&customer2)
# print(customer1|customer2)
# print(customer1-customer2)
# print(customer1^customer2)
# design_team = {"Figma", "Photoshop", "Canva", "Illustrator"} 
# marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"} 
# print(design_team&marketing_team)
# print(design_team-marketing_team)
# print(design_team|marketing_team)
# print(design_team^marketing_team)
# cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"} 
# football_fans = {"Nisha", "Rahul", "Ajay", "David"}
# print(cricket_fans&football_fans)
# print(cricket_fans-football_fans)
# print(football_fans-cricket_fans)
# print(cricket_fans|football_fans)
# electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"} 
# accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"} 
# print(electronics&accessories)
# print(electronics-accessories)
# print(electronics|accessories)
# print(electronics^accessories)
# employee1 = {"Python", "Java", "SQL", "C"} 
# employee2 = {"Python", "JavaScript", "SQL", "Go"} 
# print(employee1&employee2)
# print(employee1-employee2)
# print(employee1|employee2)
# print(employee1^employee2)
# friend1 = {"Netflix", "Prime", "Hotstar", "SonyLiv"} 
# friend2 = {"Netflix", "Zee5", "Prime", "JioCinema"}
# print(friend1&friend2)
# print(friend1-friend2)
# print(friend1|friend2)
# print(friend1^friend2)
# basic_salary=35000
# bonus=5000
# tax=2000
# total_salary=(basic_salary+bonus)
# print(total_salary)
# final_salary=(total_salary-tax)
# print(final_salary)
# yearlysalary=(12*final_salary)
# print(yearlysalary)
# yearly=(yearlysalary//12)
# print(yearly)
# mobile_price=45000
# discount=5000
# gst=2000
# discountedprice=(mobile_price-discount)
# print(discountedprice)
# gstprice=(discountedprice+gst)
# hfa=(gstprice/2)
# print(gstprice)
# print(hfa)
# rem=(gst%3)
# print(rem)
pymarks=85
sqlmarks=78
pbimarks=90
total=(pymarks+sqlmarks+pbimarks)
print(total)
avg=(pymarks+sqlmarks+pbimarks/3)
print(avg)
print("pymarks>sqlmarks",pymarks>sqlmarks)