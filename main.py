import psutil

GB = 1024**3

def cpu_usage():
    return {
        "usage": psutil.cpu_percent(),
        "cores": psutil.cpu_count(),
        "logical_cores": psutil.cpu_count(logical=True)
    }


def memory_usage():
    mem = psutil.virtual_memory()
    return {
        "usage": mem.percent,
        "total": mem.total / GB,
        "available": mem.available / GB
    }


def disk_usage():
    disk = psutil.disk_usage('/')
    return {
        "usage": disk.percent,
        "total": disk.total / GB
    }


print("[+] Gathering Server Information...")

cpu = cpu_usage()
print(f"Usage: {cpu['usage']}%")
print(f"Cores: {cpu['cores']}")
print(f"Logical Cores: {cpu['logical_cores']}")

memory = memory_usage()
print(f"Usage: {memory['usage']}%")
print(f"Total: {memory['total']}GB")
print(f"Available: {memory['available']}GB")

disk = disk_usage()
print(f"Usage: {disk['usage']}%")
print(f"Total: {disk['total']}GB")
