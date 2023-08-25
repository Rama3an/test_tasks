import time
n = int(input())
arr = [float(input()) for _ in range(n)]
sum_arr = sum(arr)
for i in range(n):
    print(str(round(arr[i] / sum_arr, ndigits=3)).ljust(5, '0'))
