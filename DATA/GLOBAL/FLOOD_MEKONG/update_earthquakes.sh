#!/bin/bash
# Cập nhật dữ liệu động đất mới nhất (24 giờ qua, >=4.5)

TODAY=$(date +%Y-%m-%d)
OUTPUT_DIR="DATA/GLOBAL/FLOOD_MEKONG/RAW_DATA"
mkdir -p "$OUTPUT_DIR"

echo "[$(date)] Đang tải dữ liệu động đất ngày $TODAY..."

curl -s "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=$(date -d '1 day ago' +%Y-%m-%d)&minmagnitude=4.5" \
  > "$OUTPUT_DIR/earthquakes_${TODAY}.geojson"

echo "[$(date)] Đã lưu dữ liệu vào $OUTPUT_DIR/earthquakes_${TODAY}.geojson"
