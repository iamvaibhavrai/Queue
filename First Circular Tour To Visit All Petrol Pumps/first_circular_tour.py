from queue import Queue

class PetrolPump:
    def __init__(self,petrol,distance):
        self.petrol = petrol
        self.distance = distance

def printTour(a,n):
        start,end = 0,1
        currentPetrol = a[start].petrol - a[start].distance
        while start != end:
            while currentPetrol < 0:
                currentPetrol -= a[start].petrol - a[start].distance
                start = (start+1)%n
                if start == 0:
                    return -1
            currentPetrol += a[start].petrol - a[start].distance
            end = (end+1)%n
        return start


def main():
    n = int(input())
    a = []
    for i in range(n):
        x,y = map(int,input().split(" "))
        a.append(PetrolPump(x,y))
    start = printTour(a,n)
    print(start+1 if start != -1 else "No Tour Found")

if __name__ == '__main__':
    main()
