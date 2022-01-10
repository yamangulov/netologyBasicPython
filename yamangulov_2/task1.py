word = input("Введите слово из английских букв: ")
if len(word) % 2 != 0:
    i = int(len(word)//2)
    print(word[i])
else:
    i = int(len(word)/2)
    print(word[i - 1], word[i])