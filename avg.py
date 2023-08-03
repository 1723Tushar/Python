# a = input("Enter your Name:")
# b = input("Enter your Date of Brith:")
# c = input("Enter your Mobile No.:")

# print("Name :- "+a)
# print("DOB :- "+b)
# print("Mobile No. :- "+c)

#-----------------------------------2-----------------
# print("###########")
# print("#")
# print("#")
# print("###########")
# print("#")
# print("#")
# print("#")
# print("#")
 #-----------------------------------3---------------
# print("                   ###")
# print("                 #")
# print("               #")
# print("              #")
# print("            #")
# print("           #")
# print("          #")
# print("          #")
# print("           #")
# print("             #")
# print("               #")
# print("                 #")
# print("                   ###")


# day = int(input("Enter the days :"))
# if (day>=0):
#     year = day//365
#     print("Year:-")
#     print(year)
#     val = year*365
#     mo = day-val
#     week = mo//7
#     print("Week:-")
#     print(week)
#     da = week*7
#     mon = mo-da
#     print("Days:-")
#     print(mon) 
# else:
#     print("invalid number")


# num =  int(input("Enter the number:"))
# if (num<=20):
#     print("[0-20]")
# elif(num<=40):
#     print("[21-40]")
# elif(num<=60):
#     print("[41-60]")
# elif(num<=80):
#     print("[61-80]")
# else:
#     print("Invalid number")



# sum=0
# a = []
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = int(input())
#     a.append(ele) 
# for i in range(len(a)):
#     if(a[i] % 2):
#         sum+=a[i] # sum = sum+a[i]
# print("sum of all odd number:",sum)
 


# a = int(input("Enter the Hypotenuse line number:"))
# b = int(input("Enter the Opposite line number:"))
# c = int(input("Enter the Adjacent line number:"))
# if(a+b>c and a+c>b and b+c>a):
#     print("triangle is correct")
# else:
#     print("Invalid number")
 


# a = int(input("Enter the Hypotenuse line number:"))
# b = int(input("Enter the Opposite line number:"))
# c = int(input("Enter the Adjacent line number:"))
# if(a+b>c):
#     if(a+c>b):
#         if(b+c>a):
#             print("Triangle is correct")
# else:
#     print("Triangle is not correct")



# import math
# a = int(input("Enter the number of A: "))
# b = int(input("Enter the number of B: "))
# c = int(input("Enter the number of C: "))
# d = (b*b)-(4*a*c) 
# if (d>0):
#     x1 = (-b+(math.sqrt(d)))/(2*a)
#     print(x1)
# else:
#     print ("Invalid number")


# a = []
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     b = int(input())
#     a.append(b) 
# if()


#-----------------------------------------------------21/07/2023-----------------------------------------------------------------

# a = int(input("Enter the number 1 b/w 12:"))
# if(a==1):
#     print("January")
# elif(a==2):
#     print("February")
# elif(a==3):
#     print("March")
# elif(a==4):
#     print("April")
# elif(a==5):
#     print("May")
# elif(a==6):
#     print("June")
# elif(a==7):
#     print("July")
# elif(a==8):
#     print("August")
# elif(a==9):
#     print("September")
# elif(a==10):
#     print("October")
# elif(a==11):
#     print("November")
# elif(a==12):
#     print("December")
# else:
#     print("Invalid number")


# a = int(input("Enter the number 1 to 12:"))
# def switch(month):
#     if (month == 1):
#         print("January")
#     elif(month == 2):
#         print("February")
#     elif(month==3):
#         print("March")
#     elif(month==4):
#         print("April")
#     elif(month==5):
#         print("May")
#     elif(month==6):
#         print("June")
#     elif(month==7):
#         print("July")
#     elif(month==8):
#         print("August")
#     elif(month==9):
#         print("September")
#     elif(month==10):
#         print("October")
#     elif(month==11):
#         print("November")
#     elif(month==12):
#         print("December")
#     else:
#         print("Invalid number")
# print(switch(a))

# for i in range(1,51):
#     if(i%2==0):
#         print(i)



# a = int(input("Enter the number:"))
# for i in range(1,a):
#     if(i%2==0):
#         print("All even number:",i)
#         print("All square :",i**2)


# a = int(input("Enter the value of A:"))
# if(a%2):
#     if(a>0):
#         print("positive odd")
#     elif(a<0):
#         print("Negative odd")
# elif(a==0):
#     print("This value is zero")
# else:
#     if(a>0):
#         print("positive even")
#     elif(a<0):
#         print("Negative even")

# a = int(input("Enter the Number to divide:"))
# for i in range(1,101):
#     # print(i)
#     if(i%a==3):
#         print(i)


# n = []
# a = int(input("Enter the sone integer number:"))
# for i in range(0,a):
#     b = int(input())
#     n.append(b)
#     for j in range(0,b):
#         index = n.index(b)
# n.sort()
# print("It is the largest value:",n)
# print("It is Position of Value",index)


