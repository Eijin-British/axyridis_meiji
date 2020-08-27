
import random
import matplotlib.pyplot as plt

#初期値を設定
model = {1: 2, 2: 2, 3: 2}
#print(model)

x = 1
k1_t = []
k2_t = []
while x <=10000:
#keyとvalueで分割
    keys = []
    vals = []
    for key, val in model.items():
        keys.append(key)
        vals.append(val)
    #print(vals)

#2つを抽出して、1足す
    a, b = random.choices(vals, k=2, weights=vals)
    #print(a, b)
    a += 1
    b += 1
#a, b が元々あった場所を探す
    for i in range(len(vals)):
        if vals[i] == a-1:
            vals[i] = a
            break
    for j in range(len(vals)):
        if vals[j] == b-1:
            vals[j] = b
            break

#keyとvalueを合体させる
    model = dict(zip(keys, vals))
    model[len(model)+1] = 2
    #print(model)
    k1_t.append(model[4])
    if len(model) > 4:
        k2_t.append(model[5])
    else:
        k2_t.append(0)
    x += 1

#グラフ生成
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

#グラフに要素を追加
t = list(range(1, 10001))
ax1.plot(t, k1_t)
ax1.plot(t, k2_t)


#グラフ描画
plt.show()
