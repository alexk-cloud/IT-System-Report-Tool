import psutil
import platform
import socket
import subprocess

def get_system_info(): 
    info = {}
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    info["System Name"] = f"{socket.gethostname()}"
    info["OS"] = f"{platform.system()} {platform.release()}"
    info["Build"] = platform.version()
    info["Architecture"] = platform.machine()
    
    info["# CPU Cores"] = psutil.cpu_count(logical=False)
    info["# CPU Threads"] = psutil.cpu_count(logical=True)
    info["CPU Usage (%)"] = psutil.cpu_percent(interval=1)

    info["Total RAM (GB)"] = round(mem.total / (1024**3), 2)
    info["Available RAM (GB)"] = round(mem.available / (1024**3), 2)
    info["Memory Usage (%)"] = mem.percent

    info["Disk Total (GB)"] = round(disk.total / (1024**3), 2)
    info["Disk Free (GB)"] = round(disk.free / (1024**3), 2)
    info["Disk Used (%)"] = disk.percent

    return info

def ping_test(host="8.8.8.8"):
    try:
        output = subprocess.run(
            ["ping", host, "-n", "3"],
            capture_output=True,
            text=True
        )

        print(f"Ping Test with {host}")
        print('*' * 50)
        print(output.stdout)
    
    except subprocess.CalledProcessError as e:
        print(f"Ping test failed with exception {e.returncode}")
        print(f"Error output: {e.stderr}")

def get_top_processes():
    processes = []
    
    for p in psutil.process_iter(["pid", "name", "memory_percent"]):
        try:
            processes.append(p.info)

        except (psutil.NoSuchProcess, psutil.ZombieProcess, psutil.AccessDenied):
            pass
    
    processes = sorted(processes, key=lambda x: x["memory_percent"], reverse=True)
    return processes[:5]