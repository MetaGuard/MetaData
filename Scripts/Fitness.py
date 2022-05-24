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
predicted = []

with open('../Data/truth.csv', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    fitness_index = headers.index('fitness')
    for row in reader:
        actual.append(float(row[fitness_index]))

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
    low = np.percentile(camera_y, 0.05)
    depth = height - low
    predicted.append(depth)
    if (i == 1):
        plt.title('Observed Height vs. Time')
        plt.xlabel('Frame Number (#)')
        plt.ylabel('Observed Height (m)')
        plt.axhline(low, color='r')
        plt.plot(camera_y)
        plt.annotate("Squat Depth: " + str(round(depth, 2)) + "m", (0, low + 0.02), color='Red')
        plt.annotate("← Squat jumps (room #9)", (28000, 1.05), color='Black')
        plt.tight_layout()
        plt.savefig('../Figures/fitness-time.pdf')
        plt.savefig('../Figures/fitness-time.png')

correct = 0;
incorrect = 0;
for i in range(0,N):
    if (actual[i] == 1):
        if (predicted[i] < 0.5): correct += 1;
        else: incorrect += 1;
    else:
        if (predicted[i] > 0.5): correct += 1;
        else: incorrect += 1;

percent = round((correct / (correct + incorrect))*100,2)
print("Fitness: " + str(correct) + "/" + str(correct+incorrect) + " (" + str(percent) + "%)")
