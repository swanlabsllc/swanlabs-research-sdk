"""Official public Python SDK for Swan Labs, LLC (https://swanlabs.si)."""

from __future__ import annotations

import json
import urllib.request
from typing import Any

__version__ = "0.0.1"
__all__ = ["__version__", "SwanLabsPublicClient"]


class SwanLabsPublicClient:
    """Zero-dependency HTTP client for public Swan Labs verification and status endpoints."""

    def __init__(self, base_url: str = "https://swanlabs.si", timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    @property
    def version(self) -> str:
        return __version__

    def check_site_reachable(self) -> dict[str, Any]:
        req = urllib.request.Request(
            f"{self.base_url}/",
            headers={"User-Agent": f"swanlabs-sdk-python/{__version__}"},
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            ctype = resp.headers.get("Content-Type", "")
            raw = resp.read().decode("utf-8", errors="replace")
            if "application/json" in ctype:
                return json.loads(raw)
            return {"ok": resp.status == 200, "status_code": resp.status, "base_url": self.base_url}
