# Проверим парадокс мальчиков и девочек
import random

def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()

    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1
    
print("P(Оба девочки|Старший ребенок девочка) = ", both_girls / older_girl)
print("P(Оба девочка|Хотя бы одна девочка) = ", both_girls / either_girl)