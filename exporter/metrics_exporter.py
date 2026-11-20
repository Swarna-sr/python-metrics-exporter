from prometheus_client import Counter, Gauge, start_http_server
import time

# Define application metrics
REQUEST_COUNT = Counter(
    'metrics_exporter_requests_total',
    'Total number of requests processed'
)

APP_STATUS = Gauge(
    'metrics_exporter_up',
    'Application status'
)


def update_metrics():
    REQUEST_COUNT.inc()
    APP_STATUS.set(1)


def main():
    # Start metrics server on port 8000
    start_http_server(8000)

    print("Metrics exporter running on port 8000")

    while True:
        update_metrics()
        time.sleep(5)


if __name__ == "__main__":
    main()