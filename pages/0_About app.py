import streamlit as st

st.set_page_config(layout="wide", page_title="About app | HydroPix 💧🛰️")

st.markdown("## 🌐 About HydroPix")

st.markdown("> *Visualizing and Monitoring Wetness – From Space to Understanding*")

st.markdown("""
**HydroPix** is an interactive geospatial application developed as part of a master's thesis focused on the **detection and monitoring of wetlands** and **flood dynamics** using **Sentinel-1 radar satellite imagery**.

Designed to support both **extreme flood events** (e.g., the 2024 flood) and **long-term hydrological changes**, HydroPix enables users to explore **temporal and spatial wetness patterns** across key regions.
""")

st.markdown("### 🛰️ Technology & Data")
st.markdown("""
- **Satellite Data**: Sentinel-1 radar imagery (2018–2025); Sentinel-1, Sentinel-2 (flood event)
- **Processing Platform**: [Google Earth Engine](https://earthengine.google.com)  
- **Python Tooling**: [geemap](https://geemap.org)  
- **Study Area**: *Kraków*, *Krakowski*, *Wielicki* counties and *Kłodzki*, *Nyski*, *Ząbkowicki* counties (flood event)
""")

st.markdown("### 🧠 Methodology")
st.markdown("""
The application implements an **adaptive Otsu thresholding algorithm** applied to Sentinel-1 backscatter data.  
This enables reliable **water surface detection under any weather conditions**.
""")

st.markdown("### 💧 Key Outputs")
st.markdown("""
- **💦 Water & Wetness Layer** – frequency of water occurrence across all observations  
- **💦 Water & Wetness Probability Index (WWPI)** – likelihood of water presence per pixel
""")

st.markdown("### 🌍 What You Can Do")
st.markdown("""
- 📊 Analyze **flood extent** across multiple timeframes  
- 🔄 Compare **before / after / post-flood** imagery  
- 🗓️ Observe **seasonal and long-term wetness trends**  
- 🗺️ Investigate water dynamics within **flood-prone areas**
""")

st.success("Use the sidebar to explore flood imagery, wetness layers, and probabilities across time.")

