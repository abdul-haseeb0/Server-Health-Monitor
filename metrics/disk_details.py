import psutil
GB = 1024**3

def disk_usage():
    disk = psutil.disk_usage('/')
    return {
        "usage": disk.percent,
        "total": disk.total / GB
    }