# number=int(input())
# last_digit=number%10
# print("Last digit is",last_digit)
# if number%2==0:
#     print("Last digit is even")
# else:
#     print("last digit is odd")
# if number>500:
#     print("Number is greater than 500")
# else:
#     print("Number is not greater than 500")
    
# #Students marks
# marks=int(input("Enter your marks: "))
# attendance=float(input("enter your attendence percentage: "))
# if marks>=40 and attendance>=75:
#     print("Pass")
# else:
#     print("fail")

#Electricity bill
# units=float(input("Enter your units consumed: "))
# bill=0
# if 0<=units<=100:
#     bill=units*s
# elif 101<=units<=200:
#     bill=units*7
# else:
#     bill=units*10
# print("Bill: ",bill)

# age=int(input("Enter your age: "))
# if age>=18:
#     entrance_Exam=input("Passed or not passed the exam?: ")
#     if entrance_Exam=="Passed":
#         Documents=input("verified or not verified?: ")
#         if Documents=="verified":
#             print("You are eligible for admission")
#     elif entrance_Exam=="not passed":
#             print("Entrance exam not cleared")
#     else:
#         print("Documents not verified")
# else:
#     print("Too young!")

#Debugging
# 
a=2
b=3
c=a/b
print(a/b)
print(round(a/b,5))
print(f"{c:.5f}")
def hello(to):
    print("Hello",to)

name=input("Enter Your name: ")
hello(name)