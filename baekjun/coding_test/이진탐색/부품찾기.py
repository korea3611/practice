def binary_search(array, target, start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int,input().split()))

for i in m_list:
    result = binary_search(n_list, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')