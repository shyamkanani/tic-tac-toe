def gb():
    a = '----'.join("    ")
    b = '    '.join("||||")
    print(a)
    print(b)
    print(a)
    print(b)
    print(a)
    print(b)
    print(a)

def losewin(l1):
    for i in range(len(l1)):
        if l1[0][i] == l1[1][i] and l1[0][i]== l1[2][i]:
            if l1[0][i] == " x ":
                return("1")
            elif l1[0][i] == " o ":
                return("2")

    for i in range(len(l1)):
        if l1[i][0] == l1[i][1] and l1[i][0]== l1[i][2]:
            if l1[i][0] == " x ":
                return("1")
            elif l1[i][0] == " o ":
                return("2")

    if l1[0][0] == l1[1][1] and l1[0][0]== l1[2][2]:
        if l1[0][0] == " x ":
            return("1")
        elif l1[0][0] == " o ":
            return("2")

    if l1[0][2] == l1[2][0] and l1[0][2]== l1[1][1]:
        if l1[0][2] == " x ":
            return("1")
        elif l1[0][2] == " o ":
            return("2")

def moves(p1,p2):
    flag = 0
    l = [['___','___','___'],
         ['___','___','___'],
         ['___','___','___']]
    while True:
        a = input("P1 enter your row,coln")
        a = a.split(",")
        if (l[int(a[0])][int(a[1])] == '___'):
            l[int(a[0])][int(a[1])] = " x "
        else:
            print("you have entered  wrong position")
            a = input("P1 enter your row,coln")
            a = a.split(",")
            if (l[int(a[0])][int(a[1])] == '___'):
                l[int(a[0])][int(a[1])] = " x "
        for i in range(len(l)):
            print("|",end='')
            for j in range(len(l[i])):
                print(l[i][j],end='')
                print("|",end='')
            print("\n")
        d = losewin(l)
        if d=="1":
            print("Congratulations {} You won the game".format(p1))
            break
        elif d=="2":
            print("Congratulations {} You won the game".format(p2))
            break
        flag+=1
        if flag==9:
            print("It's a draw...")
            break

        b = input("P2 enter your row,coln")
        b = b.split(",")
        if (l[int(b[0])][int(b[1])] == '___'):
            l[int(b[0])][int(b[1])] = " o "
        else:
            print("you have entered  wrong position")
            b = input("P2 enter your row,coln")
            b = b.split(",")
            if (l[int(b[0])][int(b[1])] == '___'):
                l[int(b[0])][int(b[1])] = " o "
        for i in range(len(l)):
            print("|",end='')
            for j in range(len(l[i])):
                print(l[i][j],end='')
                print("|",end='')
            print("\n")
        d = losewin(l)
        if d=="1":
            print("Congratulations {} You won the game".format(p1))
            break
        elif d=="2":
            print("Congratulations {} You won the game".format(p2))
            break
        flag+=1
        if flag==9:
            print("It's a draw...")
            break

print("Let's play Tic Tac Toe")
print("You will have to enter in  row,column form")
p1 = input("Enter name of first player: ")
p2 = input("Enter name of second player: ")
gb()
moves(p1,p2)
