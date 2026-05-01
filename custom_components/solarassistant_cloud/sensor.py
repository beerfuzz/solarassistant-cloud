from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import DeviceInfo

DOMAIN = "solarassistant_cloud"

async def async_setup_entry(hass, entry, async_add_entities):

    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []

    for key in coordinator.data.keys():
        entities.append(SolarAssistantSensor(coordinator, key))

    async_add_entities(entities)


class SolarAssistantSensor(CoordinatorEntity, SensorEntity):

    def __init__(self, coordinator, key):
        super().__init__(coordinator)
        self.key = key

    @property
    def name(self):
        return f"SolarAssistant {self.key.replace('_', ' ').title()}"

    @property
    def unique_id(self):
        return f"solarassistant_{self.key}"

    @property
    def state(self):
        return self.coordinator.data.get(self.key)

    @property
    def device_info(self) -> DeviceInfo:
        return {
            "identifiers": {(DOMAIN, "solarassistant_cloud")},
            "name": "SolarAssistant Cloud",
            "manufacturer": "SolarAssistant",
            "model": "Cloud API",
        }