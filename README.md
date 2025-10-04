**Purpose**
This small OSINT project demonstrates practical data gathering and analysis using public geospatial sources (OpenStreetMap). It shows:
- How to query public map data (Overpass API).
- How to extract and save results for quick analysis (CSV).
- An anonymized case study that demonstrates reasoning and redaction.

**Files**
- `overpass_query.py` — Python script that queries OSM for points-of-interest (POI) within a bounding box and writes CSV.
- `OSINT_case_study.md` — a short, anonymized OSINT case study analyzing open data (no private/personal info).
- `requirements.txt` — Python dependencies.

**Quick demo (run locally)**
1. Install Python 3.8+.
2. Create venv and install deps:
   ```
   python -m venv venv
   source venv/bin/activate    # macOS / Linux
   venv\Scripts\activate       # Windows
   pip install -r requirements.txt
   ```
3. Run example query:
   ```
   python overpass_query.py --min-lat 31.76 --min-lon 35.18 --max-lat 31.78 --max-lon 35.20 --tag cafe
   ```
   This queries OSM for nodes/ways with tag `cafe` inside the bounding box and writes `results.csv`.

**Ethics & Safety**
- This project uses **public** data only (OpenStreetMap). Do not use it to target private individuals.
- Redact any personal data in case studies. Use this as a portfolio piece to show method and reasoning.

**License**
MIT — use as a demonstration of capability.
