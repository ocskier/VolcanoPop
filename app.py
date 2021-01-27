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
marker_data=volcano_data.loc[0: len(volcano_data) ,['LAT','LON','ELEV']]

volcano_map = folium.Map(location=[marker_data.mean()['LAT'],marker_data.mean()['LON']],zoom_start=5,tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

def correctColor(value):
    if value < 2000:
        return 'gray'
    elif value >= 2000 and value <= 3000:
        return 'red'
    else: 
        return 'blue'

for i in marker_data.index:
    lat = marker_data['LAT'][i]
    lon = marker_data['LON'][i]
    el = marker_data['ELEV'][i]
    html = """
    <div style="display: flex;width: 150px;flex-direction: column;">
        <h4 style="font-size: 2rem;">Volcano Info:</h4>
        <span style="font-size:1.2rem">
            Height: {height} m
        </span>
    </div>
    """.format(height=el)
    iframe = folium.IFrame(html=html, width=200, height=100)
    fg.add_child(folium.Marker(location=[lat,lon],popup=html,icon=folium.Icon(color=correctColor(int(el)),icon="fa-area-chart", prefix='fa')))
    volcano_map.add_child(fg)

fg.add_child(folium.GeoJson(data=(open('./world.json','r', encoding='utf-8-sig').read())))

volcano_map.save("./index.html")
