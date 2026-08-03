import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import mplcursors

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("earthquakes_2023_global_2.csv")

# Remove rows with missing coordinates
df = df.dropna(subset=["latitude", "longitude", "mag", "depth"])

# -----------------------------
# Create Figure
# -----------------------------
plt.figure(figsize=(14,8))

# Create World Map
m = Basemap(
    projection='mill',
    llcrnrlat=-60,
    urcrnrlat=80,
    llcrnrlon=-180,
    urcrnrlon=180,
    resolution='c'
)

# Draw map features
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color='lightgreen', lake_color='lightblue')
m.drawmapboundary(fill_color='lightblue')

# Convert latitude and longitude
x, y = m(df["longitude"].values,
         df["latitude"].values)

# -----------------------------
# Scatter Plot
# -----------------------------
scatter = plt.scatter(
    x,
    y,
    c=df["depth"],              # Color = depth
    s=df["mag"]*20,             # Size = magnitude
    cmap="hot",
    alpha=0.7
)

# Color Bar
cbar = plt.colorbar(scatter)
cbar.set_label("Depth (km)")

plt.title("Earthquake Locations on World Map")

# -----------------------------
# Mouse Hover Information
# -----------------------------
cursor = mplcursors.cursor(scatter, hover=True)

@cursor.connect("add")
def on_add(sel):

    index = sel.index

    text = f"""
Place : {df.iloc[index]['place']}
Magnitude : {df.iloc[index]['mag']}
Depth : {df.iloc[index]['depth']} km
Latitude : {df.iloc[index]['latitude']}
Longitude : {df.iloc[index]['longitude']}
"""

    sel.annotation.set_text(text)

plt.show()