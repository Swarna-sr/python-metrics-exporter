import os
import unittest

from prometheus_client import generate_latest

from exporter.metrics_exporter import (
    REQUEST_COUNT,
    APP_STATUS,
    update_metrics
)


class TestMetricsExporter(unittest.TestCase):

    def test_metrics_update(self):

        # Controlled failure for Jenkins demonstration
        if os.getenv("FORCE_TEST_FAILURE") == "1":
            self.fail("Intentional test failure for Jenkins demonstration")

        update_metrics()

        self.assertGreaterEqual(REQUEST_COUNT._value.get(), 1)

        self.assertEqual(APP_STATUS._value.get(), 1)

    def test_metrics_output(self):

        output = generate_latest().decode("utf-8")

        self.assertIn("metrics_exporter_requests_total", output)
        self.assertIn("metrics_exporter_up", output)


if __name__ == "__main__":
    unittest.main()