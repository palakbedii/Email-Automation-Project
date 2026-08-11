from pathlib import Path

# Prometheus Configuration
PROMETHEUS_URL = "http://127.0.0.1:9090"
QUERY_ENDPOINT = "/api/v1/query"        # API Endpoint
REQUEST_TIMEOUT = 10                    # HTTP Request Timeout (seconds)

# HTTP Request Timeout (seconds)
BASE_DIR = Path(__file__).resolve().parent      # Base directory of monitoring/
BACKEND_DIR = BASE_DIR.parent                   # BACKEND/ directory
REPORT_FOLDER = BACKEND_DIR / "Reports"         # BACKEND/Reports/
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

# Report configuration
REPORT_NAME_PREFIX = "Monitoring_Report"
SHEET_NAME = "Node Monitoring"