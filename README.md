# Optimization-Of-Potato-Cost-Lotringer

##  Introduction to the problem and presentation of its complexity:
Many businesses find it difficult to maintain fixed profits and even maximize their income according to the set prices in the market. <br/>
Because of this, many places in the world try to predict the optimal price for their goods.
As part of our work, we will try to optimize the above forecasting process at the "Lotteringer Brothers" packing house.  <br/>
The Lotringer packing house is located in Moshav Givat - Han, and they pack two types of potatoes - red and white. <br/>
The income of the packing house is affected by the sale of the goods only, while its expenses are affected by number of factors,
some of which are constant and some of them change.
We will review all the factors that affect this in our work, and then through simulation, we will examine options
Variation in the pricing of the potatoes, and we will also examine how the difference in price affects the duration of the sale.

## The purpose of the simulation
This tool allows us to simulate different scenarios that exist in the real world under different constraints.
In our work, we will illustrate how the price of potatoes affects the amount of time it takes for the commodity to be sold.
For this, we will build equations for each scenario and compare different prices.


## Defining the model
The model symbolizes the following scenarios:
1. The price of potatoes is 2NIS per kilo
2. The price of potatoes is 3NIS per kilo
3. The price of potatoes starts at NIS 5 per kilo, and decreases depending on the time
under the following assumptions:
1. The time between customer and customer is exponentially distributed with 1𝝀 =
2. The price of potatoes decreases by 5% in a fixed period of time (to be expanded later), as part of scenario number 3
3. The probability of buying the potatoes by a particular customer is inversely related to the time that passes and the price
the potatoes
4. The purchase threshold of a certain customer is distributed uniformly (to be expanded later)
5. The size of the stock is 10,000 kg of potatoes per year

## Decision variables:
the price of potatoes
In the simulation, prices are tested in the range between 2 NIS and 5 NIS. These prices make sense because the total is calculated
The fixed and variable expenses of the packing house is 525.1 NIS per kg.
sub-objective:
• Cost of X packaging materials
• The cost of the raw material of the potatoes Y
• Transportation costs W
• Sorting and packing P
• Cost of U employees
• Fixed expenses V
• Electricity cost for the T machines
• The cost of maintaining the S machines
• Q water
Below is the cost calculation:
𝐶𝑜𝑠𝑡 𝑝𝑒𝑟 𝐾𝑔 = 𝑋 + 𝑌 + 𝑊 + 𝑃 + 𝑈 + 𝑉 + 𝑇 + 𝑆 + 𝑄 =
= 0.1 + 0.9 + 0.18 + 0.07 + 0.1 + 0.05 + 0.005 + 0.07 + 0.05 = 1.525

## Planning the simulation
The simulation simulates a situation where customers arrive one after the other and purchase the potatoes, as long as there is stock.
We ran the simulation above 15 times on every possible price, to reach an average result that would give an answer
More reliable and trustworthy than a single run.
The simulation consists of five stages:

<br/>

1. Sampling a time function - in order to simulate the arrival times of customers at the packing house,
we sample a time function that is exponentially distributed, as is customary in simulations. <br/>
The samples are growing and symbolizing the time that passes between the arrival of customers. <br/>
Calculating the probability of buying - in order to symbolize the chance that the customer will buy the potatoes, <br/>
we use a probability calculation function that quantifies the chance of buying depends on the price of potatoes and the time that has passed.  <br/>
The function is constructed in such a way that as the higher the price, the smaller the chance to buy,<br/>
and in addition, as time passes, the chance to buy decreases as well because the goods are less fresh. The function results are in the range [1,0].<br/>
f = 1/price + 1/time<br/>
2. Setting a price - in order to compare the simulation between the effect of different prices, we set different prices in the reasonable price range for the sale price according to the fixed and variable expenses we have.
3. The purchase threshold lottery - in order to highlight an option in which the customer is debating whether to buy the potatoes,<br/>
We drew a buy threshold with a uniform distribution in the range [1,0]. Therefore, if the probability of buying is greater than the threshold,<br/>
So the customer buys the potatoes, and if it's small, he doesn't buy.<br/>
4. Lottery of purchase quantity - in order to select a different purchase quantity between each customer, we drew quantities in a distribution<br/>
uniform in the range [5,1.]<br/>
The decisions regarding the aforementioned functions, the various distributions chosen and the ranges of the functions were made in coordination
with Amir Alalof.* <br/> 

![a](https://github.com/sapirhender123/Optimization-Of-Potato-Cost-Lotringer/blob/master/PotatoCostSimulation.PNG)
