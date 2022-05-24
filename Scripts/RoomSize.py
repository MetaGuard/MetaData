import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import statistics

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False

N = 2
real_w = []
real_l = []
real_a = []
found_w = []
found_l = []
found_a = []
device = []

with open('../Data/truth.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    width_index = headers.index('width')
    length_index = headers.index('length')
    device_index = headers.index('device')
    for row in reader:
        real_w.append(float(row[width_index]))
        real_l.append(float(row[length_index]))
        real_a.append(float(row[width_index]) * float(row[length_index]))
        device.append(row[device_index])

for i in range (1,N+1):
    camera_x = []
    camera_y = []
    camera_z = []
    with open('../Data/' + str(i) + '.txt') as file:
        for line in file:
            parts = line.split(': ')
            if (parts[0] == "main-camera"):
                coords = parts[1].strip('() \n').split(', ')
                if len(coords) >= 3 and is_float(coords[0]) and is_float(coords[1]) and is_float(coords[2]):
                    camera_x.append(float(coords[0]))
                    camera_y.append(float(coords[1]))
                    camera_z.append(float(coords[2]))

    camera_x = camera_x[1200:-2400]
    camera_y = camera_y[1200:-2400]
    camera_z = camera_z[1200:-2400]
    left = np.percentile(camera_x, 0)
    right = np.percentile(camera_x, 99.9)
    bottom = np.percentile(camera_z, 0)
    top = np.percentile(camera_z, 99.9)

    width = right - left
    length = top - bottom
    actual_w = real_w[i-1]
    actual_l = real_l[i-1]
    center_x = left + (width/2)
    center_y = bottom + (length/2)
    found_w.append(width)
    found_l.append(length)
    found_a.append(width * length)

    if (i == 1):
        plt.title('2D Location Data; Actual vs. Predicted Room Size')
        plt.plot(camera_x, camera_z)
        ax = plt.gca()
        rect = patches.Rectangle((left, bottom), width, length, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
        plt.annotate("Observed Width: " + str(round(width, 2)) + "m\nObserved Length: " + str(round(length, 2)) + "m", (left + 0.05, bottom + 0.05), color='r')
        plt.annotate("Actual Width: " + str(round(actual_w, 2)) + "m\nActual Length: " + str(round(actual_l, 2)) + "m", (right - 0.05, bottom + 0.05), color='b', ha='right')
        rect = patches.Rectangle((center_x - actual_w/2, center_y - actual_l/2), actual_w, actual_l, linewidth=2, edgecolor='b', facecolor='none')
        ax.add_patch(rect)
        plt.tight_layout()
        plt.savefig('../Figures/room-size.pdf')
        plt.savefig('../Figures/room-size.png')

errs = np.absolute(np.subtract(real_a, found_a))
print('Accuracy within 1m²:', len([x for x in errs if x <= 1.0])/N)
print('Accuracy within 2m²:', len([x for x in errs if x <= 2.0])/N)
print('Accuracy within 3m²:', len([x for x in errs if x <= 3.0])/N)
