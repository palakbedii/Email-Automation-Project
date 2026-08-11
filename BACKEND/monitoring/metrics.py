import socket

from .prometheus_api import query_prometheus


def get_hostname():
    """Get the Windows hostname from Prometheus."""

    result = query_prometheus("windows_os_hostname")
    results = result["data"]["result"]

    if not results:
        raise ValueError("Hostname metric returned no data.")

    return results[0]["metric"]["hostname"]


# CPU Usage
def get_cpu_usage():
    """Get the average CPU usage percentage from Prometheus."""

    promql = (
        '100 - (avg(rate(windows_cpu_time_total{mode="idle"}[5m])) * 100)'
    )

    result = query_prometheus(promql)
    results = result["data"]["result"]

    if not results:
        raise ValueError("CPU usage metric returned no data.")

    cpu_usage = float(results[0]["value"][1])
    return round(cpu_usage, 2)


# RAM Usage
def get_memory_usage():
    """Get the physical memory usage percentage from Prometheus."""

    total_result = query_prometheus(
        "windows_memory_physical_total_bytes"
    )

    available_result = query_prometheus(
        "windows_memory_available_bytes"
    )

    total_results = total_result["data"]["result"]
    available_results = available_result["data"]["result"]

    if not total_results:
        raise ValueError(
            "Total physical memory metric returned no data."
        )

    if not available_results:
        raise ValueError(
            "Available memory metric returned no data."
        )

    total_memory = float(total_results[0]["value"][1])
    available_memory = float(available_results[0]["value"][1])

    used_memory = total_memory - available_memory
    memory_usage = (used_memory / total_memory) * 100

    return round(memory_usage, 2)


# Disk Usage
def get_disk_usage():
    """Get the C: drive disk usage percentage from Prometheus."""

    total_result = query_prometheus(
        'windows_logical_disk_size_bytes{volume="C:"}'
    )

    free_result = query_prometheus(
        'windows_logical_disk_free_bytes{volume="C:"}'
    )

    total_results = total_result["data"]["result"]
    free_results = free_result["data"]["result"]

    if not total_results:
        raise ValueError(
            "Total disk size metric returned no data."
        )

    if not free_results:
        raise ValueError(
            "Free disk space metric returned no data."
        )

    total_disk = float(total_results[0]["value"][1])
    free_disk = float(free_results[0]["value"][1])

    used_disk = total_disk - free_disk
    disk_usage = (used_disk / total_disk) * 100

    return round(disk_usage, 2)


# Getting local IP dynamically
def get_ip_address():
    """Get the local machine's active IP address."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("8.8.8.8", 80))
        ip_address = sock.getsockname()[0]
    finally:
        sock.close()

    return ip_address