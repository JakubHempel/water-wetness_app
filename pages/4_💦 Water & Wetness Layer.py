import streamlit as st
st.set_page_config(layout="wide", page_title="💦 Water and Wetness Layer | HydroPix 💧🛰️")

import geemap.foliumap as geemap
import gee_data as gd
from folium import plugins


# Load the water & wetness layer
@st.cache_data
def load_wetness_layer():
    return gd.get_water_wetness_layer()


# Page title
st.subheader("💦 Water & Wetness Layer")

with st.sidebar:
    st.markdown("""
    This layer represents the **frequency of water and wetness occurrence** from 2018 to 2025, derived using **Sentinel-1 radar imagery** and the **Otsu classification** method.

    The data provides insight into permanent and temporary wetness conditions across the study area.
    """)

# Define color palette (you can adjust to your preferred one)
palette = ['#1d3f94', '#3772ff', '#59c3ff', '#9cfff0']
vis_params = {
    'min': 1,
    'max': 4,
    'palette': palette
}

# Load layer
wetness_layer = load_wetness_layer()

legend_dict = {
    "Permanent Water": "#1d3f94",
    "Temporary Water": "#3772ff",
    "Permanent Wet": "#59c3ff",
    "Temporary Wet": "#9cfff0"
}


# Map setup
with st.spinner("Wait for the map ..."):
    Map = geemap.Map(center=[50.10, 19.95], zoom=10, control_scale=True, layer_ctrl=True)
    Map.addLayer(gd.aoi.style(color='red', fillColor='00000000', width=2), {},"AOI Boundary")
    Map.addLayer(wetness_layer.updateMask(wetness_layer.neq(0)), vis_params, "Water & Wetness Layer")

    # Tip
    st.markdown(
        "<div style='text-align: right; font-size: 0.85em; color: gray;'>"
        "💡 Toggle layers from the control panel in the top-right corner of the map."
        "</div>", unsafe_allow_html=True
    )

    Map.add_legend(title="Water & Wetness Layer", legend_dict=legend_dict)
    Map.to_streamlit(height=700)
