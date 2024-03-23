# Task #2: Statistics

import pandas as pd
from pathlib import Path

scriptDirectory = Path(__file__).resolve().parent
inputFilename = "BostonHousing.csv"
inputFilePath = scriptDirectory / inputFilename
# pandas data frame, read from BostonHousing.csv
df = pd.read_csv(inputFilePath)
# medv takes items only from the 'medv' column
medv = df['medv']

def max(data) -> float:
    max = data[0]
    for i in data:
        max = i if i > max else max
    return max

def min(data) -> float:
    min = data[0]
    for i in data:
        min = i if i < min else min
    return min

def range(data) -> float:
    min = data[0]
    max = data[0]
    for i in data:
        min = i if i < min else min
        max = i if i > max else max
    return max - min


def mean(data) -> float:
    total = 0
    dataLen = len(data)
    for i in data:
        total += i
    return total / dataLen

def mode(data) -> list:
    frequency = {}
    for i in data:
        if i in frequency.keys():
            frequency[i] += 1
        else:
            frequency[i] = 1
    freqValues = list(frequency.values()) # list
    maxValue = max(freqValues)
    mostCommonKeys = [key for key, value in frequency.items() if value == maxValue]
    return mostCommonKeys

def variance(data) -> float:
    avg = mean(data)
    n = len(data)
    numerator = 0
    for i in data:
        numerator += (i - avg) ** 2
    return numerator / n

def standardDeviation(data) -> float:
    var = variance(data)
    return var ** .5

def mergesort(data) -> list:
    arr = list(data)
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        left_half = mergesort(left_half)  # Recursively sort the left half
        right_half = mergesort(right_half)  # Recursively sort the right half

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check for any remaining elements in right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def percentile1(data, perc: float):
    # greater than
    index = int(perc * len(data)) + 1
    return data[index]

def percentile2(data, perc: float):
    # greater than or equal to
    index = int(perc * len(data)) + 1
    return data[index-1]

def percentile3(data, perc: float):
    # using an interpolation approach
    rank = perc * (len(data) + 1)
    if rank == int(rank):
        return data[rank-1]
    else:
        lowIndex = int(rank) - 1
        highIndex = lowIndex + 1
        adder = (data[highIndex] - data[lowIndex]) * perc
        return data[lowIndex] + adder

def main():
    print("Task #2 - Statistics\n")
    print(f"max: {max(medv)}")
    print(f"min: {min(medv)}")
    print(f"range: {range(medv)}")
    print(f"mean: {mean(medv):.2f}")
    print(f"mode: {mode(medv)}")
    print(f"variance: {variance(medv):.2f}")
    print(f"standard deviation: {standardDeviation(medv):.2f}\n")
    
    sortedData = mergesort(medv)
    m140 = percentile1(sortedData, .40)
    m240 = percentile2(sortedData, .40)
    m340 = percentile3(sortedData, .40)
    m180 = percentile1(sortedData, .80)
    m280 = percentile2(sortedData, .80)
    m380 = percentile3(sortedData, .80)

    print(f"Method 1 (40th perceentile): {m140:.2f}")
    print(f"Method 2 (40th perceentile): {m240:.2f}")
    print(f"Method 3 (40th perceentile): {m340:.2f}\n")
    print(f"Method 1 (80th perceentile): {m180:.2f}")
    print(f"Method 2 (80th perceentile): {m280:.2f}")
    print(f"Method 3 (80th perceentile): {m380:.2f}")

if __name__ == "__main__":
    main()