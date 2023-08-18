x = ["a"]
x.append("a")
x.append("b")
x.extend(["c", "d"])
x.append("e")
x[-1], x[-2] = x[-2], x[-1]
x.pop()
x.reverse()
x.remove("c")

x.clear()

print(x)