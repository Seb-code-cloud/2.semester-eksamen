import pandas as pd
import folium


df = pd.read_csv('Ladestander3214.csv')

m = folium.Map([55.68380104737004,12.585175041013349], zoom_start=12)

for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longtitude']], 
                  #popup=row['Location'],
                  icon=folium.Icon(icon='home')
                 ).add_to(m)
m
m.save('index.html')





