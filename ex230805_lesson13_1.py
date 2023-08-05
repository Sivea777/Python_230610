t = np.arange(0.,1.0,0.05)
print(t)

# 脛度
t1 = 2 * np.pi * t
print(t1)

# 角度
y1 = np.sin(2 * np.pi * t)
y2 = np.cos(2 * np.pi * t)
print(y1)
print(y2)

#畫圖
figure1 = plt.figure(figsize=(8,4))
axes1 = figure1.add_subplot()
axes1.plot(y1)
axes1.plot(y2)
plt.show()