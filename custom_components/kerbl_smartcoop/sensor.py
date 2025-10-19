"""Sensor platform for Kerbl SmartCoop."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Kerbl SmartCoop sensors from config entry."""
    # Hier könntest du später echte API-Daten übergeben
    sensors = [
        KerblSmartCoopTemperatureSensor(),
        KerblSmartCoopHumiditySensor(),
    ]
    async_add_entities(sensors)


class KerblSmartCoopTemperatureSensor(SensorEntity):
    """Beispiel-Temperatursensor."""

    _attr_name = "Kerbl Coop Temperatur"
    _attr_native_unit_of_measurement = "°C"
    _attr_icon = "mdi:thermometer"

    @property
    def native_value(self):
        # Später: echten Wert aus API zurückgeben
        return 22.5


class KerblSmartCoopHumiditySensor(SensorEntity):
    """Beispiel-Luftfeuchtigkeitssensor."""

    _attr_name = "Kerbl Coop Luftfeuchtigkeit"
    _attr_native_unit_of_measurement = "%"
    _attr_icon = "mdi:water-percent"

    @property
    def native_value(self):
        # Später: echten Wert aus API zurückgeben
        return 60

