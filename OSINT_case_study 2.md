# OSINT Case Study — Anonymized (Demonstration)

**Objective (example):**  
Demonstrate how public map data and open imagery can be used to build situational awareness for a small area. This is purely a technical demonstration; all names and sensitive details are redacted.

**Scope:**  
- Area: small 2km × 2km bounding box (coordinates anonymized).  
- Source: OpenStreetMap (Overpass API), publicly available satellite imagery.

**Steps performed**
1. Queried OpenStreetMap for points of interest (POIs): `amenity=cafe`, `amenity=bakery`, `highway=traffic_signals`, `building=yes`.  
2. Downloaded the results and inspected coordinates and tags.  
3. Exported to CSV and visualized on QGIS (screenshot captured).  
4. Cross-checked the timestamps/last edit on OSM elements to evaluate freshness.

**Findings (example, redacted)**
- Concentration of commercial POIs along the main road — indicates foot traffic and local hub.
- Recent edits (within last 6 months) to several POIs suggests active changes (construction/renovation).
- Two clusters of parking/POIs are consistent with likely logistic access points.

**Conclusions**
- Public map data can quickly identify local hubs and logistical nodes.
- For operational use, this should be combined with verified imagery and field confirmation.
- No personal data or private identifying info was used or recorded.

**Notes**
- All data sources are public. This case study demonstrates method and care in redaction.
