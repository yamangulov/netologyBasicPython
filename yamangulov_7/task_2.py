from exchange import Rate

r0 = Rate(format='full')
print((r0.eur()))

r1 = Rate()
print(r1.eur())

r2 = Rate(diff=True)
print(r2.eur())