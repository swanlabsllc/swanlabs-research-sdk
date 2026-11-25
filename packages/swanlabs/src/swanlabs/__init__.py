"""Official public Python package for Swan Labs, LLC (https://swanlabs.si)."""

from __future__ import annotations

from dataclasses import dataclass
import json
import urllib.request
from typing import Any

__version__ = "0.0.1"
__all__ = ["__version__", "OrganizationMetadata", "ORGANIZATION", "fetch_public_status"]


@dataclass(frozen=True)
class OrganizationMetadata:
    """Public corporate metadata for Swan Labs, LLC."""

    legal_name: str
    website: str
    support_email: str
    partnerships_email: str


ORGANIZATION = OrganizationMetadata(
    legal_name="Swan Labs, LLC",
    website="https://swanlabs.si",
    support_email="info@swanlabs.si",
    partnerships_email="partnerships@swanlabs.si",
)


def fetch_public_status(endpoint: str = "https://swanlabs.si", timeout: float = 10.0) -> dict[str, Any]:
    """Check reachability of a public Swan Labs endpoint."""
    req = urllib.request.Request(
        endpoint,
        headers={"User-Agent": f"swanlabs-python/{__version__}"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        ctype = resp.headers.get("Content-Type", "")
        raw = resp.read().decode("utf-8", errors="replace")
        if "application/json" in ctype:
            return json.loads(raw)
        return {"ok": resp.status == 200, "status_code": resp.status, "url": endpoint}
