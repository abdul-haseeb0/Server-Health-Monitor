import psutil
GB = 1024**3

def memory_usage():
    mem = psutil.virtual_memory()
    return {
        "usage": mem.percent,
        "total": mem.total / GB,
        "available": mem.available / GB
    }