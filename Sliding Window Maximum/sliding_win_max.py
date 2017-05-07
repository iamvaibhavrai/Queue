from collections import deque

def slidindMax(a,k):
    n = len(a)
    d = deque()
    for i in range(k):
        while d and a[i] >= a[d[-1]]:
            d.pop()
        d.append(i)
    for i in range(k,n):
        print(a[d[0]],end=" ")
        while d and d[0] <= i-k:
            d.popleft()
        while d and a[i] >= a[d[-1]]:
            d.pop()
        d.append(i)
    print(a[d[0]])

def main():
    print("Enter Array: ")
    a = list(map(int,input().split(" ")))
    print("Enter Window Size: ")
    k = int(input())
    slidindMax(a,k)

if __name__ == '__main__':
    main()
