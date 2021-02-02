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
marker_data=volcano_data.loc[0: len(volcano_data) ,['LAT','LON','ELEV','NAME']]

volcano_map = folium.Map(location=[marker_data.mean()['LAT'],marker_data.mean()['LON']],zoom_start=4,tiles="Stamen Terrain")

fg1 = folium.FeatureGroup(name="Volcanoes")

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
    name = marker_data['NAME'][i]

    html = """
    <div style="display: flex;width: 150px;flex-direction: column;">
        <h4 style="font-size: 1.5rem;">Mt. {name}</h4>
        <span style="font-size:1.2rem">
            Height: {height} m
        </span>
    </div>
    """.format(height=el,name=name)

    iframe = folium.IFrame(html=html, width=200, height=100)
    fg1.add_child(folium.Marker(location=[lat,lon],popup=html,icon=folium.Icon(color=correctColor(int(el)),icon="fa-area-chart", prefix='fa')))
    volcano_map.add_child(fg1)

fg2 = folium.FeatureGroup(name='Population')
fg2.add_child(folium.GeoJson(data=(open('./world.json','r', encoding='utf-8-sig').read()),style_function=lambda x: {'fillOpacity':0.3,'fillColor': 'yellow' if x['properties']['POP2005'] <= 10000000 else 'darkgreen' if x['properties']['POP2005'] > 10000000 and x['properties']['POP2005'] <= 300000000 else 'blue'}),)

volcano_map.add_child(fg1)
volcano_map.add_child(fg2)
volcano_map.add_child(folium.LayerControl())

volcano_map.save("./index.html")
