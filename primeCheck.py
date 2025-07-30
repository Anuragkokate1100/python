num = int(input("Enter a number: "))
if num < 2:
    print("Not a prime number")
else:
    i = 2
    is_prime = True
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
