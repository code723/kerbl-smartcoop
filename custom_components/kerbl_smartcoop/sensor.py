"""Example sensor for Kerbl SmartCoop."""
from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities([KerblSmartCoopSensor()])

class KerblSmartCoopSensor(SensorEntity):
    _attr_name = "Kerbl Coop Temperatur"
    _attr_native_unit_of_measurement = "°C"

    @property
    def native_value(self):
        return 22.5
