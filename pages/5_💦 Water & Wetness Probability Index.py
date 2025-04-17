import streamlit as st

st.set_page_config(layout="wide", page_title="💦 Water and Wetness Probability Index | HydroPix 💧🛰️")

import geemap.foliumap as geemap
import gee_data as gd
from folium import plugins


# Load the water & wetness layer
@st.cache_data
def load_wwpi_layer():
    return gd.get_wwpi_layer()


# Page title
st.subheader("💦 Water & Wetness Probability Index")

with st.sidebar:
    st.markdown(""" TU NAPISAĆ COŚ O TEJ STRONIE !!! """)

# Define color palette (you can adjust to your preferred one)
palette = ['#fef0d9', '#fd8d3c', '#e34a33', '#253494', '#081d58']
vis_params = {
    'min': 1,
    'max': 5,
    'palette': palette
}

# Load layer
wwpi_layer = load_wwpi_layer()

# 💠 Add legend
legend_dict = {
    r"5 - 25% Wetness": "#fef0d9",
    r"26 - 50% Wetness": "#fd8d3c",
    r"51 - 75% Wetness": "#e34a33",
    r"76 - 99% Wetness": "#253494",
    r"100% Permanent Water": "#081d58"
}

# Map setup
with st.spinner("Wait for the map ..."):
    Map = geemap.Map(center=[50.10, 19.95], zoom=10, control_scale=True, layer_ctrl=True)
    Map.addLayer(gd.aoi.style(color='red', fillColor='00000000', width=2), {}, "AOI Boundary")
    Map.addLayer(wwpi_layer.updateMask(wwpi_layer.neq(0)), vis_params, "Water & Wetness Probability Index")

    # Tip
    st.markdown(
        "<div style='text-align: right; font-size: 0.85em; color: gray;'>"
        "💡 Toggle layers from the control panel in the top-right corner of the map."
        "</div>", unsafe_allow_html=True
    )

    Map.add_legend(title="Water & Wetness Probability Index", legend_dict=legend_dict)
    Map.to_streamlit(height=700)
