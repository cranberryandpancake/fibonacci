def calculate_fibonacci(n):
    if n < 0:
        return "음수에 대한 피보나치 수는 정의되지 않습니다."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n + 1):
            next_fib = a + b
            a = b
            b = next_fib
        return b

try:
    input_num = int(input("찾고 싶은 피보나치 수의 순서(0부터 시작)를 입력하세요."))
    fib_result = calculate_fibonacci(input_num)
    if isinstance(fib_result, str):
        print(fib_result)
    else:
        print(f"피보나치 수열의 {input_n}번째 항은 {fib_result}입니다.")
except ValueError:
    print("유효한 정수를 입력해 주세요.")

