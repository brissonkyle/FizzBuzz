my_nums = [2,7,8,9,100,66,44,22,55,11,234,678,990,1000]


def fizzbuzz (num):
    if num % 3 == 0 and num % 5 == 0 :
        print('FizzBuzz')
    elif num % 5 == 0 :
        print('Buzz')
    elif num % 3 == 0 :
        print('Fizz')
    else :
        print('No fizzbuzz :(')

fizzbuzz(45)

for num in my_nums :
    fizzbuzz(num)
    print(num)