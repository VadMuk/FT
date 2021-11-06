
# Online Python - IDE, Editor, Compiler, Interpreter

def sum_digit(n, current_sum=0):
    if n == 0:
        return current_sum
    else:
        digit = n % 10
        current_sum += digit
        n //= 10
        return sum_digit(n, current_sum)
summ = 493193
# summ =sum_digit(summ)
# print (summ)
while summ > 10: 
   summ = sum_digit(summ)
print (summ)
