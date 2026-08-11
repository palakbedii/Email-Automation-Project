from .metrics import (
    get_hostname,
    get_ip_address,
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage
)

from .report_generator import generate_report


def generate_monitoring_report():
    """
    Collect all monitoring metrics and generate an Excel report.
    """


    # 1. Collect monitoring information

    node_name = get_hostname()
    ip_address = get_ip_address()
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()


    # 2. Generate Excel report

    report_path = generate_report(
        node_name=node_name,
        ip_address=ip_address,
        cpu_usage=cpu_usage,
        memory_usage=memory_usage,
        disk_usage=disk_usage
    )

    return report_path