#PythonEstadoDiscosRed.py
import subprocess
import time


def get_disk_status():
  """Gets the status of all disks."""
  try:
    disk_status = subprocess.run(["wmic", "diskdrive", "get", "status", "caption", "size", "freespace"], shell=True, capture_output=True, text=True).stdout.splitlines()
  except subprocess.CalledProcessError:
    return {}

  disk_status = {}
  for disk in disk_status:
    disk_name, disk_status, disk_size, free_space = disk.split()
    disk_status[disk_name] = {
        "status": disk_status,
        "size": disk_size,
        "free_space": free_space,
    }
  return disk_status


def get_network_activity():
  """Gets the network activity for all interfaces."""
  try:
    interfaces = subprocess.check_output(["netstat", "-ban"]).decode("utf-8").splitlines()
  except subprocess.CalledProcessError:
    return {}

  network_activity = {}
  for interface in interfaces:
    interface_name, interface_status, interface_ip, interface_mac = interface.split()
    network_activity[interface_name] = {
        "status": interface_status,
        "ip": interface_ip,
        "mac": interface_mac,
    }
  return network_activity

def main():
  """Monitors the status of disks and network activity."""
  while True:
    disk_status = get_disk_status()
    network_activity = get_network_activity()

    print("Disk status:")
    for disk_name, disk_info in disk_status.items():
      print("  %s: %s" % (disk_name, disk_info))

    print("Network activity:")
    for interface_name, interface_info in network_activity.items():
      print("  %s: %s" % (interface_name, interface_info))

    time.sleep(10)

if __name__ == "__main__":
  main()