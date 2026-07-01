# 🖥️ Server Health Monitor

**A lightweight, zero-config, real-time server health dashboard — right in your terminal.**

![Python](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge) ![psutil](https://img.shields.io/badge/libraries-psutil_%7C_rich-yellow?style=for-the-badge) ![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey?style=for-the-badge) ![License](https://img.shields.io/badge/license-open--source-green?style=for-the-badge)

---

## Overview

**SHM (Server Health Monitor)** gives you a continuously updating, beautifully formatted system dashboard directly in your terminal — powered by [`psutil`](https://pypi.org/project/psutil/) and [`rich.live`](https://rich.readthedocs.io/). No web interface, no agents, no daemons, no overhead.

Built for developers and sysadmins who want fast, readable system visibility during local development, remote SSH sessions, or server maintenance — now with a fully redesigned, multi-panel layout and live network monitoring.

---

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ **CPU Monitoring** | Real-time CPU usage (%), physical core count, and logical thread count |
| 🧠 **Memory Overview** | Usage %, total, and available RAM in human-readable units |
| 💾 **Disk Usage Table** | Per-device breakdown — mount point, used %, total, and free space |
| 🌐 **Network Interfaces** | Live table of interfaces with IPv4 address, link speed, and status (UP/DOWN) |
| 🚀 **Internet Speed Test** | Real-time download and upload throughput (Mbps) |
| ⏱️ **System Uptime** | Displayed prominently in the dashboard header |
| 🔄 **Live Refresh** | Smooth, flicker-free updates every second via `rich.live` |
| 🎨 **Color-Coded Panels** | Distinct panel colors for CPU, Memory, Disk, Network, and Speed at a glance |
| 🔧 **Zero Configuration** | No config files, environment variables, or setup wizards |
| 🛡️ **Graceful Error Handling** | Skips inaccessible or permission-restricted partitions/interfaces cleanly |
| 🖥️ **Cross-Platform** | Tested on Windows and Linux; expected to work on macOS |
| 🌐 **SSH Compatible** | Fully usable over remote terminal sessions — no GUI or browser required |

---

## 📸 Preview

The dashboard renders as a bordered, color-coded layout with a header banner, a disk usage table, a network table, and dedicated side panels for CPU, memory, and internet speed — all refreshing live.

```
┌──────────────────────────────────────────────────────────────────────────┐
│                          SERVER HEALTH MONITOR                           │
│                       System Uptime : 0d 8h 47m 45s                      │
└──────────────────────────────────────────────────────────────────────────┘
┌─ Disk Usage ──────────────────────────────────┐┌─ CPU ────────────────────┐
│ Device   Mount   Used    Total     Free       ││ Usage      20.3%         │
│ C:\      C:\     61.8%   374.81GB  143.18GB   ││ Cores      4             │
│ D:\      D:\     35.0%   100.00GB   65.05GB   ││ Threads    8             │
│                                               │ └─────────────────────────┘
│                                               │ ┌─ Memory ────────────────┐
│                                               │ │ Usage      25.4%        │
│                                               │ │ Total      31.81 GB     │
│                                               │ │ Available  23.74 GB     │
│                                               │ └─────────────────────────┘
│                                               │ ┌─ Internet Speed ────────┐
│                                               │ │ Download   0.00 Mbps    │
│                                               │ │ Upload     0.00 Mbps    │
└───────────────────────────────────────────────┘ └─────────────────────────┘
┌─ Network ──────────────────────────────────────────────────────────────────┐
│ Interface     IPv4              Speed        Status                        │
│ Ethernet 3    192.168.56.1      1000 Mbps     UP                           │
│ Wi-Fi         192.168.0.101     144 Mbps      UP                           │
└────────────────────────────────────────────────────────────────────────────┘
                     Refresh: 1 sec   |   Press CTRL+C to Exit
```

---

## Requirements

- Python 3.8+
- `pip`

**Dependencies** (`requirements.txt`):
```
psutil
rich
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/abdul-haseeb0/server-health-monitor.git
cd server-health-monitor

# Install dependencies
pip install -r requirements.txt
```

---

## Usage

```bash
python3 main.py
```

The dashboard launches instantly and begins refreshing automatically every second. Press **Ctrl+C** to exit cleanly.

---

## Dashboard Panels

| Panel | Contents |
|---|---|
| **Header** | Dashboard title and total system uptime |
| **Disk Usage** | Table of all detected devices with used %, total, and free space |
| **CPU** | Usage %, physical core count, logical thread count |
| **Memory** | Usage %, total RAM, available RAM |
| **Internet Speed** | Live download/upload throughput in Mbps |
| **Network** | Table of active interfaces with IPv4 address, link speed, and UP/DOWN status |
| **Footer** | Refresh interval and exit instructions |

All values are displayed in human-readable units (KB, MB, GB / Mbps) and refresh live.

---

## Project Structure

```
server-health-monitor/
├── main.py 
├── requirements.txt
├── README.md
├── LICENSE
│
├── metrics/
│   ├── cpu_details.py
│   ├── memory_details.py
│   ├── disk_details.py
│   ├── network_details.py
│   └── displaying_data.py
│
├── utils/
│   ├── logs_config.py
│   ├── ui.py
│   └── banner.py
│
├── logs/
│   └── shmlogs.log
│
└── screenshots/
    ├── screenshot - Linux - 2June2026
    ├── screenshot - Windows - 2June2026
    └── screenshot - Windows - 1-July-2026 - Updated UI
```

---

## Notes

- Partitions or interfaces that are unavailable or raise permission errors are skipped gracefully — SHM never crashes on restricted mounts or interfaces.
- Internet speed test runs periodically in the background so it doesn't block the live refresh loop.
- Fully compatible with SSH remote sessions — no GUI or browser required.
- Tested on Windows and Linux. Expected to work on macOS with minor variance in partition/network data.

---

## License

This project is open source. See [LICENSE](LICENSE) for details.
