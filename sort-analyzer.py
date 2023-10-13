# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])

# Bubble sort function
def bubbleSort(anArray):
    #number of passes
    for numCompare in range(len(anArray) - 1):
       #compare adjacent numbers
       for  i in range(len(anArray) - numCompare - 1):
           if (anArray[i] > anArray[i + 1]):
               anArray[i], anArray[i + 1] = anArray[i + 1], anArray[i]
    return anArray

# Selection sort function
def selectionSort(anArray):
    for fs in range(len(anArray) - 1):
        minpos = fs
        for i in range(fs + 1, len(anArray)):
            if anArray[i] < anArray[minpos]:
                minpos = i
        #swap positions        
        anArray[fs], anArray[minpos] = anArray[minpos], anArray[fs] 
    return anArray

# Insertion sort function
def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insertVal = anArray[i]
        insPos = i
        while insPos >= 1 and anArray[insPos - 1] > insertVal:
            anArray[insPos] = anArray[insPos - 1]
            insPos -= 1
        anArray[insPos] = insertVal
    return anArray

# Time output string function
def timeFunction(sortFunction, anArray):
    startTime = time.time()
    sortFunction(anArray)
    endTime = time.time()
    return endTime - startTime

# Test bubble sort
# print(f"Bubble Sort Random Data: {timeFunction(bubbleSort, randomData)} seconds")
# print(f"Bubble Sort Reversed Data: {timeFunction(bubbleSort, reversedData)} seconds")
# print(f"Bubble Sort Nearly Sorted Data: {timeFunction(bubbleSort, nearlySortedData)} seconds")
# print(f"Bubble Sort Few Unique Data: {timeFunction(bubbleSort, fewUniqueData)} seconds")

# Test selection sort
print(f"Selection Sort Random Data: {timeFunction(selectionSort, randomData)} seconds")
print(f"Selection Sort Reversed Data: {timeFunction(selectionSort, reversedData)} seconds")
print(f"Selection Sort Nearly Sorted Data: {timeFunction(selectionSort, nearlySortedData)} seconds")
print(f"Selection Sort Few Unique Data: {timeFunction(selectionSort, fewUniqueData)} seconds")


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
