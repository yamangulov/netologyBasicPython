boys = ["Peter", "Alex", "John", "Arthur", "Richard"]
girls = ["Kate", "Liza", "Kira", "Emma", "Trisha"]

# boys = ["Peter", "Alex", "John", "Arthur", "Richard", "Michael"]
# girls = ["Kate", "Liza", "Kira", "Emma", "Trisha"]

if len(boys) != len(girls):
    print("Результат:")
    print("Внимание, кто-то может остаться без пары!")
else:
    result = zip(sorted(boys), sorted(girls))
    print("Результат:")
    print("Идеальные пары:")
    for pare in list(result):
        print(pare[0], "и", pare[1])
