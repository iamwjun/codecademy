# 判断是否为质数
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                return False
        return True

print(is_prime(6))

# 字符串倒序
def reverse(text):
    word = ""
    l = len(text) - 1
    while l > 0:
        word = word + text[l]
        l -= 1
    return word

print(reverse("abcdef"))

# 去掉字符串中 aeiouAEIOU
def anti_vowel(text):
    word = ""
    for c in text:
        if c not in "aeiouAEIOU":
            word = word + c
    return word

anti_vowel("Hey look Words!")

# 数字积分游戏
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    w = word.lower()
    for k in w:
        total = total + score[k]
    return total

# 替换指定字符
def censor(text, word):
    a = text.split(word)
    w = '*' * len(word)
    r = w.join(a)
    return r
  
print(censor("this hack is wack hack", "hack"))

# 统计item在list中出现在的次数
def count(sequence, item):
    sum = 0
    for i in sequence:
        if i == item:
            sum += 1
    return sum

print(count([1, 2, 1, 1], 1))

# 返回list中偶数
def purify(lists):
    result = []
    for i in lists:
        if i % 2 == 0:
            result.append(i)
    return result

purify([1, 2, 3])

# 返回list中数字乘积
def product(lists):
    total = 1
    for i in lists:
        total *= i
    return total

print(product([4, 5, 5]))

# 清除list中重复项
def remove_duplicates(lists):
    result = []
    for i in lists:
        if i not in result:
             result.append(i)
    return result

remove_duplicates([1, 1, 2, 2])

# 计算list中位数
import math

def median(lists):
    length = len(lists)
    relist = sorted(lists)
    if length % 2 == 0:
        value = relist[length / 2] + relist[(length / 2) - 1]
        result = value / 2.0
    else:
        result = relist[int(math.floor(length / 2))]
    return result