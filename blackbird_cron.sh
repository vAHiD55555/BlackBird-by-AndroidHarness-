#!/usr/bin/env bash
# BlackBird DataBridge — chạy phân tích thị trường mỗi giờ
# Lưu vào: ~/blackbird_cron.sh

REPO_DIR="$HOME/BlackBird-by-AndroidHarness"
DATA_FILE="$REPO_DIR/data/market_data.jsonl"
LOG_FILE="$REPO_DIR/logs/analysis.log"

mkdir -p "$REPO_DIR/logs"

echo "========== $(date '+%Y-%m-%d %H:%M:%S') ==========" >> "$LOG_FILE"

if [ ! -f "$DATA_FILE" ]; then
    echo "Chưa có dữ liệu: $DATA_FILE" >> "$LOG_FILE"
    exit 0
fi

python3 "$REPO_DIR/analysis/analyze.py" "$DATA_FILE" >> "$LOG_FILE" 2>&1

echo "----------------------------------------" >> "$LOG_FILE"
