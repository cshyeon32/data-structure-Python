import random
import time
#1.선택 정렬
def selection_sort(A):
    n = len(A) #리스트 길이를 n 에 저장
    for i in range(n-1): #리스트 길이만큼 돌기
        least = i #i 를 least 라고 두기
        for j in range(i+1, n): #i+1 부터 리스트 길이 즉 끝까지 돌기
            if A[j] < A[least]: # 만약 j가 least 보다 작으면 
                least = j #j를 least로 두기 
        A[i], A[least] = A[least], A[i]
    return A

#2.삽입 정렬
def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j-=1
        A[j+1] = key
    return A

#3.버블 정렬
def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1):
      #  bChanged = False
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                #bChanged = True
       # if not bChanged : break
    return A


#4.퀵 정렬
def quick_sort(A, left, right):
    if left < right:
        i = left + 1
        j = right
        pivot = A[left]

        while i <= j:
            while i <= right and A[i] <= pivot:
                i += 1
            while j >= left and A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        A[left], A[j] = A[j], A[left]

        quick_sort(A, left, j - 1)
        quick_sort(A, j + 1, right)

    return A


# 5.합병 정렬
def merge(A, left, mid, right):
    i = left
    j = mid + 1
    k = left
    merged = [0] * len(A)

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            merged[k] = A[i]
            i, k = i + 1, k + 1
        else:
            merged[k] = A[j]
            j, k = j + 1, k + 1

    if i > mid:
        merged[k : k + right - j + 1] = A[j : right + 1]
    else:
        merged[k : k + mid - i + 1] = A[i : mid + 1]

    A[left : right + 1] = merged[left : right + 1]

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)


# 6-1. 힙 정렬(힙을 이용한 정렬)
def heapify(date, n, i):
    # 현재 노드를 가장 큰 값으로 설정함
    largest = i
    # 왼쪽 자식 노드에 대한 인덱스를 계산
    l = 2 * i
    # 오른쪽 자식 노드에 대한 인덱스를 계산
    r = 2 * i + 1

    # 왼쪽 자식이 힙의 크기 내에 있고, 현재의 값보다 크면 largest(가장 큰 값)를 왼쪽 자식으로 업데이트함.
    if l <= n and date[i - 1] < date[l - 1]:
        largest = l
    # 오른쪽 자식이 힙의 크기 내에 있고, 현재의 값보다 크면 largest(가장 큰 값)를 오른쪽 자식으로 업데이트함.
    if r <= n and date[largest - 1] < date[r - 1]:
        largest = r

    # largest가 변경되면 현재 노드와 largest 노드 값을 교환, 이후 다시 heapify() 함수 호출
    if largest != i:
        date[i - 1], date[largest - 1] = date[largest - 1], date[i - 1]
        heapify(date, n, largest)

# 힙 정렬 1
def heap_sort(date):
    n = len(date)
    # 최대 힙 구성
    for i in range(n // 2, 0, -1):
        heapify(date, n, i)
    # 힙에서 원소를 하나씩 꺼내어 정렬함.
    for i in range(n - 1, 0, -1):
        date[i], date[0] = date[0], date[i]
        heapify(date, i, 1)
    # 힙 정렬된 리스트를 반환함
    return date


# 6-2. 힙 정렬(제자리정렬로 구현한 힙정렬)
def heapPush(heap, n):
    # 힙에 원소를 추가, 그리고 힙 속성을 유지
    heap.append(n)
    i = len(heap) - 1
    while i != 0 and n > heap[i // 2]:
        heap[i] = heap[i // 2]
        i //= 2
    heap[i] = n

# 힙 정렬 2
def heapPop(heap):
    # 힙에서 최댓값을 제거후 반환
    size = len(heap) - 1
    if size == 0:
        return None
    p = 0
    i = 1
    root = heap[0]
    last = heap[size]
    while i <= size:
        if i < size and heap[i] < heap[i + 1]:
            i += 1
        if last >= heap[i]:
            break
        heap[p] = heap[i]
        p = i
        i *= 2
    heap[p] = last
    heap.pop()
    return root

# 힙 정렬 2
def heapSort(lst):
    # 정렬을 요하는 리스트를 Heap에 Input, 그 후 다시 꺼내어 정렬
    heap = [0]
    for e in lst:
        heapPush(heap, e)
    for i in range(1, len(lst) + 1):
        lst[-i] = heapPop(heap)
    # 힙 정렬된 리스트를 반환
    return lst





print("""************************************************
***  여러가지 정렬 프로그램 구현             ***
***                                          ***
*** 1. 선택(selection) 정렬                  ***
*** 2. 삽입(insertion) 정렬                  ***
*** 3. 버블(bubble) 정렬                     ***
*** 4. 퀵(quick) 정렬                        ***
*** 5. 합병(merge) 정렬                      ***
*** 6. 힙 정렬(heap) 정렬                    ***
*** 7. 종료(quit)                            ***
************************************************""")
time.sleep(2)

while True:
    print("")
    num = int(input("원하는 정렬의 번호를 입력하세요 : "))
    print("")
    random_numbers = [random.randint(0, 100) for _ in range(25)]
    if num == 7:
        print("정렬 프로그램이 종료되었습니다.")
        break
    elif num == 1:
        print("선택 정렬전 리스트 : ",random_numbers)
        rn = selection_sort(random_numbers)
        print("선택 정렬후 리스트 : ", rn)
    elif num == 2:
        print("삽입 정렬전 리스트 : ",random_numbers)
        rn = insertion_sort(random_numbers)
        print("삽입 정렬후 리스트 : ", rn)
    elif num == 3:
        print("버블 정렬전 리스트 : ",random_numbers)
        rn = bubble_sort(random_numbers)
        print("버블 정렬후 리스트 : ", rn)
    elif num == 4:
        qrn = random_numbers
        print("퀵 정렬전 리스트 : ",qrn)
        rn = quick_sort(qrn, 0, len(qrn)-1)
        print("퀵 정렬후 리스트 : ", rn)
    elif num == 5:
        mrn = random_numbers
        print("합병 정렬전 리스트 : ",mrn)
        rn = merge_sort(mrn, 0, len(mrn)-1)
        print("합병 정렬후 리스트 : ", mrn)
    elif num == 6:
        hrn = random_numbers.copy()
        print("힙 정렬(힙을 이용) 전 리스트 : ", hrn)
        rn = heap_sort(hrn)
        print("힙 정렬(힙을 이용) 후 리스트 : ", rn)
        print("")
        print("-------------------------------------------------------------------------------------------------------")
        print("")
        hrn_copy = random_numbers.copy()
        print("힙 정렬(제자리정렬) 전 리스트 : ", hrn_copy)
        rn = heapSort(hrn_copy)
        print("힙 정렬(제자리정렬) 후 리스트 : ", rn)
    else :
        print("번호 오류 입니다. 다시 입력하세요!")
