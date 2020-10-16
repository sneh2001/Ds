
class sort:
    def __init__(self,arr,type):
        self.arr = arr
        self.type = type
        if self.type == 'i' or 'I':
            self.insertionSort()
        elif self.type == 'b' or 'B':
            self.bubbleSort()
        elif self.type == 's' or 'S':
            self.selection()
        else:
            print('Invalid Sort type')

    def insertionSort(self):  
        print('Using Insertion Sort')
        for i in range(1, len(self.arr)): 
            key = self.arr[i] 
            j = i-1
            while j >=0 and key < self.arr[j] : 
                    self.arr[j+1] = self.arr[j] 
                    j -= 1
            self.arr[j+1] = key 

    def bubbleSort(self): 
        print('Using Bubble Sort')
        n = len(self.arr)  
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                if self.arr[j] > self.arr[j+1] : 
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
    
    def selection(self):
        print('Using Selection Sort')
        for i in range(len(self.arr)):  
            min_ = i 
            for j in range(i+1, len(self.arr)): 
                if self.arr[min_] > self.arr[j]: 
                    min_ = j       
            self.arr[i], self.arr[min_] = self.arr[min_], self.arr[i]

a = [7,8,6,2,3,5,7,2,0,1,3]
sort(a, 'I')
print(a)


########



class Sorting:
    
    def _init_(self,lst):
        self.lst = lst
        
    def bubble_sort(self,lst):
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[i] < lst[j]:
                    lst[i],lst[j] = lst[j],lst[i]
                else:
                    pass
        return lst

    def selection_sort(self,lst):
        for i in range(len(lst)):
            smallest_element = i
            for j in range(i+1,len(lst)):
                if lst[smallest_element] > lst[j]:
                    smallest_element = j
            lst[i],lst[smallest_element] = lst[smallest_element],lst[i]
        return lst

    def insertion_sort(self,lst): 
        for i in range(1, len(lst)): 
            index = lst[i] 
            j = i-1
            while j >= 0 and index < lst[j] : 
                    lst[j + 1] = lst[j] 
                    j -= 1
            lst[j + 1] = index 
        return lst
    
    def run_sort(self):
        while True:
            print('Select the sorting algorithm:')
            print('1. Bubble Sort.')
            print('2. Selection Sort.')
            print('3. Insertion Sort.')
            print('4. Quit')
            opt = int(input('Option: '))
            if opt == 1:
                print(sort.bubble_sort(self.lst))
            elif opt == 2:
                print(sort.selection_sort(self.lst))
            elif opt == 3:
                print(sort.insertion_sort(self.lst))
            else:
                break
lst = [4,2,3,9,12,1] 
sort = Sorting(lst)
sort.run_sort(
