str = input()
count = ''

for s in str:
    if s.isdigit():
        count = count + s
    else:
        if count == '':
            print(s, end='')
        else:
            for i in range(0, int(count)):
                print(s, end='')
        count = ''



