from monitoring.monitoring_service import generate_monitoring_report


print("Generating monitoring report...")

report_path = generate_monitoring_report()

print()
print("Report generated!")
print("Path:", report_path)
print("Type:", type(report_path))

if report_path.exists():
    print("SUCCESS: Report exists.")
else:
    print("ERROR: Report does not exist.")