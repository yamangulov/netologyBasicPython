# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

phrase_1=input("Введите первую фразу:")
phrase_2=input("Введите вторую фразу:")
if len(phrase_1) > len(phrase_2):
    print("Фраза 1 длиннее фразы 2")
elif len(phrase_2) > len(phrase_1):
    print("Фраза 2 больше фразы 1")
else:
    print("Фразы равной длины")


