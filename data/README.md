# Course Dataset: UK Weather Station Records

This folder holds the dataset used throughout the course, from Week 1 to the Week 10 portfolio project. The same data comes back every week, so the work you do in one lesson builds on the last rather than being thrown away.

## Where it came from

Met Office historic station data, five stations, monthly readings.

> Contains public sector information licensed under the Open Government Licence v3.0.

Source: https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data

The data is redistributed here under that licence. If you use it in anything you publish, keep the attribution line above.

## The five stations

| Station | Location | Record starts | Rows |
| --- | --- | --- | --- |
| Armagh | Northern Ireland, 54.352N 6.649W | 1853 | 2,084 |
| Oxford | South England, 51.761N 1.262W | 1853 | 2,084 |
| Sheffield | North England, 53.381N 1.490W | 1883 | 1,724 |
| Lerwick | Shetland, 60.139N 1.183W | 1930 | 1,149 |
| Camborne | Cornwall, 50.218N 5.327W | 1978 | 576 |

They were chosen for geographic spread rather than at random. Lerwick against Camborne is the length of the country, and the difference shows up clearly in sunshine hours and rainfall.

## The files

| File | What it is | Used from |
| --- | --- | --- |
| `oxford_2015_2025.csv` | Oxford only, 2015 to 2025, 132 rows | Weeks 1 and 2 |
| `uk_weather.csv` | All five stations, all years, 7,617 rows | Weeks 3, 4, 7, 8, 9, 10 |
| `raw/*.txt` | The original Met Office files, untouched | Weeks 5 and 6 |
| `prepare_data.py` | The script that turns `raw/` into the CSVs | Reference |

The raw files are kept deliberately. They are awkward: seven lines of header before the data starts, missing months marked `---`, estimated values marked `*`, and a trailing `Provisional` flag on recent rows. That awkwardness is the point. Weeks 5 and 6 are about validation, error handling and file parsing, and real data that needs cleaning teaches those far better than a tidy file that does not.

## Columns

| Column | Meaning | Units |
| --- | --- | --- |
| `station` | Station name | |
| `year` | Year of the reading | |
| `month` | Month, 1 to 12 | |
| `tmax` | Mean daily maximum temperature | degrees Celsius |
| `tmin` | Mean daily minimum temperature | degrees Celsius |
| `af` | Days of air frost that month | days |
| `rain` | Total rainfall | millimetres |
| `sun` | Total sunshine duration | hours |

Empty cells mean the reading is missing. There are 171 months with no temperature recorded, mostly in the nineteenth century, and handling them is part of the work rather than a fault in the file.

## Regenerating the CSVs

You should not need to, but if the raw files are updated:

```
python data/prepare_data.py
```

It prints a row count per station and rewrites both CSVs.

## Refreshing the raw data

The Met Office adds a new month roughly monthly. To pull the latest:

```
for s in oxford sheffield armagh camborne lerwick; do
  curl -sS -o "data/raw/${s}.txt" "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/${s}data.txt"
done
python data/prepare_data.py
```
