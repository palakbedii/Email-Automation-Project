from monitoring.report_generator import generate_report


report_path = generate_report(
    node_name="LAPTOP-K00JNL0V",
    ip_address="192.168.1.10",
    cpu_usage=7.71,
    memory_usage=50.38,
    disk_usage=87.54
)

print("Report generated successfully!")
print("Report path:", report_path)