import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

random.shuffle(nouns)
random.shuffle(adverbs)
random.shuffle(adjectives)

for i in range(len(nouns)):
    print(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
