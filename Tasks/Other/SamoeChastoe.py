
with open('C:\\Python_Course\\Text.txt') as f:
    text = f.read().lower().split()
popular_word = max(set(text), key=text.count)
print(popular_word, text.count(popular_word))