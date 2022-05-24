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

N=2
actual = []
device = []
predicted = []

with open('../Data/truth.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    ipd_index = headers.index('ipd')
    device_index = headers.index('device')
    for row in reader:
        actual.append(float(row[ipd_index]))
        device.append(row[device_index])

for i in range (1,N+1):
    ipd = []
    with open('../Data/' + str(i) + '.txt') as file:
        for line in file:
            parts = line.split(': ')
            if (parts[0] == "ipd"): ipd.append(float(parts[1]))
    predicted.append(statistics.median(ipd) * 1000)

z = np.polyfit(actual, predicted, 1)
p = np.poly1d(z)

correlation_matrix = np.corrcoef(actual, predicted)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print('R²=' + str(r_squared))
plt.title('Actual vs. Predicted IPD\n(n=' + str(N) + ', R²=' + str(round(r_squared, 2)) + ')')
plt.xlabel('Actual IPD (mm)')
plt.ylabel('Predicted IPD (mm)')
for l in ['Vive Pro 2', 'HTC Vive', 'Oculus Quest 2']:
    plt.scatter(
        [actual[i] for i in range(len(actual)) if device[i] == l],
        [predicted[i] for i in range(len(actual)) if device[i] == l],
        label=l
    )
plt.plot(actual,p(actual),"r")
plt.legend()
plt.tight_layout()
plt.savefig('../Figures/ipd-corr.pdf')
plt.savefig('../Figures/ipd-corr.png')

errs = np.absolute(np.subtract(predicted, actual))
print('Accuracy within 0.2mm:', len([x for x in errs if x <= 0.2])/N)
print('Accuracy within 0.5mm:', len([x for x in errs if x <= 0.5])/N)
print('Accuracy within 1mm:', len([x for x in errs if x <= 1])/N)
