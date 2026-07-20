import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def test_report_exists():
    """Success criterion 1: /app/report.json exists."""
    assert REPORT_PATH.is_file(), "no /app/report.json file found"


def test_report_schema():
    """Success criterion 2: the report has the exact JSON fields and types."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}
    assert type(report["total_requests"]) is int
    assert type(report["unique_ips"]) is int
    assert type(report["top_path"]) is str


def test_total_requests():
    """Success criterion 3: total_requests equals the six log records."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion 4: unique_ips equals the three distinct clients."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 5: top_path is the most-requested path."""
    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert report["top_path"] == "/index.html"
