import psutil
import platform
import socket

def get_system_info(): 
    info = {}
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    info["System Name"] = f"{socket.gethostname()}"
    info["OS"] = f"{platform.system()} {platform.release()} {platform.version()}"
    

    info["# CPU Cores"] = psutil.cpu_count(logical=False)
    info["# CPU Threads"] = psutil.cpu_count(logical=True)

    info["Total RAM (GB)"] = round(mem.total / (1024**3), 2)
    info["Available RAM (GB)"] = round(mem.available / (1024**3), 2)
    info["Memory Usage (%)"] = mem.percent

    info["Disk Total (GB)"] = round(disk.total / (1024**3), 2)
    info["Disk Free (GB)"] = round(disk.free / (1024**3), 2)
    info["Disk Used (%)"] = disk.percent

    return info