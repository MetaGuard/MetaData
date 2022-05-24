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
l_actual = []
r_actual = []
l_predicted = []
r_predicted = []
device = []
hand = []

with open('../Data/truth.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    l_index = headers.index('left')
    r_index = headers.index('right')
    device_index = headers.index('device')
    hand_index = headers.index('hand')
    for row in reader:
        l_actual.append(float(row[l_index]) / 100)
        r_actual.append(float(row[r_index]) / 100)
        device.append(row[device_index])
        hand.append(row[hand_index])

for i in range (1,N+1):
    left = []
    right = []
    cam = []
    dleft = []
    dright = []
    dist = []

    with open('../Data/' + str(i) + '.txt') as file:
        for line in file:
            parts = line.split(': ')
            if (parts[0] == "left-controller"): left.append(parts[1].strip('() \n').split(', '))
            if (parts[0] == "right-controller"): right.append(parts[1].strip('() \n').split(', '))
            if (parts[0] == "main-camera"): cam.append(parts[1].strip('() \n').split(', '))

    for j in range(min([len(cam), len(left), len(right)])):
        l = left[j]
        r = right[j]
        c = cam[j]
        if (len(l) == 3 and len(r) == 3 and len(c) == 3
            and is_float(l[0]) and is_float(l[1]) and is_float(l[2])
            and is_float(r[0]) and is_float(r[1]) and is_float(r[2])
            and is_float(c[0]) and is_float(c[1]) and is_float(c[2])):
            xl = float(l[0])
            yl = float(l[1])
            zl = float(l[2])
            xc = float(c[0])
            yc = float(c[1])
            zc = float(c[2])
            xr = float(r[0])
            yr = float(r[1])
            zr = float(r[2])
            d = math.sqrt((xl - xr)**2 + (yl - yr)**2 + (zl - zr)**2)
            dist.append(d)
            dl = math.sqrt((xl - xc)**2 + (zl - zc)**2)
            dleft.append(dl)
            dr = math.sqrt((xr - xc)**2 + (zr - zc)**2)
            dright.append(dr)

    dist = dist[12000:-12000]
    if (max(dist[0:25000]) >= 6): dist = dist[25000:]
    if (max(dist[0:5000]) >= 2.5): dist = dist[5000:]
    while (max(dist) >= 6): dist = dist[:-5000]
    while (max(dist) >= 2): dist = dist[5000:]

    wingspan = max(dist)
    index = dist.index(wingspan)
    left = dleft[index]
    right = dright[index]
    if device[i-1] == 'Oculus Quest 2':
        offset_l = 0.23
        offset_r = 0.19
    if device[i-1] == 'HTC Vive':
        offset_l = 0.59
        offset_r = 0.57
    if device[i-1] == 'Vive Pro 2':
        offset_l = 0.51
        offset_r = 0.52
    l_predicted.append(left + offset_l)
    r_predicted.append(right + offset_r)
    dleft.sort()
    dright.sort()

# Longer Arm
correct = 0;
incorrect = 0;
for i in range(len(l_actual)):
    if (abs(l_actual[i] - r_actual[i]) <= 0.03): continue;
    if (l_actual[i] > r_actual[i]):
        if (l_predicted[i] > r_predicted[i]): correct += 1
        else: incorrect += 1
    elif (l_actual[i] < r_actual[i]):
        if (l_predicted[i] < r_predicted[i]): correct += 1
        else: incorrect += 1

percent = round((correct / (correct + incorrect))*100,2)
print("Arm Length: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")
