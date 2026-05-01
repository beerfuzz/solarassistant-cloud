import requests
import logging
from datetime import timedelta
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

_LOGGER = logging.getLogger(__name__)

class SolarAssistantCoordinator(DataUpdateCoordinator):

    def __init__(self, hass, url, solar_key, site_key, scan_interval):
        self.url = url
        self.cookies = {
            "_solar_assistant_key": solar_key,
            "site_key": site_key,
           }

        super().__init__(
            hass,
            _LOGGER,
            name="SolarAssistant",
            update_interval=timedelta(seconds=scan_interval),
        )

    def _parse_cookie_string(self, cookie_string):
        cookies = {}
        for item in cookie_string.split(";"):
            if "=" in item:
                k, v = item.strip().split("=", 1)
                cookies[k] = v
        return cookies

    async def _async_update_data(self):
        query = (
            'SELECT last("combined") FROM "Battery power";'
            'SELECT last("combined") FROM "Battery SOC";'
            'SELECT last("combined") FROM "Grid power";'
            'SELECT last("combined") FROM "Load power"'
        )

        url = f"{self.url}/grafana/api/datasources/proxy/1/query?db=solar_assistant&q={requests.utils.quote(query)}&epoch=ms"

        try:
            resp = requests.get(url, cookies=self.cookies, timeout=10)

            if resp.status_code != 200:
                raise UpdateFailed(f"HTTP {resp.status_code}")

            # 🔴 Detect expired session
            if "Sign in" in resp.text:
                self.hass.services.call(
                    "persistent_notification",
                    "create",
                    {
                        "title": "SolarAssistant Cookie Expired",
                        "message": "Your SolarAssistant session cookie has expired. Please update it."
                    }
                )
                raise UpdateFailed("Authentication expired")

            data = resp.json()

            def get_val(i):
                try:
                    return data["results"][i]["series"][0]["values"][0][1]
                except:
                    return None

            return {
                "battery_power": get_val(0),
                "battery_soc": get_val(1),
                "grid_power": get_val(2),
                "load_power": get_val(3),
            }

        except Exception as e:
            raise UpdateFailed(str(e))