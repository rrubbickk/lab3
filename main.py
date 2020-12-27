import math
import struct


l = []
for i in range(1000):
    l.append([])
    for j in range(1000):
        l[i].append(0)
for k in range(int(2*math.pi*1000)):
    t = k / 1000
    for i in range(-2, 3):
        for j in range(-2, 3):
            l[int(500+20*(math.sin(t)-math.sin(5 * t)/5)*15)+i][int(500+20*(math.cos(t)+math.cos(5*t)/5)*15)+j] = 1

with open("result.bmp", 'wb') as file:
    file.write(struct.pack("<hi2hi", 19778, 1000062, 0, 0, 62))
    file.write(struct.pack("<3i2h6i", 40, 1000, 1000, 1, 8, 0, 0, 0, 0, 2, 0))
    file.write(struct.pack("<8B", *(0, 0, 0, 0), *(255, 255, 255, 0)))
    for i in range(1000):
        for j in range(1000):
            if l[i][j] == 1:
                file.write(struct.pack("<B", 0))
            else:
                file.write(struct.pack("<B", 1))
