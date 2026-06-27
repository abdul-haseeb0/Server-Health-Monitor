<div align="center">

# 🖥️ Server Health Monitor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/psutil-powered-4CAF50?style=flat-square" alt="psutil">
  <img src="https://img.shields.io/badge/rich-live%20dashboard-7B2FBE?style=flat-square" alt="rich">
  <img src="https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-0078D4?style=flat-square" alt="Platform">
  <img src="https://img.shields.io/badge/license-Open%20Source-22C55E?style=flat-square" alt="License">
</p>

<p align="center">
  A lightweight, zero-config, real-time server health dashboard — right in your terminal.
</p>

</div>

---

## Overview

**SHM (Server Health Monitor)** gives you a continuously updating, beautifully formatted system metrics dashboard directly in your terminal — powered by [`psutil`](https://github.com/giampaolo/psutil) and [`rich.live`](https://rich.readthedocs.io/en/stable/live.html). No web interface, no agents, no daemons, no overhead.

Built for developers and sysadmins who want fast, readable system visibility during local development, remote SSH sessions, or server maintenance.

---

## Features

| Feature | Description |
|---|---|
| ⚡ **CPU Monitoring** | Real-time CPU usage (%) with system uptime |
| 🧠 **Memory Overview** | Total, used, and free RAM in human-readable units |
| 💾 **Disk Summary** | Aggregated disk usage across all drives |
| 📂 **Partition Breakdown** | Per-partition details — mount point, filesystem type, used/free/total |
| 🔄 **Live Refresh** | Smooth, flicker-free updates via `rich.live` |
| 🔧 **Zero Configuration** | No config files, no environment variables, no setup wizards |
| 🛡️ **Graceful Error Handling** | Skips inaccessible or permission-restricted partitions cleanly |
| 🌐 **SSH Compatible** | Designed for both local and remote terminal sessions |

---

## Requirements

- **Python** 3.8+
- **pip**

Dependencies (`requirements.txt`):

```
psutil
rich
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/server-health-monitor.git
cd server-health-monitor

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python3 main.py
```

The dashboard launches instantly and begins refreshing automatically. Press `Ctrl+C` to exit cleanly.

---

## Dashboard Panels

Once running, SHM renders the following panels in your terminal:

```
┌─────────────────────────────────────────────────────────────┐
│ 🖥  CPU                                                      │
│      Usage: 12.4%    Uptime: 3d 7h 22m                      │
├─────────────────────────────────────────────────────────────┤
│ 🧠  Memory                                                  │
│      Total: 16.0 GB   Used: 9.3 GB   Free: 6.7 GB           │
├─────────────────────────────────────────────────────────────┤
│  💾  Disk (Summary)                                         │
│      Total: 512 GB    Used: 210 GB   Free: 302 GB           │
├─────────────────────────────────────────────────────────────┤
│  📂  Disk (Partitions)                                      │
│      Mount     FS      Total    Used     Free               │
│      /         ext4    100 GB   45 GB    55 GB              │
│      /home     ext4    412 GB   165 GB   247 GB             │
└─────────────────────────────────────────────────────────────┘
```

All values are displayed in human-readable units (KB, MB, GB) and refresh in real time.

---

## Project Structure

```
server-health-monitor/
├── main.py                   # Entry point
├── requirements.txt          # Python dependencies
├── README.md
├── LICENSE
│
├── metrics/
│   ├── cpu_details.py        # CPU usage & uptime collection
│   ├── memory_details.py     # RAM metrics collection
│   ├── disk_details.py       # Disk & partition metrics collection
│   └── displaying_data.py    # Rich panel rendering logic
│
├── utils/
│   └── logs_config.py        # Logging configuration
│
├── logs/
│   └── shmlogs.log           # Runtime log output
│
└── screenshots/
    ├── screenshot - Linux - 2June2026
    └── screenshot - Windows - 2June2026
```

---

## Notes

- Partitions that are unavailable or raise permission errors are **skipped gracefully** — SHM never crashes on restricted mounts.
- Fully compatible with **SSH remote sessions** — no GUI or browser required.
- Tested on **Linux**. Expected to work on **macOS** and **Windows** with minor variance in partition data.

---

## License

This project is open source. See [`LICENSE`](./LICENSE) for details.
