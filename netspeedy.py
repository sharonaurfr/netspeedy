import subprocess
import ctypes
import platform

class NetSpeedy:
    def __init__(self):
        self.os_version = platform.system()

    def check_admin(self):
        """Check if the script is running with administrative privileges."""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except AttributeError:
            return False

    def optimize_tcp(self):
        """Optimize TCP settings for faster internet speeds."""
        try:
            subprocess.run(["netsh", "int", "tcp", "set", "global", "autotuninglevel=normal"], check=True)
            subprocess.run(["netsh", "int", "tcp", "set", "global", "rss=enabled"], check=True)
            subprocess.run(["netsh", "int", "tcp", "set", "global", "chimney=enabled"], check=True)
            print("TCP settings optimized.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to optimize TCP settings: {e}")

    def optimize_dns_cache(self):
        """Optimize DNS cache settings."""
        try:
            subprocess.run(["ipconfig", "/flushdns"], check=True)
            subprocess.run(["netsh", "dns", "client", "set", "dnssec", "state=disabled"], check=True)
            print("DNS cache settings optimized.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to optimize DNS cache settings: {e}")

    def optimize_network_throughput(self):
        """Optimize network throughput for faster download speeds."""
        try:
            subprocess.run(["netsh", "int", "tcp", "set", "global", "heuristics=disabled"], check=True)
            subprocess.run(["netsh", "int", "tcp", "set", "global", "ecncapability=disabled"], check=True)
            print("Network throughput optimized.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to optimize network throughput: {e}")

    def run(self):
        """Run all optimizations."""
        if self.os_version != "Windows":
            print("NetSpeedy is only supported on Windows platforms.")
            return

        if not self.check_admin():
            print("This script requires administrative privileges to run. Please run as administrator.")
            return

        print("Starting NetSpeedy optimizations...")
        self.optimize_tcp()
        self.optimize_dns_cache()
        self.optimize_network_throughput()
        print("NetSpeedy optimizations complete.")

if __name__ == "__main__":
    netspeedy = NetSpeedy()
    netspeedy.run()