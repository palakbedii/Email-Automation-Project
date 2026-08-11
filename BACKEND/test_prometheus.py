from monitoring.metrics import (
    get_hostname,
    get_ip_address,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage
)


hostname = get_hostname()
ip_address = get_ip_address()
cpu = get_cpu_usage()
memory = get_memory_usage()
disk = get_disk_usage()


print("Hostname:", hostname)
print("IP Address:", ip_address)
print("CPU Usage:", cpu, "%")
print("RAM Usage:", memory, "%")
print("Disk Usage:", disk, "%")