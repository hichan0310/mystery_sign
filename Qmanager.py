import random as r

#여기에 문제 추가

class question_manager:
    def __init__(self):
        self.questions = [
            [lambda a, b: (a - b) ** 2, "빼서 제곱".encode("utf-8")],
            [lambda a, b: a % b if a > b else b % a, "나머지".encode("utf-8")],
            [lambda a, b: a + b ** 2, "a+b**2".encode("utf-8")],
            [lambda a, b: a ** 2 + b, "a**2+b".encode("utf-8")],
            [lambda a, b: sum(list(map(int, list(str(a))))) + sum(list(map(int, list(str(a))))), "각 자리 수의 총합".encode("utf-8")],
            [lambda a, b: sum(list(map(int, list(str(a))))) * sum(list(map(int, list(str(a))))), "각 자리 수의 합의 곱".encode("utf-8")],
            [lambda a, b: abs(sum(list(map(int, list(str(a))))) - sum(list(map(int, list(str(a)))))), "각 자리 수의 합의 차".encode("utf-8")],
            [lambda a, b: (a + 1) * (b + 1), "1씩 더해서 곱하기".encode("utf-8")],
            [lambda a, b: (a - 1) * (b - 1), "1씩 빼서 곱하기".encode("utf-8")],
            [lambda a, b: (a + b) % 12, "더해서 12로 나눈 나머지".encode("utf-8")],
            [lambda a, b: a // b + b // a, "나누었을 때 몫".encode("utf-8")],
        ]
        self.length = len(self.questions)
        self.index = r.randint(0, self.length)
        self.explain = self.questions[self.index][1]

    def answer(self, a, b):
        return self.questions[self.index][0](a, b)