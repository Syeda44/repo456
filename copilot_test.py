import os
import platform

def get_uptime():
    if platform.system() == "Windows":
        # Windows does not provide direct uptime, but we can use 'net stats srv'
        try:
            output = os.popen('net stats srv').read()
            for line in output.split('\n'):
                if "Statistics since" in line:
                    print("Uptime info:", line)
                    return
        except Exception as e:
            print("Could not retrieve uptime:", e)
    else:
        # Linux/Unix/Mac
        try:
            with open('/proc/uptime', 'r') as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = uptime_seconds // 3600
                minutes = (uptime_seconds % 3600) // 60
                seconds = uptime_seconds % 60
                print(f"System Uptime: {int(hours)}h {int(minutes)}m {int(seconds)}s")
        except FileNotFoundError:
            # macOS alternative
            try:
                output = os.popen('uptime').read()
                print("System Uptime:", output.strip())
            except Exception as e:
                print("Could not retrieve uptime:", e)

if __name__ == "__main__":
    get_uptime()
