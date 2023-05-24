m1 = "PLAYER I WINS"
m2 = "PLAYER II WINS"
m3 = "GAME IS A TIE"


a = '1'
b = '2'
c = '3'
d = '4'
e = '5'
f = '6'
g = '7'
h = '8'
i = '9'

k = 0
x = 'x'
flag = 1
n = 0
w = 0


def display():
    print("-------------")
    print("|", a, "|", b, "|", c, "|")
    print("-------------")
    print("|", d, "|", e, "|", f, "|")
    print("-------------")
    print("|", g, "|", h, "|", i, "|")
    print("-------------")


def avail(n):

    if n == 1:
        if a == '1':
            return 1
        else:
            return 0
    elif n == 2:
        if b == '2':
            return 1
        else:
            return 0
    elif n == 3:
        if c == '3':
            return 1
        else:
            return 0
    elif n == 4:
        if d == '4':
            return 1
        else:
            return 0
    elif n == 5:
        if e == '5':
            return 1
        else:
            return 0
    elif n == 6:
        if f == '6':
            return 1
        else:
            return 0
    elif n == 7:
        if g == '7':
            return 1
        else:
            return 0
    elif n == 8:
        if h == '8':
            return 1
        else:
            return 0
    else:
        if i == '9':
            return 1
        else:
            return 0


def insert(n):
    global a, b, c, d, e, f, g, h, i
    if n == 1:
        a = x
    elif n == 2:
        b = x
    elif n == 3:
        c = x
    elif n == 4:
        d = x
    elif n == 5:
        e = x
    elif n == 6:
        f = x
    elif n == 7:
        g = x
    elif n == 8:
        h = x
    else:
        i = x


def gover():
    if ((a == b == c == 'x') or (d == e == f == 'x') or (g == h == i == 'x')):
        return 1
    elif ((a == d == g == 'x') or (b == e == h == 'x') or (c == f == i == 'x')):
        return 1
    elif ((a == e == i == 'x') or (c == e == g == 'x')):
        return 1
    elif ((a == b == c == 'o') or (d == e == f == 'o') or (g == h == i == 'o')):
        return 2
    elif ((a == d == g == 'o') or (b == e == h == 'o') or (c == f == i == 'o')):
        return 2
    elif ((a == e == i == 'o') or (c == e == g == 'o')):
        return 2
    else:
        return 0


while (flag != 0):
    display()
    if k % 2 == 0:
        x = 'x'
    else:
        x = 'o'
    if x == 'x':
        print("PLAYER I , ENTER POSITION OF x : ")
        n = int(input())
    else:
        print("PLAYER II , ENTER POSITION OF o : ")
        n = int(input())
    w = avail(n)
    if w == 0:
        print("INVALID\n")
    else:
        insert(n)
        k += 1
    w = gover()
    if w == 1:
        display()
        print("PLAYER I WINS")
        flag = 0

    elif w == 2:
        display()
        print("PLAYER II WINS")
        flag = 0

    else:
        if k == 9:
            flag = 0
        else:
            flag = 1

if flag == 0:
    print(m3)
