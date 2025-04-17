import streamlit as st

st.set_page_config(layout="wide", page_title="🧠 Methodology | HydroPix 💧🛰️")

st.markdown("## 🧠 Methodology")

st.markdown("""
Here, you can discover how **satellite data** was transformed into **meaningful insights** for **wetland monitoring** and **flood analysis**.
""")

st.markdown("### 🔍 Key Methodological Steps")

st.markdown("""
**1. Radar-Based Water Detection**  
- Primary method based on **Sentinel-1 radar imagery**.  
- Radar penetrates clouds and operates day & night — perfect for **consistent monitoring** during extreme events.
- **Detection workflow**:
  - Process **VV polarization** backscatter.
  - Apply the **Otsu thresholding** algorithm to separate water from non-water surfaces.
  - Generate **binary water masks** for each scene.
""")

st.markdown("""
**2. Spectral Index Analysis (Optical Data)**  
- Complementary analysis using **Sentinel-2 optical imagery**.
- Key spectral indices:
  - **AWEI** (Automated Water Extraction Index)
  - **CGI** (Chlorophyll Green Index)
  - **CDOM** (Colored Dissolved Organic Matter)
  - **DOC** (Dissolved Organic Carbon)
- These indices helped analyze **pre- and post-flood** conditions during the **2024 flood event**.
""")

st.markdown("""
**3. Multi-Temporal Aggregation**  
- Long-term wetland monitoring (2018–2025).
- Creation of two important products:
  - **Water & Wetness Layer (WWL)** – frequency of water occurrence.
  - **Water & Wetness Probability Index (WWPI)** – likelihood of water presence over time.
- Each classified "water" pixel contributed to a **comprehensive wetland dynamics map**.
""")

st.divider()

st.markdown("### ⚙️ Technologies Behind the Scenes")

st.markdown("""
- 🚀 **Google Earth Engine (GEE)**  
  - Cloud-based platform for accessing, processing, and analyzing satellite imagery.  
  - All classifications and aggregations performed at scale.
- 🐍 **Python + geemap**  
  - Python scripting environment using the **geemap** library.  
  - Enabled interactive mapping, custom analyses, and exports.
- 🛠️ **FME (Feature Manipulation Engine)**  
  - Automated workflows for selecting satellite scenes based on **meteorological events** (e.g., rainfall > 15 mm).
- 🛰️ **Sentinel-1 and Sentinel-2 Data**  
  - Satellite data sourced from the **Copernicus Open Access Hub** and processed entirely within GEE.
""")

st.success("""
💡 *Tip: The methodologies and technologies were carefully chosen to ensure **fast, reliable, and repeatable monitoring** — even when clouds or extreme weather made traditional optical observations impossible.*
""")
