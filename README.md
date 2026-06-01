# Server Health Monitor (SHM)

A lightweight, real-time terminal-based server health monitoring CLI tool built with `psutil` and `rich.live`. SHM provides a continuously updating, beautifully formatted dashboard directly in your terminal — no web interface, no agents, no overhead.

---

## Features

- **CPU Monitoring** — Real-time CPU usage percentage and system uptime
- **Memory Overview** — Used, free, and total RAM with human-readable units
- **Disk Summary** — Overall disk usage including used, free, and total space
- **Partition Breakdown** — Per-partition details including mount point, filesystem type, used, free, and total space
- **Live Refresh** — Powered by `rich.live` for a smooth, flicker-free terminal dashboard
- **Zero Configuration** — No config files, no environment variables, no daemons

---

## Requirements

- Python
- pip

Dependencies are listed in `requirements.txt`:

```
psutil
rich
```

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/server-health-monitor.git
cd server-health-monitor
pip install -r requirements.txt
```

---

## Usage

Run the monitor with a single command:

```bash
python3 main.py
```

The dashboard will launch in your terminal and begin refreshing automatically. Press `Ctrl+C` to exit cleanly.

---

## Dashboard Overview

Once running, SHM displays the following panels in your terminal:

| Panel | Metrics |
|---|---|
| **CPU** | Usage (%), System Uptime |
| **Memory** | Total, Used, Free |
| **Disk (Summary)** | Total, Used, Free |
| **Disk (Partitions)** | Mount Point, Filesystem, Total, Used, Free |

All values are displayed in human-readable units (KB, MB, GB) and update in real time.

---

## Project Structure

```
server-health-monitor/
├── main.py            # Entry point — launches the live dashboard
├── requirements.txt   # Python dependencies
└── README.md
```

---

## Notes

- Partition metrics are collected for all mounted, accessible filesystems. Partitions that are unavailable or raise permission errors are skipped gracefully.
- SHM is designed for local and remote terminal sessions (SSH compatible).
- Tested on Linux. Should work on macOS and Windows with minor variance in partition data.

---

## License

This project is open source. See `LICENSE` for details.
