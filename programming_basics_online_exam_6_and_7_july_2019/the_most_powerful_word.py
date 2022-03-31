# Задача 6. Най-силната дума
# Да откриеш коя е "най-силната" дума.
# До получаване на команда "End of words" ще се четат от конзолата думи. За да се открие силата на всяка една,
# трябва да се намери сборът от ASCII стойностите на символите, от които се състои думата.

# Ако започва с гласна буква - 'a', 'e', 'i', 'o', 'u', 'y' (или техните еквивалентни главни букви),
# полученият сбор трябва да се умножи по дължината на думата, в противен случай,
# да се раздели на дължината и да се закръгли до най-близкото цяло число надолу.
# Вход
# До получаване на команда "End of words" се чете по един ред от конзолата:
# •	дума – текст


word = input()
best_sum = 0
best_word = ''

while word != "End of words":
    sum = 0     # МНОГО ВАЖНО ДА Е ВЪТРЕ!!!
    for letter in word:
        sum += ord(letter)
    must_be_multiplied = False  # МНОГО ВАЖНО ДА Е ВЪТРЕ!!!
    if word[0] == 'a' or word[0] == 'A':
        must_be_multiplied = True
    elif word[0] == 'e' or word[0] == 'E':
        must_be_multiplied = True
    elif word[0] == 'i' or word[0] == 'I':
        must_be_multiplied = True
    elif word[0] == 'o' or word[0] == 'O':
        must_be_multiplied = True
    elif word[0] == 'u' or word[0] == 'U':
        must_be_multiplied = True
    elif word[0] == 'y' or word[0] == 'Y':
        must_be_multiplied = True

    if must_be_multiplied:
        sum = int(sum * len(word))
    if not must_be_multiplied:
        sum = int(sum / len(word))

    if sum > best_sum:
        best_sum = sum
        best_word = word
        sum = 0
    word = input()

print(f"The most powerful word is {best_word} - {best_sum}")







# Изход
# След приключване на програмата се печата на един ред думата с "най-голяма сила":
# •	"The most powerful word is {думата с най-голяма сила} - {силата на думата}"

word = input()
best_sum = 0
best_word = ''

while word != "End of words":
    sum = 0     # МНОГО ВАЖНО ДА Е ВЪТРЕ!!!
    for letter in word:
        sum += ord(letter)
    must_be_multiplied = False  # МНОГО ВАЖНО ДА Е ВЪТРЕ!!!
    if word[0] in ('A''a''E''e''I''i''O''o''U''u''Y''y'):
        must_be_multiplied = True

    if must_be_multiplied:
        sum = int(sum * len(word))
    if not must_be_multiplied:
        sum = int(sum / len(word))

    if sum > best_sum:
        best_sum = sum
        best_word = word
        sum = 0
    word = input()

print(f"The most powerful word is {best_word} - {best_sum}")