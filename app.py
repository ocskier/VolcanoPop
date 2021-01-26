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
