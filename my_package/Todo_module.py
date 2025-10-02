#my_package/todo_module.py

def num_sum(num1,num2):
    result = 0
    for v in range(num1,num2+1):
        result += v
    print(result)    
    
#num_sum(2,10)

def num_sum2(num1=0,num2=10):
    result = 0
    for v in range(num1,num2+1):
        result += v
    print(result)

#num_sum2()

def func(num):
    num = int(num)
    for v in range(1,10):
        print(f"{num} * {v} = {num*v}")

#func(input("정수 입력 : "))


def func2(weight,tall):
    result = weight/(tall**2)
    str = ''
    if result < 18.5:
        str = '저체중'
    elif result >= 18.5 and result < 25:    
        str = '정상'
    elif result >= 25 and result < 30:    
        str = '과체중'
    elif result >= 30:    
        str = '비만'
    print(result)
    print(str)

#func2(65,1.7)