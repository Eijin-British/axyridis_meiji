
import random
import matplotlib.pyplot as plt

#�����l��ݒ�
model = {1: 2, 2: 2, 3: 2}
#print(model)

x = 1
k1_t = []
k2_t = []
while x <=10000:
#key��value�ŕ���
    keys = []
    vals = []
    for key, val in model.items():
        keys.append(key)
        vals.append(val)
    #print(vals)

#2�𒊏o���āA1����
    a, b = random.choices(vals, k=2, weights=vals)
    #print(a, b)
    a += 1
    b += 1
#a, b �����X�������ꏊ��T��
    for i in range(len(vals)):
        if vals[i] == a-1:
            vals[i] = a
            break
    for j in range(len(vals)):
        if vals[j] == b-1:
            vals[j] = b
            break

#key��value�����̂�����
    model = dict(zip(keys, vals))
    model[len(model)+1] = 2
    #print(model)
    k1_t.append(model[4])
    if len(model) > 4:
        k2_t.append(model[5])
    else:
        k2_t.append(0)
    x += 1

#�O���t����
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

#�O���t�ɗv�f��ǉ�
t = list(range(1, 10001))
ax1.plot(t, k1_t)
ax1.plot(t, k2_t)


#�O���t�`��
plt.show()
