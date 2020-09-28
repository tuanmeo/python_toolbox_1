#1. IF, ELIF, ELSE
z = 7
if z % 2 == 0 : # True
    print('z is divisible by 2')
elif z % 3 == 0 :
    print('z is divisible by 3')
else :
    print('unknown')

#%%
# two variables as:
room = 'bed'
area = 14.0
# if room = kit --> looking around in the kitchen 
# elif == bed --> looking around in the bedroom
# looking around elsewhere

# if area > 15 --> big place! 
# elif > 10 --> medium size, nice!
# else pretty small
if room == 'kit' :
    print('looking around in the kitchen')
elif room == 'bet' :
    print('looking around in the bedroom')
else :
    print('looking around elsewhere')
if area > 15 :
    print('big place!')
elif area > 10 :
    print('medium size, nice!')
else :
    print('pretty small')
# %%

#2. Filtering pandas DataFrames
# import bric.csv
import pandas as pd
brics = pd.read_csv('/home/tuan_nguyen/Documents/Tuan_nguyen/PYTHON/Fundamental_Python/brics.csv', sep = ',')
brics_1 = brics[['country']]
brics_list = brics_1.values.tolist()
print(brics_list[0])

# %%
