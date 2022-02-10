from numpy import random
import random as rand


def getTime(timeStamp):
    x = random.exponential(scale=1, size=(1, 1)) + timeStamp
    return x


def getPrice(num):
    if num == 1:
        return 5
    elif num == 2:
        return 50
    elif num == 3:
        return 100


def purchaseProb(option, timeStamp):
    timeStamp = getTime(timeStamp)
    return 1/timeStamp + 1/getPrice(option), timeStamp


def purchaseThreshold():
    randNum = rand.uniform(0.0, 1.0)
    return randNum


def main():
    times = []
    loops = []
    for index in range(1,4):
        sumTime = 0
        sumLoops = 0
        for i in range(15):
            inventory = 100
            timeStamp = 0
            while (inventory > 0):
                # buying
                purchProb, timeStamp = purchaseProb(index, timeStamp)
                if (purchProb > purchaseThreshold()):
                    amount = rand.uniform(1.0, 5.0)
                    inventory = inventory - amount
                    sumLoops += 1
            sumTime = sumTime + timeStamp
        avgTime = sumTime / 15
        avgLoops = sumLoops / 15
        times.append(avgTime)
        loops.append(avgLoops)
        print("The average time of index " ,index, " is " ,times[index - 1])
        print("The average number of loops until the inventory ends in index ", index, " is ",loops[index - 1])

if __name__ == '__main__':
    main()

