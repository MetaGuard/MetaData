import csv
import numpy as np
import matplotlib.pyplot as plt
import statistics
from numpy import array
from numpy.linalg.linalg import pinv
from scipy.spatial.distance import euclidean
import geopy.distance

N=2
us_east_1_avg = []
us_east_2_avg = []
us_west_1_avg = []
us_west_2_avg = []
ca_central_1_avg = []
dist = []

for i in range (1,N+1):
    us_east_1 = []
    us_east_2 = []
    us_west_1 = []
    us_west_2 = []
    ca_central_1 = []
    with open('../data/' + str(i) + '.txt') as file:
        for line in file:
            parts = line.split(': ')
            if (parts[0] == "us-east-1"): us_east_1.append(int(parts[1]))
            if (parts[0] == "us-east-2"): us_east_2.append(int(parts[1]))
            if (parts[0] == "us-west-1"): us_west_1.append(int(parts[1]))
            if (parts[0] == "us-west-2"): us_west_2.append(int(parts[1]))
            if (parts[0] == "ca-central-1"): ca_central_1.append(int(parts[1]))
    us_east_1_avg.append(statistics.median(us_east_1))
    us_east_2_avg.append(statistics.median(us_east_2))
    us_west_1_avg.append(statistics.median(us_west_1))
    us_west_2_avg.append(statistics.median(us_west_2))
    ca_central_1_avg.append(statistics.median(ca_central_1))

def transpose_1D(M):
    return M.reshape(len(M), 1)

def multilaterate(anchor_positions, distances):
    N = anchor_positions.shape[0]
    A = np.vstack([np.ones(N), -2 * anchor_positions[:, 0], -2 * anchor_positions[:, 1]]).T
    B = distances ** 2 - anchor_positions[:, 0] ** 2 - anchor_positions[:, 1] ** 2
    X = np.dot(A.T, A)
    xp = np.dot(np.dot(np.linalg.inv(X), A.T), B)
    return xp[1:]

for i in range(0,N):
    d = 0.496
    loc = multilaterate(np.array([
        [40.093655163828615, -82.75021108220088],
        [37.413769057554184, -121.97182817337978],
        [45.921586440357295, -119.26565997256668],
    ]), np.array([
        (us_east_2_avg[i]-2)*d,
        (us_west_1_avg[i]-2)*d,
        (us_west_2_avg[i]-2)*d,
    ]))
    dist.append(geopy.distance.geodesic((loc[0], loc[1]), (37.87680775, -122.2563914)).km)

print('Accuracy within 400km:', len([d for d in dist if d <= 400]) / N)
print('Accuracy within 500km:', len([d for d in dist if d <= 500]) / N)
