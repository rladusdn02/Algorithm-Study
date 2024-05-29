case=int(input())
for i in range(case):
    num, s=input().split()
    #num과 문자열을 공백을 기준으로 나눠서 입력받는다(split)
    text=''
    for i in s:
        text+=int(num)*i
    print(text)
