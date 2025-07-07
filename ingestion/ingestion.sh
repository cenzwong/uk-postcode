curl -L "https://hub.arcgis.com/api/v3/datasets/ed28dda8b75146288d7d08d56d2290a0_1/downloads/data?format=csv&spatialRefId=27700" \
-o "data/$(date +%Y%m%d)_ons_postcode.csv"
