def fibo(n_int):
    if n_int == 0:
        return 0
    elif n_int== 1:
        return 1
    else:
        return fibo(n_int-1) + fibo(n_int-2)

def fib(n):
    num = n
    while True:
        if num.isdigit():
            print('Fib('+num+') = ', fibo(int(num)))
            num = input('Please enter another non-negative integer or type stop: ')
        elif num == 'stop':
            break
        else:
            print('The input argument', num, 'is not a non-negative integer!')
            num = input('Please enter a non-negative integer: ')

fib('amir')
