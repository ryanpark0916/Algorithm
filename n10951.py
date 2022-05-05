while True:
    try:
        sum = 0
        arr = input().split()
        for i in arr:
            sum += int(i)
        print(sum)

    except EOFError:
        break

    # 채점 결과:
    #  - 1차: 실패(EOFError 예외처리 X)
    #  - 2차: 실패(언어 선택 오류)
    #  - 3차: 성공