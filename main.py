maxfib = input("Bitte geben Sie eine Zahl ein: ")
maxfib = int(maxfib)
fib1 = 0
fib2 = 1
fib = 0
print(fib1)
print(fib2)
while fib <= maxfib:
    fib = fib1 + fib2
    if fib <= maxfib:
        print(fib)
    fib1 = fib2
    fib2 = fib