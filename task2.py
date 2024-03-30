# Task #2: Statistics

import pandas as pd
from pathlib import Path

# gets file path in case code run not in immediate directory
scriptDirectory = Path(__file__).resolve().parent
inputFilename = "BostonHousing.csv"
inputFilePath = scriptDirectory / inputFilename

# pandas data frame, read from BostonHousing.csv
df = pd.read_csv(inputFilePath)
# medv takes items only from the 'medv' column, Series obj
medv = df['medv']

def max(data) -> float:
    '''
    Gets the largest value in dataset column
    '''
    max = data[0]
    for i in data:
        max = i if i > max else max
    return max

def min(data) -> float:
    '''
    Gets the minimum value in dataset column
    '''
    min = data[0]
    for i in data:
        min = i if i < min else min
    return min

def range(data) -> float:
    '''
    Gets the range of dataset column
    '''
    min = data[0]
    max = data[0]
    for i in data:
        min = i if i < min else min
        max = i if i > max else max
    return max - min


def mean(data) -> float:
    '''
    Gets the average value from dataset column
    '''
    total = 0
    dataLen = len(data)
    for i in data:
        total += i
    return total / dataLen

def mode(data) -> list:
    '''
    Gets the most common value(s) from dataset column
    '''
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
    '''
    Calculates variance from dataset column
    '''
    avg = mean(data)
    n = len(data)
    numerator = 0
    for i in data:
        numerator += (i - avg) ** 2
    return numerator / n

def standardDeviation(data) -> float:
    '''
    Calculates the standard deviation from dataset column
    '''
    var = variance(data)
    return var ** .5

def mergesort(data) -> list:
    '''
    Sorts dataset column from least to greatest
    '''
    arr = list(data)
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        left = mergesort(left)  # Recursively sort the left half
        right = mergesort(right)  # Recursively sort the right half

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Check for any remaining elements in left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Check for any remaining elements in right
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def percentile1(data, perc: float):
    '''
    Calculates percentile using Method 1: Greater than
    '''
    index = int(perc * len(data)) + 1
    return data[index]

def percentile2(data, perc: float):
    '''
    Calculates percentile using Method 2: Greater than or Equal to
    '''
    index = int(perc * len(data)) + 1
    return data[index-1]

def percentile3(data, perc: float):
    '''
    Calculates percentile using Method 3: Using an Interpolation Approach
    '''
    rank = perc * (len(data) + 1)
    if rank == int(rank):
        return data[rank-1]
    else:
        lowIndex = int(rank) - 1
        highIndex = lowIndex + 1
        adder = (data[highIndex] - data[lowIndex]) * perc
        return data[lowIndex] + adder

# main method
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