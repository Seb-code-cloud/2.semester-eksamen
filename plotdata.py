import matplotlib.pyplot as plt
import pandas as pd 




plt.style.use('seaborn')  # to get seaborn scatter plot

# read the csv file to extract data

data = pd.read_csv('Ladestander3214.csv')
Latitude = data['Latitude']
Longtitude = data['Longtitude']


plt.scatter(Latitude, Longtitude, s=100, alpha=0.6, edgecolor='black', linewidth=1)

plt.title('Charging stations')
plt.xlabel('Latitude')
plt.ylabel('Longtitude')

plt.tight_layout()
plt.show()






