months1 = set(["january","feb","march","april","may"])
print(months1)

months1.add("june")
print(months1)

months2 = set(["july","augest","september"])
i = months1.union(months2)
print(i)

i.remove("january")
print(i)

i.pop()
print(i)

i.discard("feb")
print(i)

x= months1.copy()
print(x)

y= i.difference(months2)
print(y)

months2.clear()
print(months2)

print(i.issubset(months1))

print(i.issuperset(months1))


