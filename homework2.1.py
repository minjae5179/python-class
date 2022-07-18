a=int(input("첫 값을 입력하시오"))
more=True;
while more:
   b=(input("연산자를 입력하시오"))
   c= int(input("두번째 값을 입력하시오"))
   if b=="+":
       print(a+c)
   elif b=="-":
       print(a-c)
   elif b=="*":
       print(a*c)
   elif b=="/":
       print(a/c)
   else:
       print("끝")
       break
