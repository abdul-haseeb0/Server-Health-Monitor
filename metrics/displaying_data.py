from metrics.cpu_details import cpu_usage, uptime
from metrics.memory_details import memory_usage
from metrics.disk_details import disk_usage
from metrics.network_details import speed_info, network_info


def print_cpu():
    display_cpu = cpu_usage()
    return (
        "CPU ↴\n\n"
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
        "Memory ↴\n\n"
        f"Usage:        {display_memory['usage']}%\n"
        f"Total:        {display_memory['total']:.2f} GB\n"
        f"Available:    {display_memory['available']:.2f} GB\n"
        "---------------------------------------"
    )


def print_disk():
    display_disks = disk_usage()

    output = "Disk Usage Info ↴\n"

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

def get_network_details():
    network_list = network_info()
    output = "Network Details\n\n"

    for network in network_list:

        ipv4_val = network['ipv4'][0]['address'] if network['ipv4'] else "N/A"
        ipv6_val = network['ipv6'][0]['address'] if network['ipv6'] else "N/A"

        output += (
            f"Interface:        {network['interface']}\n"
            f"Is Up:            {network['is_up']}\n"
            f"Max Speed:        {network['max_speed_mbps']} Mbps\n"  # Note: matched key name from previous code
            f"IPv4 Address:     {ipv4_val}\n"
            f"IPv6 Address:     {ipv6_val}\n"
            f"{'-' * 30}\n"  # Separator line between interfaces
        )

    return output


def get_speed():
    display_speed = speed_info()
    return (
        " Speed\n\n"
        f"Download Speed:        {display_speed['download_speed']:.2f} Mbps\n"
        f"Upload Speed:        {display_speed['upload_speed']:.2f} Mbps"
    )