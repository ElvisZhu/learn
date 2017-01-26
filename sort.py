# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
    
def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

def insertionSort_bak(arr):
    for i in range(1,len(arr)):
        t=arr[i]
        j=i-1
        while(j>=0):
            if arr[j] > t:
                arr[j+1] = arr[j]
                if j==0:
                    arr[j]=t
                    break
            else:
                arr[j+1] = t
                break
            j=j-1
    return arr
                
def insertionSort(arr):
    for i in range(len(arr)):
        tmp = arr[i]
        prei = i-1
        while prei >= 0 and arr[prei] > tmp:
            arr[prei+1] = arr[prei]
            prei -= 1
        arr[prei+1] = tmp
    return arr

def shellSort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr    

import math   
def mergeSort_bak(arr):
    if len(arr)<=1:
        return arr
    spi=math.floor(len(arr)/2)
    arr1=mergeSort_bak(arr[0:spi])
    arr2=mergeSort_bak(arr[spi:])
    r_arr=[]
    i,j=0,0
    while True:
        if arr1[i]<=arr2[j]:
            r_arr.append(arr1[i])
            i+=1
        else:
            r_arr.append(arr2[j])
            j+=1
        if i == len(arr1):
            r_arr = r_arr + arr2[j:]
            break
        if j == len(arr2):
            r_arr = r_arr + arr1[i:]
            break
    return r_arr
        
def mergeSort(arr):
    if len(arr)<=1:
        return arr
    spi=math.floor(len(arr)/2)
    arr1=mergeSort(arr[0:spi])
    arr2=mergeSort(arr[spi:])
    r_arr=[]
    while True:
        if arr1[0]<=arr2[0]:
            r_arr.append(arr1.pop(0))
        else:
            r_arr.append(arr2.pop(0))
        if not arr1:
            r_arr = r_arr + arr2
            break
        if not arr2:
            r_arr = r_arr + arr1
            break
    return r_arr    
    
    
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot=arr.pop(0)
    l=[]
    r=[]
    while arr:
        if arr[0]<=pivot:
            l.append(arr.pop(0))
        else:
            r.append(arr.pop(0))
    return quickSort(l)+[pivot]+quickSort(r)
        
        
        
        
    
    
    
    