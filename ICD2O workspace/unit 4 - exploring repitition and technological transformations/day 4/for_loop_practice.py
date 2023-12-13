#question 1
def numbers():
    for i in range (10):
        print(i+1)

numbers()

#question 2
def even():
    for i in range(2,11,2):
        print(i)

even()

#question 3
def calculate():
    total = 0
    for i in range(1,8,2):
        total += i
    
    print(total)

calculate()

#question 4
def backward():
    for i in range (10,0,-1):
        print(i)

backward()

#question 5
def multiple():
    for i in range(4,21,4):
        print(i)

multiple()

#question 6
def product():
    total = 1
    for i in range(1,6):
        total *= i
    print(total)

product()

#question 7
def divisible():
    for i in range(1,13):
        if i % 3 == 0:
            print(i)

divisible()

#question 8
def countdown():
    for i in range(5,0,-1):
        print(i)
    print("blast off!")

countdown()

#question 9
def sqaures():
    for i in range(1,6):
        print(i*i)

sqaures()


#question 10
def factorial():
    for n in range(1,8):
        product = 1
        for i in range(n,0,-1):
            product *= i
        print(product)


factorial()

#question 11 and 12
def string():
    word = "WONDERFUL"
    result = ""
    for i in range(1,len(word),2):
        result += word[i]
    print(result)

string()

#question 13
def count():
    count = 0
    word = "COMPUTER".lower()
    for index in range(len(word)):
        if word[index] in ('a','e','i','o','u'):
            count += 1
    print(count)
count()

#question 13
def palindrome():
    backwards = ""
    forwards = "RACECAR"
    for i in range(len(forwards)-1, -1, -1):
        backwards += forwards[i]

    if backwards == forwards:
        print("yes, it is a palindrome!")
    else:
        print("no, it is not a palindrome.")

palindrome()







        
