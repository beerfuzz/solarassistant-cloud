from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .coordinator import SolarAssistantCoordinator
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):

    coordinator = SolarAssistantCoordinator(
        hass,
        entry.data["url"],
        entry.data["cookies"],
        entry.data.get("scan_interval", 60),
    )

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setup(entry, "sensor")

    return True