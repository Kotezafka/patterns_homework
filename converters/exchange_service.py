import os
import time
import json
import logging
from typing import Dict, Optional

import requests


class ExchangeRateService:
    def __init__(
        self, base_url: str = "https://api.exchangerate-api.com/v4/latest/USD"
    ):
        self.base_url = base_url
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def get_rates(self) -> Optional[Dict[str, float]]:
        try:
            response = requests.get(self.base_url, timeout=10)
            response.raise_for_status()
            return response.json().get("rates")

        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to fetch rates: {e}")
            return None
