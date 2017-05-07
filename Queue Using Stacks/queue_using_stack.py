s1 = []
s2 = []
o = 5
while(o!=4):
    print("1-Push",end=" || ")
    print("2-Pop",end=" || ")
    print("3-Print",end=" || ")
    print("4-Exit")
    o = int(input())
    if o == 1:
        print("Enter Number: ",end="")
        s1.append(input())
        s2.reverse()
        print("Current Queue:", " ".join(s2)," ".join(s1))
        s2.reverse()
    elif o == 2:
        if s2:
            print("Popped Element:",s2.pop())
            s2.reverse()
            print("Current Queue:", " ".join(s2)," ".join(s1))
            s2.reverse()
        else:
            while s1:
                s2.append(s1.pop())
            print(s2.pop())
            s2.reverse()
            print("Current Queue:", " ".join(s2)," ".join(s1))
            s2.reverse()
