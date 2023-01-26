print("enter your first number")
number1=int(input())
print("enter your operation")
operation=str(input())
print("enter your second number")
number2=int(input())
if operation=="+":
   results= number1 + number2
   print(results)
elif operation=="-":
    results=number1 - number2
    print(results)
elif operation=="*":
    results= number1 * number2
    print (results)
elif operation=="/":
    results=number1 / number2
    print (results)
elif operation=="%":
    results=(number1/number2)*100
    print(results)
else:
    print("invalid operation type")
#result1 = number1+number2
#result2 = (number1+number2)
#print(type(result1))
#print(result2)
#print(result1,result2,end= ' ')