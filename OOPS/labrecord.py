# Write a Python program to count the frequency of each character in a string using a dictionary.
str=input("Enter a string: ")
dict={}
for i in str:
    dict[i]=str.count(i)
print(dict)
# Write a Python program to use the split() and join() methods to split a string into a list of words and then join the list back into a string.
a="hi i am python programmer"
b=a.split()
print(b)
c="".join(b)
print(c)
# Write a Python program to check if two strings are similar using the difflib module.
from difflib import SequenceMatcher
def Nearly_Equal(a, b):
    return SequenceMatcher(None, a, b).ratio()
a="khit"
b="khitc"
c=Nearly_Equal(a, b)
if(c*100>80):
    print("Both Strings are similar")
    print("a is mutation of b")
else:
    print("Both Strings are different")
# Write a Python program to find the GCD and LCM of two numbers. 
import fractions
n1=int(input("Enter n1 value: "))
n2=int(input("Enter n2 value: "))
gcd=fractions.gcd(n1,n2)
print("GCD of n1 and n2 is: ",gcd)
def lcm(n1,n2):
    return (n1*n2)//gcd
print("LCM of n1 and n2 is: ",lcm(n1,n2))
# Write a Python program to implement the merge sort algorithm.
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is")
    printList(arr)
# Write a Python program to implement the selection sort algorithm.
import sys
A=[64,25,12,22,11]
for i in range(len(A)-1):
    min_idx=i
    for j in range(i+1,len(A)):
        if A[j]<A[min_idx]:
            min_idx=j
    A[i],A[min_idx]=A[min_idx],A[i]
print("Sorted array is")
for i in range(len(A)):
    print("%d" %A[i],end=" ")
# Write a Python program to implement the insertion sort algorithm.   
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr= [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array is")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

