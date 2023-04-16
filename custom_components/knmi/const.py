"""Constants for knmi."""
from datetime import timedelta
from typing import Final

# API
API_CONF_URL: Final = "http://weerlive.nl/api/toegang/account.php"
API_ENDPOINT: Final = "http://weerlive.nl/api/json-data-10min.php?key={}&locatie={},{}"
API_TIMEOUT: Final = 10
API_TIMEZONE: Final = "Europe/Amsterdam"

# Base component constants.
NAME: Final = "KNMI"
DOMAIN: Final = "knmi"
VERSION: Final = "1.3.8"

# Defaults
DEFAULT_NAME: Final = NAME
SCAN_INTERVAL: timedelta = timedelta(seconds=300)
