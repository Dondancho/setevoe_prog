# cifrovoi koreny
n = int(input())

total = 0
total1 = 10

while total1 > 9:
    while n > 0:
        num = n % 10
        total += num
        n //= 10
    total1 = total
    n = total
    total = 0
print(total1)
# konec




        if i == 0 or i == n:
            print("*" * 19, sep="")
        else:
            print("*", "               ", "*")