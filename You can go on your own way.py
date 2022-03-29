def solve(s):
    string1 = ''
    for c in s:
        if c=='S':
            string1 += 'E'
        else:
            string1 += 'S'
    return string1


t = int(input()) # t=2
for i in range(t):
    n = int(input())
    s = input()
    print('Case #' + (i+1)+': '+ solve(s))
    