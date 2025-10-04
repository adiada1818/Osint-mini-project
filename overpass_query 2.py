#!/usr/bin/env python3
overpass_query.py
Simple script to query OpenStreetMap Overpass API for POI tags inside a bounding box
and save results to CSV.

Usage example:
python overpass_query.py --min-lat 31.76 --min-lon 35.18 --max-lat 31.78 --max-lon 35.20 --tag cafe

Note: This uses public OpenStreetMap data. Do not use to collect private/personal data.

import argparse
import requests
import pandas as pd

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

def build_query(min_lat, min_lon, max_lat, max_lon, tag):
    bbox = f"{min_lat},{min_lon},{max_lat},{max_lon}"
    if "=" in tag:
        key, val = tag.split("=", 1)
        q = f'''
        [out:json][timeout:25];
        (
          node["{key}"="{val}"]({bbox});
          way["{key}"="{val}"]({bbox});
          relation["{key}"="{val}"]({bbox});
        );
        out center;
        '''
    else:
        q = f'''
        [out:json][timeout:25];
        (
          node["{tag}"]({bbox});
          way["{tag}"]({bbox});
          relation["{tag}"]({bbox});
        );
        out center;
        '''
    return q

def run_query(query):
    headers = {"User-Agent": "OSINT-mini-project/1.0 (+https://github.com/yourname)"}
    resp = requests.post(OVERPASS_URL, data={"data": query}, headers=headers)
    resp.raise_for_status()
    return resp.json()

def parse_elements(data):
    rows = []
    for el in data.get("elements", []):
        el_type = el.get("type")
        el_id = el.get("id")
        lat = el.get("lat")
        lon = el.get("lon")
        if lat is None or lon is None:
            center = el.get("center")
            if center:
                lat = center.get("lat")
                lon = center.get("lon")
        tags = el.get("tags") or {}
        name = tags.get("name", "")
        rows.append({
            "type": el_type,
            "id": el_id,
            "lat": lat,
            "lon": lon,
            "name": name,
            "tags": tags
        })
    return rows

def save_csv(rows, out_file="results.csv"):
    records = []
    for r in rows:
        records.append({
            "type": r["type"],
            "id": r["id"],
            "lat": r["lat"],
            "lon": r["lon"],
            "name": r["name"],
            "tags": ";".join([f"{k}={v}" for k, v in (r["tags"] or {}).items()])
        })
    df = pd.DataFrame.from_records(records)
    df.to_csv(out_file, index=False)
    print(f"[+] Saved {len(df)} rows to {out_file}")

def main():
    parser = argparse.ArgumentParser(description="Query Overpass API and save results to CSV")
    parser.add_argument("--min-lat", type=float, required=True)
    parser.add_argument("--min-lon", type=float, required=True)
    parser.add_argument("--max-lat", type=float, required=True)
    parser.add_argument("--max-lon", type=float, required=True)
    parser.add_argument("--tag", type=str, required=True, help='Tag like "amenity=cafe" or "shop"')
    parser.add_argument("--out", type=str, default="results.csv")
    args = parser.parse_args()

    query = build_query(args.min_lat, args.min_lon, args.max_lat, args.max_lon, args.tag)
    print("[*] Running Overpass query...")
    data = run_query(query)
    rows = parse_elements(data)
    save_csv(rows, out_file=args.out)

if __name__ == "__main__":
    main()
