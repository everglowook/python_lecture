def print_root(a,b,c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('해는', r1, '또는', r2)

    # 계수 값이 다른 2차 방정식의 해를 구함
print_root(1,2,-8)
print_root(2,-6,-8)
  