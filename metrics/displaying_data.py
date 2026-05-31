from metrics.cpu_details import cpu_usage
from metrics.cpu_details import uptime
from metrics.memory_details import memory_usage
from metrics.disk_details import disk_usage

def print_cpu():
    display_cpu = cpu_usage()
    print("\nCPU\n")
    print(f"Usage: {display_cpu['usage']}%")
    print(f"Cores: {display_cpu['cores']}")
    print(f"Logical Processors: {display_cpu['logical_cores']}")
    return

def print_uptime():
    time = uptime()

    days = time.days
    hours, remainder = divmod(time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"System Uptime: {days}d {hours}h {minutes}m {seconds}s")

def print_memory():
    display_memory = memory_usage()
    print("\nMemory\n")
    print(f"Usage: {display_memory['usage']}%")
    print(f"Total: {display_memory['total']:.2f}GB")
    print(f"Available: {display_memory['available']:.2f}GB")
    return

def print_disk():
    display_disk = disk_usage()
    print("\nDisk\n")
    print(f"Usage: {display_disk['usage']}%")
    print(f"Total: {display_disk['total']:.2f}GB")
    return