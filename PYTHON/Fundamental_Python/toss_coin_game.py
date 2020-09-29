#%%
# toss game: 1 - tail, 0 for head
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails = [] #show numbers of tails for each 10 times tosses
# do the work 100 times of toss x times
for x in range(10000):
    tails = [0]
    # toss 10 times
    for x in range(10): 
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1]) # add the final toss count
print(final_tails)  
plt.hist(final_tails, bins = 10)
plt.show()
# %%
