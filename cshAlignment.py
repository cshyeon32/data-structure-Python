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
        A[i], A[least] = A[least], A[i] #i와 least 위치 바꾸기
    return A #A리스트 반환

#2.삽입 정렬
def insertion_sort(A):
    n = len(A)#리스트 길이를 n 에 저장
    for i in range(1,n): #리스트 1~마지막 전까지 돌기
        key = A[i]#키값을 i로 정하기
        j = i-1 #j는 i 앞에꺼로 설정
        while j >= 0 and A[j] > key:#j이가 0이상이거나 key보다 끌
            A[j+1] = A[j]#j1칸 뒤에 값을 j 값으로 바꿈
            j-=1#j를 1칸 앞으로 옮긴다.
        A[j+1] = key#j뒤에 칸을 key 값으로 바꾼다.
    return A#A리스트 반환

#3.버블 정렬
def bubble_sort(A):
    n = len(A)#리스트 길이를 n 에 저장
    for i in range(n-1,0,-1):#n-1부터 1까지 돌기
        for j in range(i):#i만큼 돌기
            if A[j] > A[j+1]:#j가 j뒤에꺼 보다 클때 실행
                A[j], A[j+1] = A[j+1], A[j]#j, j뒤에꺼 서로 위치 바꾸기
    return A#A리스트 반환

# 4.퀵 정렬
def quick_sort(A, left, right):  # A = 리스트, left = 가장 앞에꺼, right = 가장 뒤에꺼
    if left < right:  # 리스트의 길이가 1보다 큰 경우에만 정렬을 수행
        i = left + 1  # i는 pivot을 제외한 부분의 시작 인덱스
        j = right  # j는 pivot을 제외한 부분의 끝 인덱스
        pivot = A[left]  # pivot은 가장 왼쪽 값으로 설정

        while i <= j:  # i가 j보다 작거나 같을 때까지 반복
            while i <= right and A[i] <= pivot:  # pivot보다 큰 값을 찾을 때까지 i 증가
                i += 1
            while j >= left and A[j] > pivot:  # pivot보다 작은 값을 찾을 때까지 j 감소
                j -= 1
            if i < j:  # i가 j보다 작으면 두 값의 위치를 바꿈
                A[i], A[j] = A[j], A[i]

        A[left], A[j] = A[j], A[left]  # pivot과 j가 만난 지점의 값을 바꿈

        quick_sort(A, left, j - 1)  # 왼쪽 부분에 대해 퀵 정렬 재귀 호출
        quick_sort(A, j + 1, right)  # 오른쪽 부분에 대해 퀵 정렬 재귀 호출

    return A  # 정렬된 리스트 반환

# 5.합병 정렬
def merge(A, left, mid, right):
    i = left  # i는 왼쪽 부분의 시작 인덱스
    j = mid + 1  #j는 오른쪽 부분의 시작 인덱스
    k = left  #k는 병합된 리스트에 값을 저장할 인덱스
    merged = [0] * len(A)  # 병합된 리스트 0으로 초기화

    while i <= mid and j <= right:#i가 mid보다 이하이거나 j가 right 이하일때 계속 실행
        if A[i] <= A[j]:  # 왼쪽 부분이 작거나 같으면 실행
            merged[k] = A[i]  # 병합 리스트에 왼쪽 값 저장
            i, k = i + 1, k + 1 #i와 j를 한 칸 뒤로 움기기
        else:# 왼쪽 부분이 작거나 같지 않을때
            merged[k] = A[j]  # 오른쪽 부분이 작으면 병합 리스트에 오른쪽 값 저장
            j, k = j + 1, k + 1 #i와 j를 한 칸 뒤로 움기기

    if i > mid:  # 왼쪽 부분이 이미 모두 병합된 경우
    # 남은 오른쪽 부분의 값들을 병합된 리스트에 그대로 복사
        merged[k : k + right - j + 1] = A[j : right + 1]
    else:  # 오른쪽 부분이 이미 모두 병합된 경우
    # 남은 왼쪽 부분의 값들을 병합된 리스트에 그대로 복사
        merged[k : k + mid - i + 1] = A[i : mid + 1]

    # 병합된 리스트를 원본 리스트의 해당 부분에 복사
    A[left : right + 1] = merged[left : right + 1]

def merge_sort(A, left, right):
    if left < right:# right가 left보다 큰 경우
        mid = (left + right) // 2 #중간값인 mid 구하기 (리스트를 반으로 나누기 위햐여)
        merge_sort(A, left, mid)# 왼쪽 부분 리스트를 정렬하기 위한 재귀 호출
        merge_sort(A, mid + 1, right)# 오른쪽 부분 리스트를 정렬하기 위한 재귀 호출
        merge(A, left, mid, right)# 정렬된 왼쪽과 오른쪽 부분 리스트를 병합하는 함수 호출

