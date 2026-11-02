# Katabump Deployment Files

This folder contains everything needed to run BlackBird DataBridge as a persistent service on Katabump.com servers — without GitHub Actions hourly limits.

## Files

| File | Purpose |
|------|---------|
| `Dockerfile` | Python 3.11 container image |
| `requirements.txt` | Python dependencies (currently empty — stdlib only) |
| `runner.py` | Infinite loop: runs `analyze.py` + `compare.py` every N seconds |
| `docker-compose.yml` | Docker Compose service definition |
| `KATABUMP_SETUP.md` | Step-by-step deployment guide |

## Quick Start

```bash
git clone https://github.com/vAHiD55555/BlackBird-by-AndroidHarness-.git
cd BlackBird-by-AndroidHarness/katabump
docker-compose up -d --build
```

See `KATABUMP_SETUP.md` for full details.
