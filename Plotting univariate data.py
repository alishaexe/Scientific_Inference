import matplotlib.pyplot as plt
import numpy as np
import time
#%%

#First we want to make a Histogram
#We import our data

file_path = '/Users/alisha/Documents/Scientific_Inference/Data/Michelson.dat'
# the skiprows skips the first row with the header
mic = np.array(np.loadtxt(file_path, skiprows = 1))

#We can rathersimply make a histogram from
plt.hist(mic)
plt.show()
#We can specify the number of bins we want
plt.hist(mic, bins = 25, color = "orange")
#From this we see that the columns have smaller widths and there is more
#of them

#then as usual we can define axes labels etc
plt.xlabel("Velocity - 299,000 km/s")
plt.ylabel("Frequency")
plt.show()

#%%
#Now we can make a bar chart
file_path1 = '/Users/alisha/Documents/Scientific_Inference/Data/Rutherford.dat'
rut = np.array(np.loadtxt(file_path1, skiprows = 1))

x = rut[:,0]
y = rut[:,1]

plt.bar(x,y, width = 0.1, color = "green")
plt.xlabel("Rate (counts/interval)")
plt.ylabel("Frequency")
plt.show()

#%%
#Let's import the data
file_path = '/Users/alisha/Documents/Scientific_Inference/Data/Michelson.dat'
mic = np.array(np.loadtxt(file_path, skiprows = 1))

#Now we calculate the averages
light_mean = np.mean(mic)
light_median = np.median(mic)
print("The mean: ",light_mean)
print("The median: ", light_median)

#In order to find the mode we will need to use scipy
from scipy import stats as st
#We use the [0] because mode also returns the count and so if we just want
#the value of mode we use [0]
light_mode = st.mode(mic)[0]
print("The mode: ", light_mode)






















