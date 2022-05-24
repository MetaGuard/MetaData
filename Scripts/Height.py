import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics

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
    height_index = headers.index('height')
    device_index = headers.index('device')
    for row in reader:
        actual.append(float(row[height_index]) / 100)
        device.append(row[device_index])

for i in range (1,N+1):
    camera_y = []
    with open('../Data/' + str(i) + '.txt') as file:
        for line in file:
            parts = line.split(': ')
            if (parts[0] == "main-camera"):
                coords = parts[1].strip('() \n').split(', ')
                if len(coords) >= 3 and (is_float(coords[1])):
                    camera_y.append(float(coords[1].strip(',')))
    camera_y = camera_y[15000:-15000]
    camera_y = [y for y in camera_y if y > 1]
    height = np.percentile(camera_y, 99.5)
    if device[i-1] == 'Oculus Quest 2': offset = 0.12
    if device[i-1] == 'HTC Vive': offset = 0.11
    if device[i-1] == 'Vive Pro 2': offset = 0.11
    predicted.append(height + offset)
    if (i == 1):
        plt.title('Observed Height vs. Time')
        plt.xlabel('Frame Number (#)')
        plt.ylabel('Observed Height (m)')
        plt.axhline(height, color='r')
        plt.plot(camera_y)
        plt.annotate("Predicted Height: " + str(height) + "m", (0, 1.68), color='Red')
        plt.annotate("← Squat jumps (room #9)", (28000, 1.05), color='Black')
        plt.tight_layout()
        plt.savefig('../Figures/height-time.pdf')
        plt.savefig('../Figures/height-time.png')
        plt.clf()

        plt.title('Histogram of Observed Heights')
        plt.ylabel('Number of Frames (#)')
        plt.xlabel('Observed Height (m)')
        plt.hist(camera_y)
        plt.tight_layout()
        plt.savefig('../Figures/height-hist.pdf')
        plt.savefig('../Figures/height-hist.png')
        plt.clf()

correlation_matrix = np.corrcoef(actual, predicted)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2
print('R²=' + str(r_squared))

plt.title('Actual vs. Predicted Height\n(n=' + str(N) + ', R²=' + str(round(r_squared, 2)) + ')')
plt.xlabel('Actual Height (m)')
plt.ylabel('Predicted Height (m)')
plt.scatter(actual, predicted)
z = np.polyfit(actual, predicted, 1)
p = np.poly1d(z)
plt.plot(actual,p(actual),"r")
plt.tight_layout()
plt.savefig('../Figures/height-corr.pdf')
plt.savefig('../Figures/height-corr.png')

errs = np.absolute(np.subtract(predicted, actual))
print('Accuracy within 5cm:', len([x for x in errs if x <= 0.05])/N)
print('Accuracy within 6cm:', len([x for x in errs if x <= 0.06])/N)
print('Accuracy within 7cm:', len([x for x in errs if x <= 0.07])/N)
