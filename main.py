from matplotlib import pyplot as plt
x = []
y = []
c = 0
for i in range(12000):
    c += 0.001
    p = 0.5
    for j in range(60):
        p = c * p * (1 - p)
        if j > 20:
            x.append(c)
            y.append(p)
plt.scatter(x,y,s=0.001)
plt.show()