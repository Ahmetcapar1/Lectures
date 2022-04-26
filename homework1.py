import random
import time

from numpy import integer
liste= random.sample(range(10,100000000),10000000)
sorted_liste=sorted(liste)
x=random.choice(liste)
def list_unsorted(arr,x):
    if x in arr:
        return True
    else:
        return False
def list_sorted(arr,x):
    if x in arr:
        return True
    else:
        return False
def iterative_search(arr,x):
    for i in arr:
        if i==x:
            return True
    return False
def sorted_binary_search_iterative(arr,x):
    low=0
    high=len(arr)-1
    mid=0
    while low<= high:
        mid=(low+high)//2
        if arr[mid] < x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        elif arr[mid] == x:
            return True
        else:
            return False
def recursive_binary_search(arr,x):
    if len(arr)==0:
        return False
    arr=sorted(arr)
    mid_index=(len(arr)-1)//2
    if arr[mid_index] == x:
        return True
    elif arr[mid_index]<x:
        return recursive_binary_search(arr[mid_index+1:],x)
    elif arr[mid_index]>x:
        return recursive_binary_search(arr[:mid_index],x)
    else:
        return False
def binary_search_iterative(arr,x):
    arr= sorted(arr)
    low=0
    high=len(arr)-1
    mid=0
    while low<= high:
        mid=(low+high)//2
        if arr[mid] < x:
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        elif arr[mid] == x:
            return True
        else:
            return False
def set_search(arr,x):
    arr=set(arr)
    for i in arr:
        if i==x:
            return True
    
    return False
start_time=0
end_time=0
for i in range(10):
    start_time+=time.time()
    list_unsorted(liste,x)
    end_time+=time.time()
a= (end_time-start_time)/10
start_time_1=0
end_time_1=0
for i in range(10):
    start_time_1+=time.time()
    list_sorted(sorted_liste,x)
    end_time_1+=time.time()
b=(end_time_1-start_time_1)/10
start_time_2=0
end_time_2=0
for i in range(10):
    start_time_2+=time.time()
    iterative_search(liste,x)
    end_time_2+=time.time()
c=(end_time_2-start_time_2)/10
start_time_3=0
end_time_3=0
for i in range(10):
    start_time_3+=time.time()
    sorted_binary_search_iterative(sorted_liste,x)
    end_time_3+=time.time()
d=(end_time_3-start_time_3)/10
start_time_4=0
end_time_4=0
for i in range(10):
    start_time_4+=time.time()
    recursive_binary_search(liste,x)
    end_time_4+=time.time()
e=(end_time_4-start_time_4)/10
start_time_5=0
end_time_5=0
for i in range(10):
    start_time_5+=time.time()
    binary_search_iterative(liste,x)
    end_time_5+=time.time()
f=(end_time_5-start_time_5)/10
start_time_6=0
end_time_6=0
for i in range(10):
    start_time_6+=time.time()
    set_search(liste,x)
    end_time_6+=time.time()
g=(end_time_6-start_time_6)/10
bout= [a,b,c,d,e,f,g]
print(bout)