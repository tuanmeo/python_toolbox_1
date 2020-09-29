#%%
#.toss the dice for step up or down.
#. <= 2 -- step -1, <=5 -- step + 1, =6 roll again + no of 2nd roll
#. care of negative step (impossible move)
#. care of ration for slipe 

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
all_walks = []
#simulate random walk 10 times
for i in range(500):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0,step -1)
        elif dice <=5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        # implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)
print(all_walks)
# %%
# visualize the result
# convert to numpy array
np_aw = np.array(all_walks)
plt.plot(np_aw)
plt.show()
plt.clf()

#transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)
plt.plot(np_aw_t)
plt.show()
# %%
# select the last row from np_aw_t: ends
#print(np_aw)
#print(np_aw_t)
ends = np_aw_t[-1,:]
print(ends)
plt.hist(ends)
plt.show()
# %%
# cal the possibility of win the game (over 60 floors)
# ends contains 500 integers of end point of a random walk
print(type(ends))
# %%
num_steps = np.count_nonzero(ends >= 60)
print(num_steps / len(ends))
# %%
