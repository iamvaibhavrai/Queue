from queue import Queue

def main():
    a = list(map(int,input().split(" ")))
    a.sort()
    n = len(a)
    q1 = Queue()
    q2 = Queue()
    q0 = Queue()
    s = 0
    res = []
    for i in a:
        s += i
        if i%3 == 0:
            q0.put(i)
        if i%3 == 1:
            q1.put(i)
        if i%3 == 2:
            q2.put(i)
    if s % 3 == 0:
        while not q0.empty():
            res.append(q0.get())
        while not q1.empty():
            res.append(q1.get())
        while not q2.empty():
            res.append(q2.get())
    if s % 3 == 1:
        if q1:
            q1.get()
        else:
            q2.get()
            q2.get()
        while not q0.empty():
            res.append(q0.get())
        while not q1.empty():
            res.append(q1.get())
        while not q2.empty():
            res.append(q2.get())
    if s % 3 == 2:
        if q2:
            q2.get()
        else:
            q1.get()
            q1.get()
        while not q0.empty():
            res.append(q0.get())
        while not q1.empty():
            res.append(q1.get())
        while not q2.empty():
            res.append(q2.get())
    res = sorted(res,reverse=True)
    for x in res:
        print(x,end="")

if __name__ == '__main__':
    main()
