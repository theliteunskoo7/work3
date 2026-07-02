#!/bin/bash
# Usage: ./send_telegram.sh "message text"
source /home/vijay/Documents/work3/.telegram_config
curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" \
  -d chat_id="${TELEGRAM_CHAT_ID}" \
  -d text="$1" \
  -d parse_mode="Markdown" > /dev/null
