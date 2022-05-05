while True:
    try:
        sum = 0
        inputData = input()
        if not(inputData == "0 0"):
            inputArr = inputData.split()
            for i in inputArr:
                sum += int(i)
            print(sum)
        else:
            break
    except EOFError:
        break

# 채점 결과: 성공