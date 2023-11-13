import random

print("""*************************************
***  여러가지 정렬 프로그램 구현  ***
***                               ***
*** 1. 선택(selection) 정렬       ***
*** 2. 삽입(insertion) 정렬       ***
*** 3. 버블(bubble) 정렬          ***
*** 4. 퀵(quick) 정렬             ***
*** 5. 합병(merge) 정렬           ***
*** 6. 힙(heap) 정렬              ***
*** 7. 종료(quit)                 ***
*************************************""")

#선택 정렬
def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        print("Step", i+1, "=", A)

#삽입 정렬
def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
        print("Step", i, "=", A)

#버블 정렬
def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+A] = A[j+1], A[j]
                bChanged = True
        if not bChanged : break
        print("Step", n-i, "=", A)


#퀵 정렬
def quick_sort(A, left, right):
    print("quick_sort(A,",left, right, ")")
    if left < right:
        i = left + 1
        j = right
        pivot = A[left]
        while i <= j:
            while i <= right and A[i] <= pivot:
                i+=1
            while j >= left and A[j] > pivot:
                j-=1
            if j < j:
                A[i], A[j] = A[j], A[i]; print_qs(A)
        A[left], A[j] = A[j], A[left]; print_qs(A)
        quick_sort(A, left, j-1)
        quick_sort(A, j+1, right)
s = 1

def print_qs(A):
    global s
    print("Step", s, "=", A)
    s += 1

# 합병 정렬
s = 1
def merge(A, left, mid, right):
    print("merge (",left, ",", mid, ",", right, ")")
    global s
    global sorted
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k = i+1, k+1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid:
        sorted[k : k+right-j+1] = A[j : right+1]
    else:
        sorted[k : k+mid-i+1] = A[i : mid+1]

    A[left : right+1] = sorted[left : right+1]

    print("Step", s, "=", sorted)
    s +=1

def merge_sort(A, left, right):
    print("merge_sort (",left, ",", right, ")")
    if left < right:
        mid  = (left + right)//2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)

    
#힙 정렬(힙을 이용한 정렬)
def heappush(heap, n):
    heap.append(n)
    i = len(heap) - 1
    while i != 1 and n > heap[i//2]:
        heap[i] = heap[i//2]
        i//2
    heap[i] = n

def heappop(heap):
    size = len(heap) - 1
    if size == 0:
        return None
    p = 1
    i = 2
    root = heap[1]
    last = heap[size]
    while i <= size:
        if i < size and heap[i] < heap[i+1] :
            i += 1
        if last >= heap[i]:
            break
        heap[p] = heap[i]
        p = i
        i *= 2
    heap[p] = last
    heap.pop()
    return root

def heap_sort(data):
    heap = [0]
    for e in data:
        heappush(heap, e)
    for i in range(1, len(data) + 1):
        data[-i] = heappop(heap)


#힙 정렬(제자리정렬로 구현한 힙정렬)
def heapify(arr, n, i) :
    largest = i
    l = 2*i
    r = 2*i + 1
    
    if l <= n and arr[i] < arr[l]:
        largest = l
    if r <= n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
        
def heapSort(arr):
    n = len(arr) - 1
    for i in range(n//2, 0, -1):
        heapify(arr, n, i)
        print("i =", i, arr)

    for i in range(n-1, 0, -1):
        arr[i+1], arr[1] = arr[1], arr[i+1]
        heapify(arr, i, 1)
        print("i =", i, arr)


