"""
Turn the raw Met Office station files into tidy CSVs for the course.

Run this from the repository root:

    python data/prepare_data.py

It reads every .txt file in data/raw/ and writes:

    data/uk_weather.csv     all stations, all years, one row per station-month
    data/oxford_2015_2025.csv   a small gentle starter file for Weeks 1 and 2

The raw files stay exactly as downloaded. Weeks 5 and 6 use them on purpose,
because the missing-value markers and the header lines are the lesson.

Source: Met Office historic station data, Open Government Licence v3.0.
"""

import csv
import re
from pathlib import Path

DATA = Path(__file__).parent
RAW = DATA / "raw"

# The five header lines plus the two column-heading lines.
HEADER_LINES = 7

COLUMNS = ["station", "year", "month", "tmax", "tmin", "af", "rain", "sun"]


def read_location(line):
    """Pull latitude and longitude out of the station's Location line."""
    match = re.search(r"Lat\s+(-?\d+\.\d+)\s+Lon\s+(-?\d+\.\d+)", line)
    if match:
        return float(match.group(1)), float(match.group(2))
    return None, None


def clean_value(text):
    """
    Turn one raw reading into a number, or None if it is missing.

    Met Office markers:
        ---   missing (more than 2 days missing that month)
        *     estimated
        #     sunshine from a Kipp and Zonen sensor rather than Campbell Stokes
    """
    text = text.strip().rstrip("*#")
    if not text or text.startswith("---"):
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_station(path):
    """Read one station file and yield a dict per month."""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()

    name = lines[0].strip()
    lat, lon = read_location(lines[1])

    for line in lines[HEADER_LINES:]:
        if not line.strip():
            continue

        fields = line.split()

        # Rows from the current year carry a trailing "Provisional" flag.
        # Anything shorter than seven fields is not a data row.
        if len(fields) < 7:
            continue
        if not fields[0].isdigit():
            continue

        yield {
            "station": name,
            "year": int(fields[0]),
            "month": int(fields[1]),
            "tmax": clean_value(fields[2]),
            "tmin": clean_value(fields[3]),
            "af": clean_value(fields[4]),
            "rain": clean_value(fields[5]),
            "sun": clean_value(fields[6]),
            "_lat": lat,
            "_lon": lon,
        }


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: ("" if row[k] is None else row[k]) for k in COLUMNS})


def main():
    raw_files = sorted(RAW.glob("*.txt"))
    if not raw_files:
        raise SystemExit(f"No .txt files found in {RAW}. Download them first.")

    all_rows = []
    for path in raw_files:
        rows = list(parse_station(path))
        all_rows.extend(rows)
        name = rows[0]["station"] if rows else path.stem
        years = f"{rows[0]['year']} to {rows[-1]['year']}" if rows else "no data"
        print(f"{name:12s} {len(rows):5d} rows  {years}")

    all_rows.sort(key=lambda r: (r["station"], r["year"], r["month"]))

    out = DATA / "uk_weather.csv"
    write_csv(out, all_rows)
    print(f"\nWrote {out.name}  ({len(all_rows)} rows)")

    starter = [
        r for r in all_rows
        if r["station"] == "Oxford" and 2015 <= r["year"] <= 2025
    ]
    out2 = DATA / "oxford_2015_2025.csv"
    write_csv(out2, starter)
    print(f"Wrote {out2.name}  ({len(starter)} rows)")

    missing = sum(1 for r in all_rows if r["tmax"] is None)
    print(f"\nMissing tmax values: {missing} of {len(all_rows)}")


if __name__ == "__main__":
    main()
