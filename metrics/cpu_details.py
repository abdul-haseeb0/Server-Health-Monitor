import psutil
import time
from datetime import timedelta

def cpu_usage():
    return {
        "usage": psutil.cpu_percent(),
        "cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True)
    }

def uptime():
    uptime_s = time.time() - psutil.boot_time()
    uptime_h = timedelta(seconds=uptime_s)
    return uptime_h

