import psutil
import platform
import socket
import subprocess
from datetime import datetime

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
    os = platform.system()
    result = None

    try:
        if os == "Windows":
            output = subprocess.run(
                ["ping", host, "-n", "3"],
                capture_output=True,
                text=True,
                check=True
            )
            
        else:
            output = subprocess.run(
                ["ping", "-c", "3", host],
                capture_output=True,
                text=True,
                check=True
            )

        result = output.stdout

    except subprocess.CalledProcessError as e:
        result = (
            f"Ping test failed with exception {e.returncode}\n"
            f"Error output: {e.stderr}\n"
        )
        
    return result

def get_top_processes():
    processes = []
    
    for p in psutil.process_iter(["pid", "name", "memory_percent"]):
        try:
            processes.append(p.info)

        except (psutil.NoSuchProcess, psutil.ZombieProcess, psutil.AccessDenied):
            pass
    
    processes = sorted(processes, key=lambda x: x["memory_percent"], reverse=True)
    return processes[:5]

def make_txt(system_info, ping_info, top_processes):
    info = system_info["System Name"]
    now = datetime.now()

    filename = f"{info}_Report_{now.strftime("%Y-%m-%d_%H-%M-%S")}.txt"

    with open(filename, "w") as f:
        f.write("*** SYSTEM INFO ***\n")

        for key, value in system_info.items():
            f.write(f"{key}: {value}\n")
        
        f.write("\n")
        f.write("*** PING TEST ***")
        f.write(ping_info)

        f.write("\n")
        f.write("*** TOP 5 PROCESSES BY MEMORY USAGE (%) ***")
        f.write("\n")

        for p in top_processes:
            f.write(f"{p["name"]} ({p["pid"]}): {p["memory_percent"]:5.2f}%\n")