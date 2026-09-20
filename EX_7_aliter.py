import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

world_map = gpd.read_file("world_map.geojson")
india_map = gpd.read_file("india_states.geojson")

world_data = pd.read_csv("world_countries.csv")
india_data = pd.read_csv("india_states.csv")

world_map_geo = world_map.merge(world_data, how='left', left_on='SOVEREIGNT', right_on='Country')
india_map_geo = india_map.merge(india_data, how='left', left_on="name", right_on='State')

fig,axs = plt.subplots(1,2)

world_map_geo.boundary.plot(ax=axs[0])
world_map_geo.plot(column = 'Value', ax=axs[0])


india_map_geo.boundary.plot(ax=axs[1])
india_map_geo.plot(column = 'Value', ax=axs[1], legend=True)

plt.show()

