# sdic = {1: 'first',2: 'second'}
# print(type(sdic))

# print(dir(int))


# print("abcd")
# print(type("abcd"))


# rr = "Jesus Christ"

# print(rr.rjust(30))
# print(rr.center(30))

# won , ex_rate = 2500000, 1430.8

# # print("{:12d}원은 ${:10.3f} 입니다.". format(won,won/ex_rate))
# # print("{1:}원은 ${0:} 입니다.". format(won,won/ex_rate))
# print(f"{won} will be {chr(8364)}{won/ex_rate}. Right?")


# name = input("이름을 입력하세요: ")
# age = int(input("나이를 입력하세요: "))
# print(f"안녕하세요. {name}님! 당신은 {age}살입니다.")

# order = "커피"
# price = 3500
# print("주문하신 {}의 가격은 {}원입니다.".format(order,price))

# print("%-10s %-10s %-10s" %("이름","상품","가격"))
# print("%-10s %-10s %-10d" %("홍길동","커피",3500))


# def hisam():
#     print("Hi how are you?")
#     print(12 * 12)
#     print(won)
#     print(ex_rate)

# print(hisam())

# func = hisam
# print(func)

# print(type(func))
# print(type(hisam))




# def hisam(name):
#     print(f"Hi,{name}, how are you today?")
    
# hisam("Hodong")
# print(hisam("Tom"))

# # 섭씨를 화씨로 변환하는 함수 정의
# def c_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# def f_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius

# celsius = float(input("섭씨 온도를 입력하세요: ")) # 사용자로부터 섭씨 온도 입력 받기
# print(f"{celsius}도는 화씨로 {fahrenheit:.2f}도 입니다.") #결과 출격


# (lambda : print("안녕"))()


# func1 = lambda x: x+1
# func2 = lambda x, y: x+y

# print(func1(10))
# print(func2(100, 200))


# multi = lambda a, b: a*b
# print(multi(7, 8))

# print(bin(7))
# print(oct(10))
# print(hex(15))


# lst = [7, 2, 4, 5, 3]
# print(sorted(lst)) # 오름차순
# print(sorted(lst, reverse=True)) # 내림차순
# print(list(reversed(lst))) #반대로

# pl = {("basic", 1964, 5), ("java", 1995, 2), ("kotlin", 2016, 7), ("python", 1991, 1), ("c", 1972, 3)}
# # print(sorted(pl))


# print(sorted(pl, key= lambda sam: sam[2]))

# for ksh in range(0, 10, 2):
#     print(ksh, end="   ") 

# num = 5

# while (num > 0):
#     print("while loop executing")
#     num = num-1
#     print("After the minus operation")
# else:
#     print("End of while")



for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j} * {i} = {i*j:2d}", end="  ㅣ ")
    print()
    