# 6-1.힙 정렬(힙을 이용한 정렬)
def heappush(heap, n) :
    heap.append(n)#힙에 원소 추가
    i = len(heap) - 1 #i는 원소 가장 마지막에 원소 추가한 인덱스
    while i != 1 and n > heap[i//2]: # i가 1이 아니거나 n이 자식노드값보다 클떄 계속 실행
        heap[i] = heap[i//2]#부모 노드(i)와 자식노드(i//2위치 교환
        i //= 2 # 부모 노드의 인덱스로 이동
    heap[i] = n # i에 n 삽입

def heappop(heap):
    # 힙에서 최댓값을 제거후 반환
    size = len(heap) - 1# size는 힙의 크기
    if size == 0: #힙이 비었을때
        return None #None를 리턴
    p = 1 # 현재 위치
    i = 2 # 자식 노드의 인덱스
    root = heap[1] # 제거할 최댓값(루트)
    last = heap[size] # 힙의 마지막 원소

    while i <= size: #i가 size보다 이하일때 계속 실행
        if i < size and heap[i] < heap[i + 1]: #i가 size보다 작거나 i의 값이 i의 뒤의 값보다 작을때 계속 실행
            i += 1 #i증가
        if last >= heap[i]:#last(마지막 원소) 가 i(선택한 자식)의 값 보다 크거나 같으면 멈추기
            break
        heap[p] = heap[i] # 부모 노드에 더 큰 자식 값을 복사
        p = i#p를 자식 노드로 이동
        i *= 2#다음 레벨의 자식 노드로 이동

    heap[p] = last #마지막 노드 삽입
    heap.pop()# 마지막 원소를 힙에서 제거
    return root# 제거한 최댓값 반환

def heap_sort(lst):
    heap = [0]# 힙을 나타내는 리스트를 초기화
    for e in lst: 
        heappush(heap, e)#리스트의 각 원소(e)를 heap에 삽입
    for i in range(1, len(lst) + 1):
        lst[-i] = heappop(heap)# 힙에서 최댓값을 꺼내어 역순으로 리스트에 저장
    #리스트를 반환
    return lst 

# 6-2. 힙 정렬(제자리정렬로 구현한 힙정렬)
def heapify(arr, n, i):
    # 현재 노드를 가장 큰 값으로 설정
    largest = i
    # 왼쪽 자식 노드에 대한 인덱스를 계산
    l = 2 * i
    # 오른쪽 자식 노드에 대한 인덱스를 계산
    r = 2 * i + 1
    #l이 n보다 이하이거나 i의 값이 l의 값보다 작을때 실행
    if l <= n and arr[i] < arr[l]:
        largest = l#largest(가장 큰 값)을 왼쪽 자식으로 바꿈 실행
    #r이 n 보다 이하이거나 largest의 값이 r보다 작을때
    if r <= n and arr[largest] < arr[r]:
        largest = r#largest(가장 큰 값)를 오른쪽 자식으로 바꿈
    if largest != i:#i와 largest의 값이 다를 경우
        arr[i], arr[largest] = arr[largest], arr[i]#i와 largest 위치 바꾸기
        heapify(arr, n, largest)#서브트리 ㅈㅐ귀 함수 실행

def heapSort(arr) :
    n = len(arr) - 1 #n은 힙의 크기
    for i in range(n//2, 0, -1) :
        heapify(arr, n, i)
    for i in range(n-1, 0, -1) :
        arr[i+1], arr[1] = arr[1], arr[i+1]#가장 큰 값(arr[1])을 가장 끝으로 이동
        heapify(arr, i, 1)#가장 큰 값을 제외하고 다시 최대 힙을 구성
    #리스트 반환
    return arr


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
    # 0이상 100이하 사이의 숫자 중 25개를 랜덤으로 리스트에 저장
    random_numbers = [random.randint(0, 100) for _ in range(25)]
    if num == 7:#7번을 누르면 프로그램 종료
        print("정렬 프로그램이 종료되었습니다.")
        break
    elif num == 1:#1번을 누르면 랜덤 리스트를 출력하고 선택 정렬로 정렬후 출력
        print("선택 정렬전 리스트 : ",random_numbers)
        rn = selection_sort(random_numbers)
        print("선택 정렬후 리스트 : ", rn)
    elif num == 2:#2번을 누르면 랜덤 리스트를 출력하고 삽입 정렬로 정렬후 출력
        print("삽입 정렬전 리스트 : ",random_numbers)
        rn = insertion_sort(random_numbers)
        print("삽입 정렬후 리스트 : ", rn)
    elif num == 3:#3번을 누르면 랜덤 리스트를 출력하고 버블 정렬로 정렬후 출력
        print("버블 정렬전 리스트 : ",random_numbers)
        rn = bubble_sort(random_numbers)
        print("버블 정렬후 리스트 : ", rn)
    elif num == 4:#4번을 누르면 랜덤 리스트를 출력하고 퀵 정렬로 정렬후 출력
        qrn = random_numbers
        print("퀵 정렬전 리스트 : ",qrn)
        rn = quick_sort(qrn, 0, len(qrn)-1)
        print("퀵 정렬후 리스트 : ", rn)
    elif num == 5:#5번을 누르면 랜덤 리스트를 출력하고 합병 정렬로 정렬후 출력
        mrn = random_numbers
        print("합병 정렬전 리스트 : ",mrn)
        rn = merge_sort(mrn, 0, len(mrn)-1)
        print("합병 정렬후 리스트 : ", mrn)
    elif num == 6:#6번을 누르면 랜덤 리스트를 출력하고 힙(힙을 이용한) 정렬로 정렬후 출력후 다시 랜덤 리스트를 출력하고 힙(제자리정렬) 정렬로 정렬후 출력
        hrn = random_numbers.copy()
        print("힙 정렬(힙을 이용) 전 리스트 : ", hrn)
        rn = heap_sort(hrn)
        print("힙 정렬(힙을 이용) 후 리스트 : ", rn)
        print("")
        print("-------------------------------------------------------------------------------------------------------")
        print("")
        hrn_copy = random_numbers.copy()
        hrn_copy.insert(0,0)
        print("힙 정렬(제자리정렬) 전 리스트 : ", hrn_copy[1:])
        rn = heapSort(hrn_copy)
        print("힙 정렬(제자리정렬) 후 리스트 : ", rn[1:])
    else :# 1~7 이외의 숫자가 들어오면 번호 오류를 안내하고 다시 번호 입력 받기
        print("번호 오류 입니다. 다시 입력하세요!")