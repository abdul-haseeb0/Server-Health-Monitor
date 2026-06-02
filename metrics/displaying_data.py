from metrics.cpu_details import cpu_usage
from metrics.cpu_details import uptime
from metrics.memory_details import memory_usage
from metrics.disk_details import disk_usage
import pyfiglet
from colorama import Fore

def print_cpu():
    display_cpu = cpu_usage()
    return (
        "CPU\n\n"
        f"Usage:                    {display_cpu['usage']}%\n"
        f"Cores:                    {display_cpu['cores']}\n"
        f"Logical Processors:       {display_cpu['logical_cores']}"
    )

def print_uptime():
    time = uptime()

    days = time.days
    hours, remainder = divmod(time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return (
        f"System Uptime: {days}d {hours}h {minutes}m {seconds}s\n"
        "---------------------------------------"
    )

def print_memory():
    display_memory = memory_usage()
    return (
        "Memory\n\n"
        f"Usage:        {display_memory['usage']}%\n"
        f"Total:        {display_memory['total']:.2f} GB\n"
        f"Available:    {display_memory['available']:.2f} GB\n"
        "---------------------------------------"
    )


def print_disk():
    display_disks = disk_usage()

    output = "Disk Usage Info\n"

    for disk in display_disks:
        output += (
            f"\nDevice:         {disk['device']}\n"
            f"Mountpoint:       {disk['mountpoint']}\n"
            f"Usage:            {disk['usage_percent']}%\n"
            f"Total:            {disk['total_gb']:.2f} GB\n"
            f"Free:             {disk['free_gb']:.2f} GB\n"
            "---------------------------------------"
        )

    return output

def header_banner():
    banner = pyfiglet.figlet_format("Server Health Monitor")
    return Fore.CYAN + banner
