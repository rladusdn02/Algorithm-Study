for _ in range(int(input())):
    ox_list = list(input())
    ans = 0
    sc = 0
    for ox in ox_list:
        if ox == 'O':
            sc += 1
            ans += sc
        elif ox == "X":
            sc = 0
    print(ans)
                   