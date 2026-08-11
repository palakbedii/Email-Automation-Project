import requests

from .config import (
    PROMETHEUS_URL,
    QUERY_ENDPOINT,
    REQUEST_TIMEOUT
)


def query_prometheus(promql):
    """
    Execute a PromQL instant query against Prometheus.

    Args:
        promql (str): PromQL query to execute.

    Returns:
        dict: Prometheus query result.

    Raises:
        ConnectionError:
            If Prometheus cannot be reached.

        TimeoutError:
            If the Prometheus request times out.

        RuntimeError:
            If Prometheus returns an HTTP error, invalid JSON,
            or an unsuccessful API response.
    """

    url = f"{PROMETHEUS_URL}{QUERY_ENDPOINT}"

    params = {
        "query": promql
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

    except requests.exceptions.ConnectionError as e:

        raise ConnectionError(
            f"Prometheus is unavailable at {PROMETHEUS_URL}"
        ) from e

    except requests.exceptions.Timeout as e:

        raise TimeoutError(
            f"Prometheus request timed out after "
            f"{REQUEST_TIMEOUT} seconds"
        ) from e

    except requests.exceptions.RequestException as e:

        raise RuntimeError(
            f"Prometheus request failed: {str(e)}"
        ) from e

    # HTTP-level failure
    try:
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:

        raise RuntimeError(
            f"Prometheus returned HTTP {response.status_code}"
        ) from e

    # JSON parsing failure
    try:
        data = response.json()

    except ValueError as e:

        raise RuntimeError(
            "Prometheus returned an invalid JSON response"
        ) from e

    # Prometheus API-level failure
    if data.get("status") != "success":

        raise RuntimeError(
            f"Prometheus query failed: {data}"
        )

    return data


def query_prometheus_range(promql, start_time, end_time, step="60s"):
    """
    Execute a PromQL range query against Prometheus.

    Returns all metric samples between start_time and end_time.
    """

    url = f"{PROMETHEUS_URL}/api/v1/query_range"

    params = {
        "query": promql,
        "start": start_time,
        "end": end_time,
        "step": step
    }

    response = requests.get(
        url,
        params=params,
        timeout=REQUEST_TIMEOUT
    )

    response.raise_for_status()

    data = response.json()

    if data.get("status") != "success":
        raise ValueError(
            f"Prometheus range query failed: {data}"
        )

    return data