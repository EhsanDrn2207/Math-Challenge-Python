import random
import math
import time

OPERATORS = ["+", "-", "*","/"]
MIN_NUM = 3
MAX_NUM = 12
TOTAL_QUESTION = 10


def generate_problem():
    left = random.randint(MIN_NUM, MAX_NUM)
    right = random.randint(MIN_NUM, MAX_NUM)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    if operator == "/":
        answer = math.ceil(eval(expr))
    answer = round(eval(expr), 1)
    return expr, answer

def timer(func):
    def wrapped():
        start = time.time()
        func()
        end = time.time()
        total_time = end - start
        print("Nice work! You finished in", round(total_time, 2), "seconds!")
    return wrapped

@timer
def solve_problems():
    wrong = 0
    input("Press enter to start!")
    print("----------------------")

    for i in range(TOTAL_QUESTION):
        expr, answer = generate_problem()
        while True:
            guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
            if guess == str(answer):
                break
            wrong += 1

    print("----------------------")
    print("Wrong answers: ", wrong)
    
solve_problems()