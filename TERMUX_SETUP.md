# BlackBird DataBridge — Termux Setup

## 1. Clone repo
```bash
git clone https://github.com/vAHiD55555/BlackBird-by-AndroidHarness-.git
cd BlackBird-by-AndroidHarness
```

## 2. Copy file cron vào home
```bash
cp blackbird_cron.sh ~/
cp blackbird_crontab.txt ~/
```

## 3. Cấp quyền thực thi
```bash
chmod +x ~/blackbird_cron.sh
```

## 4. Cài crontab (chạy mỗi giờ)
```bash
crontab ~/blackbird_crontab.txt
```

## 5. Kiểm tra crontab đã cài chưa
```bash
crontab -l
```

## 6. Xem log chạy
```bash
tail -f ~/BlackBird-by-AndroidHarness/logs/cron.log
tail -f ~/BlackBird-by-AndroidHarness/logs/analysis.log
```

## 7. Nếu muốn dừng cron
```bash
crontab -r
```

## Lưu ý
- Termux phải đang chạy (không bị杀) để cron hoạt động.
- Nếu Termux bị tắt, cron sẽ không chạy cho đến khi mở lại.
- Dữ liệu cần đặt trong: `data/market_data.jsonl`
