t = int(input())

for i in range(1, t + 1):
    sum = 0
    testCase = input().split()
    for j in testCase:
        sum += int(j)
    print(sum)

# 채점 결과: 성공