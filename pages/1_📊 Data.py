import streamlit as st
import geemap.foliumap as geemap
import gee_data as gd

st.set_page_config(layout="wide", page_title="📊 Data | HydroPix 💧🛰️")

st.markdown("## 📊 Data Sources")

st.markdown("""Here you can explore the satellite and environmental datasets used to build the **HydroPix Wetland Monitoring Application** 💧🛰️.""")

# Sentinel-1 Radar Data
st.markdown("### 🛰️ Sentinel-1 Radar Data")
st.markdown("""
- **Type**: Synthetic Aperture Radar (SAR)  
- **Frequency**: C-band (5.405 GHz)  
- **Resolution**: ~10 meters  
- **Provider**: [Copernicus Programme (ESA)](https://www.copernicus.eu/en)

Sentinel-1 radar imagery forms the **core of this project**.  
Thanks to its **all-weather** and **day-and-night** imaging capabilities, it enables **consistent monitoring** of wetlands and flooded areas.

Water detection primarily used **VV polarization** (Vertical transmit, Vertical receive) combined with **automated Otsu thresholding**.

**Temporal Coverage**:
- Flood Dynamics Analysis: **August – October 2024** (most active period around the flood)
- Wetland Monitoring: **January 2018 – March 2025**
""")

st.divider()

# Sentinel-2 Optical Data
st.markdown("### 🛰️ Sentinel-2 Optical Data")
st.markdown("""
- **Type**: Multispectral optical imagery  
- **Resolution**: 10–20 meters  
- **Provider**: [Copernicus Programme (ESA)](https://www.copernicus.eu/en)

Sentinel-2 imagery supplements the analysis by offering information on **water quality** and **surface conditions**.  
Spectral indices such as **AWEI**, **CGI**, **CDOM**, and **DOC** were calculated to assess water changes before and after flood events.

**Temporal Coverage**:
- Focused on **key dates around the 2024 flood event**
""")

st.divider()

# Meteorological Data
st.markdown("### ☔ Meteorological Data (IMGW-PIB)")
st.markdown("""
- **Source**: [Institute of Meteorology and Water Management (IMGW-PIB), Poland](https://imgw.pl/)  
- **Type**: Daily precipitation records

Precipitation data was used to **select satellite scenes** following intense rainfall events (>15 mm).  
This step improved the detection of **temporary water accumulation** and refined the **Water & Wetness Layer (WWL)** creation.
""")

st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    # Study Areas
    st.markdown("### 📍 Study Areas")
    st.markdown("""
    **Primary flood-affected regions**:
    - Kłodzko County
    - Ząbkowice Śląskie County
    - Nysa County
    
    **General monitoring region**:
    - Surroundings of Kraków
    - Selected parts of southwestern Poland
    
    These regions were chosen due to their **rich hydrological landscapes**, experiencing both **seasonal wetland dynamics** and **extreme flooding events**.
    """)

with col2:
    col_x, col_y = st.columns([1, 1])

    Map_aoi_flood = geemap.Map(center=[50.39, 17.05], zoom=9, basemap='OpenStreetMap.DE')
    Map_aoi_flood.addLayer(gd.aoi_flood, {}, "AOI - Flood")

    Map_aoi = geemap.Map(center=[50.10, 19.95], zoom=9)
    Map_aoi.addLayer(gd.aoi, {}, "AOI - Wetland Monitoring")

    with col_x:
        st.caption("Flood - AOI")
        Map_aoi_flood.to_streamlit(height=500)

    with col_y:
        st.caption("Wetland monitoring - AOI")
        Map_aoi.to_streamlit(height=500)

st.divider()

# Key Notes
st.markdown("### 🛠️ Key Notes on Data Usage")
st.markdown("""
- All satellite imagery was downloaded and processed in **Google Earth Engine**.  
- **Sentinel-2** preprocessing included cloud masking.  
- **Sentinel-1** preprocessing involved radiometric calibration and terrain correction.  
- **Multi-temporal analysis** ensured robust detection of wetland and water dynamics over time.
""")

st.warning("""💡 *Tip: Whenever you explore a result in the app, remember it is based on carefully selected and processed satellite and environmental data!*""")
