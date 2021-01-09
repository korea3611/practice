from sys import stdin

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if array[mid] == target:
        return n_list.count(target)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n = int(stdin.readline())
n_list = sorted(map(int,stdin.readline().split()))
m = int(stdin.readline())
m_list = map(int,stdin.readline().split())

for i in m_list:
    result = binary_search(n_list, i, 0,n-1)
    print(result, end=' ')