from numpy import random
import random as rand
# import matplotlib.pyplot as plt

decreasingPrice = None
# The time have an exponential distribution, and as long as the simulation is running it increase
def getTime(timeStamp):
    x = random.exponential(scale=1, size=(1, 1)) + timeStamp
    return x

# Three options for prices, the last one is price that decreasing according to the time
def getPrice(num):
    if num == 1:
        return 2
    elif num == 2:
        return 3
    elif num == 3:
        global decreasingPrice
        decreasingPrice = 0.95 * decreasingPrice
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
    # price1 = []
    # price2 = []
    # price3 = []
    # Iterating the prices
    for index in range(1,4):
        sumTime = 0
        temp = []
        # Calculating the average from 15 loops
        for i in range(15):
            inventory = 10000
            timeStamp = 0
            global decreasingPrice
            decreasingPrice = 5
            # Simulating the purchasing until inventory is over
            while (inventory > 0):
                purchProb, timeStamp = purchaseProb(index, timeStamp)
                if (purchProb > purchaseThreshold()):
                    # purchasing
                    amount = rand.uniform(1.0, 5.0) # Random amount of inventory
                    inventory = inventory - amount
            sumTime = sumTime + timeStamp
            temp.append(timeStamp[0][0])
        # Calculating the average of all the loops
        avgTime = sumTime / 15
        print("The average time of index ",index," is ",avgTime[0][0])
        if index == 1:
            price1 = temp
        elif index == 2:
            price2 = temp
        elif index == 3:
            price3 = temp
    # fig, ax = plt.subplots()
    # print("price 1" , price1)
    # print("price 2", price2)
    # print("price 3", price3)
    # plt.plot(price1, label="price1")
    # plt.plot(price2, label="price2")
    # plt.plot(price3, label="price3")
    # ax.legend()
    # plt.show()


if __name__ == '__main__':
    main()

