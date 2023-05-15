a=input()
answer=''
for i in range(len(a)):
    l=a.rfind(a[i])+1
    if l-i>len(answer):
        answer=a[i:l]
print(answer)