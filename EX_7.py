import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

world_data = pd.read_csv("world_countries.csv")
india_states_data = pd.read_csv("india_states.csv")
india_districts_data = pd.read_csv("india_districts.csv")

world_map = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
)

world_data_geo = world_map.merge(
    world_data,
    how="left",
    left_on="NAME",
    right_on="Country"
)

fig, axs = plt.subplots(1, 3, figsize=(20, 6))

axs[0].set_title("World Countries Data")

world_data_geo.boundary.plot(
    ax=axs[0]
)

world_data_geo.plot(
    column="Value",
    ax=axs[0],
    legend=True,
    legend_kwds={
        "label": "Values by Country"
    },
    missing_kwds={
        "color": "lightgrey"
    }
)


axs[1].set_title("India States Data")

axs[1].bar(
    india_states_data["State"],
    india_states_data["Value"]
)

axs[1].tick_params(
    axis="x",
    rotation=90
)

axs[1].set_xlabel("States")
axs[1].set_ylabel("Value")

axs[2].set_title("India Districts Data")

axs[2].bar(
    india_districts_data["District"],
    india_districts_data["Value"]
)

axs[2].tick_params(
    axis="x",
    rotation=90
)

axs[2].set_xlabel("Districts")
axs[2].set_ylabel("Value")

plt.tight_layout()
plt.show()