# n = []
# a = int(input("Enter the one pair:"))
# b = int(input("Enter the one pair:"))
# n.append(a)
# n.append(b)
# n.sort()
# print(n)
# n.reverse()
# print(n)

# a = 1682
# b = int(input("Enter the Password :"))
# if(a==b):
#     print("Password is correct")
# else:
#     print("Password Invalid ")

# import random
# b = 1682
# a = (random.randrange(1680,1690))
# print("computer choose:",a)
# if(b==a):
#     print("Passwprd is correct")
# else:
#     print("Password Invalid")

##-----------------------1------------------------
# a = (input("Enter your name:"))
# b = (input("Enter the brith day:"))
# c = (input("Enter your mobile:"))

# print("Name:",a)
# print("DOB:",b)
# print("Mobile No.:",c)

# a1 = int(input("Enter the Weight item 1 in kg:"))
# a2 = int(input("Enter the No. of item 1 :"))
# b1 = int(input("Enter the Weight item 2 in kg:"))
# b2 = int(input("Enter the No. of item 2 :"))
# a3 = a1+a2
# b3 = b1+b2
# c = a3+b3//2
# print("Weight_item 1:",a1," kg")
# print("No.of item 1:",a2)
# print("Weight_item 2:",b1," kg")
# print("No.of item 2:",b2)
# print("Average Value:",c)

# a = int(input("Enter the Divident:"))
# b = int(input("Enter the dividebale:"))
# if(a<b):
#     print("Divide:",b%a)
# else:
#     print("It is not possible")

# a = int(input("Enter the Divident:"))
# b = int(input("Enter the dividebale:"))
# if(a<b):
#     print("Divide:",b%a)
# elif(a>b):
#     c = a
#     a = b
#     b = c
#     print("Divide:",b%a)

# import math
# x1 = int(input("Enter the x1:"))
# x2 = int(input("Enter the x2:"))
# y1 = int(input("Enter the y1:"))
# y2 = int(input("Enter the y2:"))
# dis = math.sqrt(((x2-x1)*(x2-x1))+(y2-y1)*(y2-y1))
# print(dis)

# rs = int(input("Enter the Rupee :"))
# if (rs>=0):
#     # note1 = rs//2000
#     # print("2000 note:-",note1)
#     # val = note1*2000
#     # pe = rs-val
#     note2 = rs//500
#     print("500 note:-",note2)
#     da = note2*500
#     ma = rs-da
#     note3 = ma//200
#     print("200 note:-",note3)
#     tu = note3*200
#     th = ma-tu
#     note4 = th//100
#     print("100 note:-",note4)
#     ts = note4*100
#     td = th-ts
#     note5 = td//50
#     print("50 note:-",note5)
#     ten = note5*50
#     tam = td-ten
#     note6 = tam//10
#     print("10 note:-",note6)
# else:
#     print("invalid number")


#fint out 2nd higest for input number
# a = []
# n = int(input("Enter the number:"))
# for i in range(0,n):
#     b = int(input())
#     a.append(b)
# a.sort()
# print(a)
# print(a[n-2])


# s = int(input("Enter the Second:"))
# h = s//3600
# print("hours:-",h)
# val = h*3600
# pe = s-val
# m = pe//60
# print("Minutes-",m)
# da = m*60
# ma = pe-da
# print("Second:-",ma)


# x = int(input("Enter the number:"))
# y = int(input("Enter the number:"))
# # x=5
# # y=6
# if(x>0 and y>0):
#     print("(+,+)")
# elif(x>0 and y<0):
#     print("(+,-)")
# elif(x<0 and y>0):
#     print("(-,+)")
# elif(x<0 and y<0):
#     print("(-,-)")
# else:
#     print("Invalid number")


# x = int(input("Enter the number:"))
# for i in range(0,x):
#     if(i%7==2) or (i%7==3):
#         print(i)

# x = int(input("Enter the number:"))
# for i in range(0,x):
#     if(i%7==0):
#         print(i)
    
# a=0
# # x = int(input("Enter the number to start:"))
# # y = int(input("Enter the number to end:"))
# # for i in range(x,y):
# #     if(i%17!=0):
# #         print(i)

# line = int(input("Enter the numbr of line:"))
# for i in range(1,line,1):
#     print(i,i*i,i*i*i)

# sum=0
# s = int(input("Enter the student:"))
# for i in range(1,s):
#     b = int(input("Enter the Marks of student:"))
#     if(b>0):
#         sum=b+sum
#         print(sum)
#         avg = sum/(s-1)
#     else:
#         if(b==0 or b<=0):
#             break
# print(avg)





