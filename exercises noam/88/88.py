def balanced(n):
    nagtive = 0
    pcsitive = 0

    for i in n:
        if i > 0:
            pcsitive += 1
        else:
            nagtive += 1

    if nagtive == pcsitive:
        print(f"The number is positive {sorted(n)}")
    else:
        print(f"The number is nagtive {sorted(n, reverse=True)}")
balanced([1,2,-3,-4])