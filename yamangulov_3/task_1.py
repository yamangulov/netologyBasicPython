ids = {'user1': [213, 213, 213, 15, 213],
'user2': [54, 54, 119, 119, 119],
'user3': [213, 98, 98, 35]}

labels = []
for values in ids.values():
    labels += values

print(set(labels))