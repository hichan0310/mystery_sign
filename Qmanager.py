import random as r


# 여기에 문제 추가
# 현재 23개


class question_manager:
    def __init__(self):
        self.questions = [
            [lambda a, b: (a - b) ** 2, "빼서 제곱".encode("utf-8"), ""],
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
            [lambda a, b: self.hardthing(a, b), "각 숫자가 합쳐서 몇 개가 있는지".encode("utf-8")],
            [lambda a, b: (a + b) % 12, "제작자는 시계라고 하는데 솔직히 이건 좀 억지임".encode("utf-8")],
            [lambda a, b: a // b + b // a, "몫".encode("utf-8")],
            [lambda a, b: abs(a * a - b * b), "제곱의 차(더하고 빼고 해서 곱한 거)".encode("utf-8")],
            [lambda a, b: (a + 1) * (b - 1), "(a+1)(b-1)".encode("utf-8")],
            [lambda a, b: (a - 1) * (b + 1), "(a-1)(b+1)".encode("utf-8")],
            [lambda a, b: a + a * b, "a+ab".encode("utf-8")],
            [lambda a, b: (a + b) * a, "a(a+b)".encode("utf-8")],
            [lambda a, b: a * b + a // b + b // a, "a*b+몫".encode("utf-8")],
            [lambda a, b: sum(list(map(int, list(str(a + b))))), "더해서 자리수 합".encode("utf-8")],
            [lambda a, b: self.sumeverynum(a ** b), "a^b의 자리수 합(많이 변태같음)".encode("utf-8")],
            [lambda a, b: self.jinbub_2(a) + self.jinbub_2(b), "이진법으로 바꾸고 2개 그대로 합하기".encode("utf-8")],
            [lambda a, b: sum(range(min(a, b), max(a, b) + 1)), "a~b 수들의 합".encode("utf-8")],
            [lambda a, b: self.listmul(self.inttolist(a)) + self.listmul(self.inttolist(b)), "각 자리 숫자의 곱의 합(0은 곱하지 않음)".encode("utf-8")]
        ]
        self.length = len(self.questions)
        self.index = r.randint(0, self.length)
        self.explain = self.questions[self.index][1]

    def answer(self, a, b):
        return self.questions[self.index][0](a, b)

    def hardthing(self, a, b):
        ans = ''
        alist = list(map(int, list(str(a))))
        blist = list(map(int, list(str(b))))
        nlist = alist + blist
        CountList = [0] * 10
        for i in nlist:
            CountList[i] += 1
        for i in range(1, 10):
            if CountList[i]:
                ans = str(ans) + str(i) + str(CountList[i])
        if CountList[0]:
            ans = str(ans) + str(0) + str(CountList[0])
        return int(ans)

    def sumeverynum(self, a):
        return sum(list(map(int, list(str(a)))))

    def jinbub_2(self, a):
        ans = ''
        while (a != 0):
            if (a % 2 == 1):
                ans = '1' + ans
            else:
                ans = '0' + ans
            a = a // 2
        if a == 0:
            return 0
        return int(ans)

    def inttolist(self, num):
        return list(map(int, list(str(num))))

    def listmul(self, numlist):
        a = 1
        for i in numlist:
            if (i != 0):
                a = a * i
        return a
