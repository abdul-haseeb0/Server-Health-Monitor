import psutil

GB = 1024 ** 3


def partitions_details():
    partitions = psutil.disk_partitions()
    result = []

    for partition in partitions:
        result.append({
            "device": partition.device,
            "mountpoint": partition.mountpoint,
            "filesystem-type": partition.fstype,
            "opts": partition.opts
        })

    return result


def disk_usage():
    usage_data = []

    for partition in psutil.disk_partitions():
        try:
            disk = psutil.disk_usage(partition.mountpoint)

            usage_data.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "usage_percent": disk.percent,
                "total_gb": disk.total / GB,
                "free_gb": disk.free / GB
            })

        except (PermissionError, FileNotFoundError):
            continue

    return usage_data