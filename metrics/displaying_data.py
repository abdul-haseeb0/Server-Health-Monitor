from metrics.cpu_details import cpu_usage, uptime
from metrics.memory_details import memory_usage
from metrics.disk_details import disk_usage
from metrics.network_details import network_info, speed_info


def collect_dashboard_data():
    """
    Collect all dashboard data in one place.
    UI is handled separately in utils/ui.py.
    """

    return {
        "cpu": cpu_usage(),
        "uptime": uptime(),
        "memory": memory_usage(),
        "disks": disk_usage(),
        "network": network_info(),
        "speed": speed_info(),
    }