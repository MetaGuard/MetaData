import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False

N = 2
actual = []
device = []
predicted = []

with open('../Data/truth.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    wingspan_index = headers.index('wingspan')
    device_index = headers.index('device')
    for row in reader:
        actual.append(float(row[wingspan_index]) / 100)
        device.append(row[device_index])

for i in range (1,N+1):
    left = []
    right = []
    dist = []

    with open('../Data/' + str(i) + '.txt') as file:
        for line in file:
            parts = line.split(': ')
            if (parts[0] == "left-controller"): left.append(parts[1].strip('() \n').split(', '))
            if (parts[0] == "right-controller"): right.append(parts[1].strip('() \n').split(', '))

    for j in range(len(right)):
        l = left[j]
        r = right[j]
        if (len(l) == 3 and len(r) == 3 and is_float(l[0]) and is_float(l[1]) and is_float(l[2]) and is_float(r[0]) and is_float(r[1]) and is_float(r[2])):
            x1 = float(l[0])
            y1 = float(l[1])
            z1 = float(l[2])
            x2 = float(r[0])
            y2 = float(r[1])
            z2 = float(r[2])
            d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            dist.append(d)

    dist = dist[12000:-12000]
    if (max(dist[0:25000]) >= 6): dist = dist[25000:]
    if (max(dist[0:5000]) >= 2.5): dist = dist[5000:]
    while (max(dist) >= 6): dist = dist[:-5000]
    while (max(dist) >= 2): dist = dist[5000:]

    wingspan = max(dist)
    if device[i-1] == 'Oculus Quest 2': offset = -0.01
    if device[i-1] == 'HTC Vive': offset = -0.03
    if device[i-1] == 'Vive Pro 2': offset = 0.06
    predicted.append(wingspan + offset)

    if (i == 1):
        plt.title('Observed Wingspan vs. Time')
        plt.xlabel('Frame Number (#)')
        plt.ylabel('Observed Wingspan (m)')
        plt.axhline(wingspan, color='r')
        plt.plot(dist)
        plt.annotate("Predicted Wingspan: " + str(round(wingspan, 2)) + "m", (40000, 1.65), color='Red')
        plt.annotate("T-pose (room #8) →", (0, 1.65), color='Black')
        plt.tight_layout()
        plt.savefig('../Figures/wingspan-time.pdf')
        plt.savefig('../Figures/wingspan-time.png')
        plt.clf()

correlation_matrix = np.corrcoef(actual, predicted)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print('R²=' + str(r_squared))

plt.title('Actual vs. Predicted Wingspan\n(n=' + str(N) + ', R²=' + str(round(r_squared, 2)) + ')')
plt.xlabel('Actual Wingspan (m)')
plt.ylabel('Predicted Wingspan (m)')
plt.scatter(actual, predicted)
z = np.polyfit(actual, predicted, 1)
p = np.poly1d(z)
plt.plot(actual,p(actual),"r")
plt.tight_layout()
plt.savefig('../Figures/wingspan-corr.pdf')
plt.savefig('../Figures/wingspan-corr.png')

errs = np.absolute(np.subtract(predicted, actual))
print('Accuracy within 5cm:', len([x for x in errs if x <= 0.05])/N)
print('Accuracy within 7cm:', len([x for x in errs if x <= 0.07])/N)
print('Accuracy within 12cm:', len([x for x in errs if x <= 0.12])/N)
