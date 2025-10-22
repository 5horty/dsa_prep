from random import sample
class Iteration:
    def __init__(self):
        self.data = []
        self.max_size = 100

    def initialise(self):
        self.data = sample(range(1, 3 * self.max_size), self.max_size)
        
    def printAll(self):
        print("The size of the random array " + str(len(self.data)))
        print("Before sorting, the array is " + str(self.data))
    def selectionSort(self):
        for i in range(len(self.data) - 1):
            indMin = i
            for j in range(i + 1, len(self.data)):
            #find index of smallest item in the unsorted part of the list
                if (self.data[j] < self.data[indMin]):
                    indMin = j
            #index smallest located, move item to position i, swap (data[i], data[indMin])
                self.data[indMin], self.data[i] = self.data[i], self.data[indMin]
        return self.data



    def insertionSort(self):
        for i in range(1, len(self.data)):
            current = self.data[i]
            j = i
            while (j > 0 and current < self.data[j - 1]):
                self.data[j] = self.data[j - 1]
                j -= 1
            self.data[j] = current
        return self.data

    def bubbleSort(self):
        for i in range(len(self.data) - 1):
            for j in range(len(self.data) - 1):
                if (self.data[j] > self.data[j + 1]):
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data

    def linearSearch(self, item):
        for ind in range(len(self.data)):
            if (self.data[ind] == item):
                return ind
        print("Not found")
        return -1


    def binaryIterSearch(self, item):
        start = 0
        end = len(self.data) - 1
        while (start <= end):
            mid = (start + end) // 2
            if (self.data[mid] < item):
                start = mid + 1
            elif (self.data[mid] > item):
                end = mid - 1
            else:
                return mid
        print("Not found")
        return -1



def main():
    arr = Iteration()
    arr.initialise()
    arr.printAll()
    print("After the selection sort, the array is " + str(arr.selectionSort()))

    arr.initialise()
    arr.printAll()
    print("After the insertion sort, the array is " + str(arr.insertionSort()))

    arr.initialise()
    arr.printAll()
    print("After the bubble sort, the array is " + str(arr.bubbleSort()))

    arr.initialise()
    arr.printAll()
    ind = arr.linearSearch(5)
    print(ind)
    print("After the insertion sort, the array is " + str(arr.insertionSort()))
    ind = arr.linearSearch(5)
    print(ind)

    arr.initialise()
    arr.printAll()
    print("After the bubble sort, the array is " + str(arr.bubbleSort()))
    ind = arr.linearSearch(5)
    print(ind)
    ind = arr.binaryIterSearch(5)
    print(ind)


if __name__ == "__main__":
    main()
