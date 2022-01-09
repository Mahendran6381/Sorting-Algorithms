import time
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
if __name__ == '__main__':
       arr = list(map(int , input("enter the sequence : ").split(" ")))
       print(arr)
       print(time.time())
       bubble_sort(arr)
       print(arr)      
       print(time.time())         
