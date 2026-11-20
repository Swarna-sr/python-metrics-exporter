# Python Metrics Exporter

A basic Python application that exposes application metrics
in Prometheus format.

## Features

- Tracks application status.
- Tracks total request count.
- Exposes metrics over HTTP.
- Supports automated testing.
- Supports Jenkins CI/CD automation.

## Requirements

- Python 3
- prometheus-client

## Installation

pip install -r requirements.txt

## Run

python exporter/metrics_exporter.py

## Metrics Endpoint

http://localhost:8000/metrics

## Testing

python -m unittest discover -s tests -v