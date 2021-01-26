import settings
import os
import mysql.connector
import folium
import pandas

# connection = mysql.connector.connect(
#     user = "root",
#     password = os.getenv("SQL_PWD"),
#     host = 'localhost',
#     database = "db"
# )

volcano_data=pandas.read_csv('./Volcanoes.txt')
marker_data=volcano_data.loc[0: len(volcano_data) ,'LAT':'LON']
print(marker_data)

volcano_map = folium.Map(location=[35.7796,-78.6382],zoom_start=6,tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for i in marker_data.index:
    fg.add_child(folium.Marker(location=[marker_data['LAT'][i],marker_data['LON'][i]],popup="Hi I am a Marker",icon=folium.Icon(color="blue")))
volcano_map.add_child(fg)

volcano_map.save("./Map.html")
