from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
):

    coordinator = hass.data["solarassistant_cloud"][entry.entry_id]

    return {
    "url": entry.data.get("url"),
    "scan_interval": entry.data.get("scan_interval"),
    "last_data": coordinator.data,
    "cookies": "REDACTED"
}