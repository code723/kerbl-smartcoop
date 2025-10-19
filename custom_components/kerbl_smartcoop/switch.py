"""Switch platform for Kerbl SmartCoop."""
from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up Kerbl SmartCoop switches from config entry."""
    switches = [
        KerblSmartCoopDoorSwitch(),
        KerblSmartCoopFeederSwitch(),
    ]
    async_add_entities(switches)


class KerblSmartCoopDoorSwitch(SwitchEntity):
    """Beispiel-Schalter für die Türsteuerung."""

    _attr_name = "Kerbl Coop Tür"
    _attr_icon = "mdi:door"

    def __init__(self):
        self._is_on = False

    @property
    def is_on(self):
        return self._is_on

    async def async_turn_on(self, **kwargs):
        # Später: API call zum Tür öffnen
        self._is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        # Später: API call zum Tür schließen
        self._is_on = False
        self.async_write_ha_state()


class KerblSmartCoopFeederSwitch(SwitchEntity):
    """Beispiel-Schalter für die Fütterung."""

    _attr_name = "Kerbl Coop Fütterung"
    _attr_icon = "mdi:food-drumstick"

    def __init__(self):
        self._is_on = False

    @property
    def is_on(self):
        return self._is_on

    async def async_turn_on(self, **kwargs):
        # Später: API call zum Futter auslösen
        self._is_on = True
        self.async_write_ha_state()
        # optional nach kurzer Zeit wieder ausschalten
        self._is_on = False
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        # Für diesen Schalter nicht unbedingt nötig
        self._is_on = False
        self.async_write_ha_state()
