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

close_actual = []
distance_actual = []
color_actual = []

close_observed = []
distance_observed = []
color_observed = []

with open('../Data/truth.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    close_index = headers.index('close')
    distance_index = headers.index('distance')
    color_index = headers.index('color')
    for row in reader:
        close_actual.append(int(row[close_index]))
        distance_actual.append(int(row[distance_index]))
        color_actual.append(int(row[color_index]))

with open('../Data/log.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    close_index = headers.index('23')
    distance_index = headers.index('24')
    color_index = headers.index('5')
    for row in reader:
        close_observed.append(row[close_index])
        distance_observed.append(row[distance_index])
        color_observed.append(row[color_index])

# Color Vision
correct = 0;
incorrect = 0;
for i in range(len(color_actual)):
    if (color_observed[i] == 'TRUE' and color_actual[i] == 0): correct += 1;
    elif (color_observed[i] == 'FALSE' and color_actual[i] != 0): correct += 1;
    else: incorrect += 1;
percent = round((correct / (correct + incorrect))*100,2)
print("Color Blindness: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# Close Eyesight
correct = 0;
incorrect = 0;
for i in range(len(close_actual)):
    if (close_observed[i] == 'TRUE' or close_observed[i] == 'FALSE'):
        if (close_observed[i] == 'TRUE' and close_actual[i] != 2): correct += 1;
        elif (close_observed[i] == 'FALSE' and close_actual[i] == 2): correct += 1;
        else: incorrect += 1;
percent = round((correct / (correct + incorrect))*100,2)
print("Close Vision: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# Distance Eyesight
correct = 0;
incorrect = 0;
for i in range(len(distance_actual)):
    if (distance_observed[i] == 'TRUE' or distance_observed[i] == 'FALSE'):
        if (distance_observed[i] == 'TRUE' and distance_actual[i] != 2): correct += 1;
        elif (distance_observed[i] == 'FALSE' and distance_actual[i] == 2): correct += 1;
        else: incorrect += 1;
percent = round((correct / (correct + incorrect))*100,2)
print("Distance Vision: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# General Eyesight
correct = 0;
incorrect = 0;
tp = 0;
tn = 0;
fp = 0;
fn = 0;
for i in range(len(distance_actual)):
    if ((distance_observed[i] == 'TRUE' or distance_observed[i] == 'FALSE') and (close_observed[i] == 'TRUE' or close_observed[i] == 'FALSE')):
        if (distance_observed[i] == 'TRUE' and close_observed[i] == 'TRUE'):
            if (distance_actual[i] + close_actual[i] >= 2): fn += 1; incorrect += 1;
            else: tn += 1; correct += 1;
        else:
            if (distance_actual[i] + close_actual[i] >= 2): tp += 1; correct += 1;
            else: fp += 1; incorrect += 1;

percent = round((correct / (correct + incorrect))*100,2)
print("General Eyesight: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")

# General Vision
correct = 0;
incorrect = 0;
tp = 0;
tn = 0;
fp = 0;
fn = 0;
for i in range(len(distance_actual)):
    if ((distance_observed[i] == 'TRUE' or distance_observed[i] == 'FALSE') and (close_observed[i] == 'TRUE' or close_observed[i] == 'FALSE')):
        if (distance_observed[i] == 'TRUE' and close_observed[i] == 'TRUE' and color_observed[i] == 'TRUE'):
            if (distance_actual[i] + close_actual[i] + color_actual[i] >= 2): fn += 1; incorrect += 1;
            else: tn += 1; correct += 1;
        else:
            if (distance_actual[i] + close_actual[i] + color_actual[i] >= 2): tp += 1; correct += 1;
            else: fp += 1; incorrect += 1;

percent = round((correct / (correct + incorrect))*100,2)
print("General Vision: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")
