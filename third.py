a=int(input("정수하나를 입력하시오."))
count=0
for i in range(2,a+1) :
    a=0
    for k in range(1,i+1):
        if i%k == 0:
            a+=1
    if a==2:
        count+=1

print(count)
