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
device = []
refresh_rate = []
tracking_rate = []
camera_w = []
camera_h = []
tr_obs = []

with open('../Data/truth.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    device_index = headers.index('device')
    for row in reader:
        device.append(row[device_index])

with open('../Data/log.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    tr_index = headers.index('rate')
    for row in reader:
        tr_obs.append(float(row[tr_index]))

for i in range (1,N+1):
    rr = []
    tr = []
    cw = []
    ch = []
    with open('../Data/' + str(i) + '.txt') as file:
        for line in file:
            parts = line.split(': ')
            if (parts[0] == "refresh-rate" and is_float(parts[1]) and float(parts[1]) < 10000): rr.append(float(parts[1]))
            if (parts[0] == "tracking-rate" and is_float(parts[1]) and float(parts[1]) < 10000): tr.append(float(parts[1]))
            if (parts[0] == "camera-w" and is_float(parts[1]) and float(parts[1]) < 10000): cw.append(float(parts[1]))
            if (parts[0] == "camera-h" and is_float(parts[1]) and float(parts[1]) < 10000): ch.append(float(parts[1]))

    refresh_rate.append(statistics.median(rr))
    tracking_rate.append(statistics.median(tr))
    camera_w.append(statistics.median(cw))
    camera_h.append(statistics.median(ch))

    if (i == 1):
        plt.title('Histogram of Observed Tracking and Refresh Rates')
        plt.ylabel('Number of Frames (#)')
        plt.yscale('log')
        plt.xlabel('Observed Rate (Hz)')
        plt.hist(rr, bins=np.arange(30,870,60), label='Refresh Rate', hatch='\\\\', alpha=0.8)
        plt.hist(tr, bins=np.arange(30,870,60), label='Tracking Rate', hatch='//', alpha=0.8)
        plt.xticks(np.arange(0,900,60))
        plt.tight_layout()
        plt.legend()
        plt.savefig('../Figures/device-hist.pdf')
        plt.savefig('../Figures/device-hist.png')

# Refresh Rate
correct = 0;
incorrect = 0;
for i in range(len(device)):
    err = 3
    if (device[i] == 'HTC Vive'):
        if (abs(refresh_rate[i] - 90) <= err): correct += 1
        else: incorrect += 1
    if (device[i] == 'Vive Pro 2'):
        if (abs(refresh_rate[i] - 120) <= err): correct += 1
        else: incorrect += 1

percent = round((correct / (correct + incorrect))*100,2)
print("Display Refresh Rate: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# Tracking Rate
correct = 0;
incorrect = 0;
for i in range(len(device)):
    err = 2.5
    if (device[i] == 'HTC Vive'):
        if (abs(tracking_rate[i] - 90) <= err): correct += 1
        else: incorrect += 1
    if (device[i] == 'Vive Pro 2'):
        if (abs(tracking_rate[i] - 120) <= err): correct += 1
        else: incorrect += 1

percent = round((correct / (correct + incorrect))*100,2)
print("Tracking Refresh Rate: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# Device Resolution (w)
correct = 0;
incorrect = 0;
for i in range(len(device)):
    err = 20
    if (device[i] == 'HTC Vive'):
        if (abs(camera_w[i] - 1852) <= err): correct += 1
        else: incorrect += 1;
    if (device[i] == 'Vive Pro 2'):
        if (abs(camera_w[i] - 2440) <= err): correct += 1
        else: incorrect += 1;
    if (device[i] == 'Oculus Quest 2'):
        if (abs(camera_w[i] - 1628) <= err): correct += 1
        else: incorrect += 1;

percent = round((correct / (correct + incorrect))*100,2)
print("Resolution w: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# Device Resolution (h)
correct = 0;
incorrect = 0;
for i in range(len(device)):
    err = 20
    if (device[i] == 'HTC Vive'):
        if (abs(camera_h[i] - 2056) <= err): correct += 1
        else: incorrect += 1;
    if (device[i] == 'Vive Pro 2'):
        if (abs(camera_h[i] - 2440) <= err): correct += 1
        else: incorrect += 1;
    if (device[i] == 'Oculus Quest 2'):
        if (abs(camera_h[i] - 1628) <= err): correct += 1
        else: incorrect += 1;

percent = round((correct / (correct + incorrect))*100,2)
print("Resolution h: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# Device Resolution (MP)
correct = 0;
incorrect = 0;
for i in range(len(device)):
    err = 98000
    if (device[i] == 'HTC Vive'):
        if (abs(camera_h[i]*camera_w[i] - 3807712) <= err): correct += 1
        else: incorrect += 1;
    if (device[i] == 'Vive Pro 2'):
        if (abs(camera_h[i]*camera_w[i] - 6051600) <= err): correct += 1
        else: incorrect += 1;
    if (device[i] == 'Oculus Quest 2'):
        if (abs(camera_h[i]*camera_w[i] - 2650384) <= err): correct += 1
        else: incorrect += 1;

percent = round((correct / (correct + incorrect))*100,2)
print("Resolution MP: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# Refresh Rate (Weak)
correct = 0;
incorrect = 0;
for i in range(len(device)):
    err = 60
    if (device[i] == 'HTC Vive'):
        if (abs(tr_obs[i] - 60) <= err): correct += 1
        else: incorrect += 1;
    if (device[i] == 'Vive Pro 2'):
        if (abs(tr_obs[i] - 120) <= err): correct += 1
        else: incorrect += 1;
    if (device[i] == 'Oculus Quest 2'):
        if (abs(tr_obs[i] - 120) <= err): correct += 1
        else: incorrect += 1;

percent = round((correct / (correct + incorrect))*100,2)
print("Refresh Rate (Weak): " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")
