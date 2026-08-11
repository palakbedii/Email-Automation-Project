from monitoring.monitoring_service import generate_monitoring_report


report_path = generate_monitoring_report()

print("Monitoring report generated successfully!")
print("Report path:", report_path)