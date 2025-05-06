# -*- coding: utf-8 -*-
"""
Created on Thu May  1 16:05:46 2025

@author: Meenakshi
"""

a = [5,7,2,9,3]
n=len(a)
print("Len is:",n)


def bubbleSort(a):
    for i in range(n):
        for j in range(i,n):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a

#arr = bubbleSort(a)

print("Bubble sort is running : ")

def SelectionSort(a):
    
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if(a[j]<a[min_idx]):
                min_idx=j
            temp=a[i]
            a[i]=a[min_idx]
            a[min_idx]=temp
    return a

print("Selection sort is running...")

#sesort = SelectionSort(a)

def insertionSort(a):
    
    for i in range(1,n):
        key = a[i]
        j=i-1
        while(j>=0 and a[j]>key):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return a
        
#insort = insertionSort(a)


def QuickSort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return QuickSort(left)+middle+QuickSort(right)

qsort=QuickSort(a)

for i in range(n):
    print(qsort[i])
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)