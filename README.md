# HydroPix 💧🛰 - Wetland Monitoring Application
This repository contains the code and documentation for the **Wetland Monitoring Application**, developed as part of a **master's thesis project**.

The application enables monitoring of wetlands and flood events based on **Sentinel-1 radar satellite imagery**, complemented by **Sentinel-2 optical data** and **meteorological information**.

## 📑 Table of Contents

- [📚 About the Project](#-about-the-project)
- [🚀 Getting Started](#-getting-started)
- [🛰️ Data Sources](#️-data-sources)
- [🛠️ Technologies Used](#️-technologies-used)
- [🧭 How to Use the Application](#-how-to-use-the-application)
- [⚡ Important Notes](#-important-notes)
- [📄 License](#-license)

---

## 📚 About the Project

The project focuses on:

- Detecting **flooded and wetland areas** using **automated Otsu classification** on radar data.
- Analyzing **long-term wetland dynamics** from **2018 to 2025**.
- Creating two key geospatial products:
  - **Water & Wetness Layer (WWL)** – frequency of water occurrence.
  - **Water & Wetness Probability Index (WWPI)** – probability of water presence.
- Performing a **case study** on the **2024 flood in southwestern Poland**.

The application was built to visualize **spatial and temporal changes** in wetland ecosystems and demonstrate the **effectiveness of radar-based monitoring techniques**.

---

## 🚀 Getting Started

Users can explore:

- 🌊 **Flood analysis results** (Sentinel-1 and Sentinel-2 imagery)
- 🌿 **Long-term wetland monitoring products** (WWL and WWPI layers)
- 🗺️ **Interactive maps and charts**

---

## 🛰️ Data Sources

- **Sentinel-1 SAR Data** (Copernicus Programme, ESA)
- **Sentinel-2 Optical Data** (Copernicus Programme, ESA)
- **Meteorological Data** (IMGW-PIB, Poland)

---

## 🛠️ Technologies Used

- 🚀 **Google Earth Engine** – satellite data processing
- 🐍 **Python + geemap** – analysis, visualization, and data export
- 🛠️ **FME (Feature Manipulation Engine)** – automated workflows for data selection
- 🖥️ **Streamlit** – building the interactive web application

---

## 🧭 How to Use the Application

You can explore the Wetland Monitoring Application in two ways:

### 1. 🌐 Visit the Hosted Application (Recommended)

- Click the link below to access the fully operational web app (no installation required):

  ➡️ [**Launch Application**]()  
  *(Link will be updated once deployed.)*

---

### 2. 🖥️ Run Locally on Your Machine

If you prefer running the app locally, follow these steps:

#### a) Clone the repository:

```bash
git clone https://github.com/JakubHempel/water-wetness_app.git
cd your-repository-name
```

#### b) Create a new conda environment:

```bash
conda create -n wetlands-app python=3.10
conda activate wetlands-app
```

#### c) Install required packages:
```bash
pip install -r requirements.txt
```

#### d) Run the Streamlit app:
```bash
streamlit run 📃_Home.py
```

---

## ⚡ Important Notes

- ✅ You must have a valid **Google Earth Engine (GEE)** account.
  - If running locally for the first time, execute authentication:
    ```python
    import ee
    ee.Authenticate()
    ee.Initialize()
    ```

- ✅ Ensure you are using **Python 3.10** or newer for full compatibility.

- ✅ The app entry point is **📃_Home.py** — it automatically manages multipage navigation inside the Streamlit app.

- ✅ Recommended to use **Conda environments** for clean dependency management.

- ✅ Internet access is required while using the app (for Google Earth Engine API calls and basemaps).

- ✅ If errors occur during first launch (Earth Engine credentials or token issues), re-authenticate using:
    ```bash
    earthengine authenticate
    ```

---

## 📄 License

This project is licensed for **educational and research purposes**.  
Please **cite the repository** if you use the application in your work.

---

## 🌍 Enjoy exploring the dynamics of wetlands from space! 💧🛰
