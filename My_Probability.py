#%%
import numpy as np
def myBet(ite_times, amount):
    amount_to_use = amount * 0.15
    for _ in range(ite_times):
        if amount <= 0:
            break
        my_var = np.random.randint(0, 101)
        if my_var >= 51:
            amount = amount - amount_to_use
            amount_to_use = amount * 0.15

        elif my_var <= 49:
            amount = amount + (amount_to_use * 2)
            amount_to_use = amount * 0.15
    return round(amount)
    

def myBet2(ite_times, amount):
    amount_to_use = amount * 0.25
    for _ in range(ite_times):
        if amount <= 0:
            break
        my_var = np.random.randint(0, 101)
        if my_var >= 51:
            amount = amount - amount_to_use
            amount_to_use = amount * 0.25

        elif my_var <= 49:
            amount = amount + (amount_to_use * 2)
            amount_to_use = amount * 0.25
    return round(amount)

my_arr = []
my_arr2 = []
for item in range(101):
    my_arr.append(myBet(100, 100))
    my_arr2.append(myBet2(100, 100))

max1 = 1
min1 = 999999
count1 = 0
for item in my_arr:
    if item > 100:
        count1 +=1
    if max1 < item:
        max1 = item
    if min1 > item:
        min1 = item

print(max1, min1, count1)

max2 = 1
min2 = 999999
count2 = 0
for item in my_arr2:
    if item > 100:
        count2 +=1
    if max2 < item:
        max2 = item
    if min2 > item:
        min2 = item

print(max2, min2, count2)



#%%

def times_go(numTimes, massa):
    for _ in range(numTimes):
        actual_massa = massa * 0.10
        massa = massa - actual_massa
        print(massa)

times_go(17, 100)


#%%