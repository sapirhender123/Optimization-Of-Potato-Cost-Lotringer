from numpy import random
import random as rand

decreasingPrice = 10
# The time have an exponential distribution, and as long as the simulation is running it increase
def getTime(timeStamp):
    x = random.exponential(scale=1, size=(1, 1)) + timeStamp
    return x

# Three options for prices, the last one is price that decreasing according to the time
def getPrice(num):
    if num == 1:
        return 5
    elif num == 2:
        return 8
    elif num == 3:
        global decreasingPrice
        decreasingPrice = 0.99 * decreasingPrice
        return decreasingPrice

# Calculate the probability of customer to purchase
def purchaseProb(option, timeStamp):
    timeStamp = getTime(timeStamp)
    return 1/timeStamp + 1/getPrice(option), timeStamp

# Uniform value that represent a threshold which above it customer is purchasing
def purchaseThreshold():
    randNum = rand.uniform(0.0, 1.0)
    return randNum


def main():
    times = []
    # Iterating the prices
    for index in range(1,4):
        sumTime = 0
        # Calculating the average from 15 loops
        for i in range(15):
            inventory = 100
            timeStamp = 0
            global decreasingPrice
            decreasingPrice = 10
            # Simulating the purchasing until inventory is over
            while (inventory > 0):
                purchProb, timeStamp = purchaseProb(index, timeStamp)
                if (purchProb > purchaseThreshold()):
                    # purchasing
                    amount = rand.uniform(1.0, 5.0) # Random amount of inventory
                    inventory = inventory - amount
            sumTime = sumTime + timeStamp
        # Calculating the average of all the loops
        avgTime = sumTime / 15
        times.append(avgTime)
        print("The average time of index ",index," is ",times[index - 1])


if __name__ == '__main__':
    main()