# a ='I'
# b ='IV'
# c ='V'
# d ='IX'
# e ='X'
# f ='XL'
# g ='L'
# m=5
# n=10
# o=15
# h=20
# k=25
# y=30
# x=35
# z=40
# q=45
# l = int(input("Enter the number under 50:"))
# m-=l 
# m=abs(m)
# n-=l
# n=abs(n)
# o-=l
# o=abs(o)
# h-=l
# h=abs(h)
# k-=l
# k=abs(k)
# y-=l
# y=abs(y)
# x-=l
# x=abs(x)
# z-=l
# z=abs(z)
# q-=l
# q=abs(q)
# if(l<4):
#     for i in range(0,l):
#         print(a)
# elif(l==4):
#     print(b)
# elif(l<=8):
#     for j in range(l,l+1):
#         print(c+a*m)
# elif(l==9):
#     print(d)
# elif(l==10):
#     print(e)
# elif(l<=49):
#     for j in range(l,l+1):
#         if(l<=13):
#             print(e+a*n)
#         elif(l==14):
#             print(e+b)
#         elif(l==15):
#             print(e+c)
#         elif(l<=18):
#             print(e+c+a*o)
#         elif(l==19):
#             print(e+d)
#         elif(l==20):
#             print(e+e)
#         elif(l<=23):
#             print(e+e+a*h)
#         elif(l==24):
#             print(e+e+b)
#         elif(l==25):
#             print(e+e+c)
#         elif(l<=28):
#             print(e+e+c+a*k)
#         elif(l==29):
#             print(e+e+d)
#         elif(l==30):
#             print(e+e+e)
#         elif(l<=33):
#             print(e+e+e+a*y)
#         elif(l==34):
#             print(e+e+e+b)
#         elif(l==35):
#             print(e*3+c)
#         elif(l<=38):
#             print(e*3+c+a*x)
#         elif(l==39):
#             print(e*3+d)
#         elif(l==40):
#             print(f)
#         elif(l<=43):
#             print(f+a*z)
#         elif(l==44):
#             print(f+b)
#         elif(l==45):
#             print(f+c)
#         elif(l<=48):
#             print(f+c+a*q)
#         elif(l==49):
#             print/(f+d)
# elif(l==50):
#     print(g)

# else:
#     print("Invlid number")


# import getpass
# a = []
# n = int(input("Enter the number of Voters:"))
# if(n<17):
#     for i in range(0,n):
#         b = int(input("Enter the S.No of Voters:"))
#         a.append(b)
#     r=[]
#     for j in range(0,5000):
#         p= getpass.getpass("Enter the You vote:")
#         if(p=='close'):
#             break
#         p=int(p)
#         r.append(p)
#         count = r.count(r)
#         # print(count)
#     for i in range(1,n+1):
#         count=r.count(i)
#         print(i,"candidate total vote:",count)
# else:
#     print("one machine allowled only 16 voters")



# from playsound import playsound
# playsound('ElevenLabs_2023-07-26T14_20_01.000Z_premade_Adam.mp3')
# a = int(input())
# if(a==1):
#     playsound('ElevenLabs_2023-07-26T14_35_37.000Z_premade_Adam.mp3')
#     b = int(input())
#     if(b==1):
#         playsound('ElevenLabs_2023-07-28T14_28_28.000Z_premade_Adam.mp3')
#         a = []
#         print("Enter the 12 number (every value single)")
#         for i in range(0,12):
#             b = int(input())
#             a.append(b)
#         print(a)
#         print("Thank you!!")
#     elif(b==2):
#         playsound('ElevenLabs_2023-07-26T14_39_24.000Z_premade_Adam.mp3')
#     else:
#         playsound('ElevenLabs_2023-07-26T14_44_31.000Z_premade_Adam.mp3')
# elif(a==2):
#     playsound('ElevenLabs_2023-07-26T14_39_24.000Z_premade_Adam.mp3')
# else:
#     playsound('ElevenLabs_2023-07-26T14_44_31.000Z_premade_Adam.mp3')


# a=[1,2,3,5,4]
# for i in range(0,5):
#     if(a[i]==5):
#         print("Index no::",i,"Number of list:",a[i])


# s = int(input("Enter the S value:"))
# p = int(input("Enter the R Value:"))
# t = int(input("Enter the T Value:"))
# s1 = s*p*t//100
# print(s1)

# a=[12,34,56,43,78,90]
# small = a[i]
# for i in range(1,7):
   
#     if(a[i]<small):
#         print(small,a[i])


# a ={1,2,3,4,5}
# a.union({6,7})
# print(a)

# num1 = input("Enter the value:")
# num1 = input("Enter the value:")
# num1 = input("Enter the value:")
# num1 = input("Enter the value:")
# num1 = input("Enter the value:")
# num1  = input("Enter the value:")
# num1 = input("Enter the value:")
# num1 = input("Enter the value:")
# num1 = input("Enter the value:")
# num1 = input("Enter the value:")
# num1 = input("Enter the value:")
# num1 = input("Enter the value:")

# for i in range(10):
#     print(i)
#     if i==5:
#         break
# print("Tusahr")


f = open ('first.txt','r')
data = f.read()
print(data)
f.close()