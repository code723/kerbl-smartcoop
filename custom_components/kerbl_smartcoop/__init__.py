"""Kerbl SmartCoop Integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .const import DOMAIN

# Definiere, welche Plattformen deine Integration nutzt
PLATFORMS: list[Platform] = [Platform.SENSOR, Platform.SWITCH]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setup einer neuen Integration-Instanz."""
    hass.data.setdefault(DOMAIN, {})

    # Hier später deinen API-Client initialisieren, falls nötig
    # client = KerblApiClient(entry.data["email"], entry.data["password"])
    # hass.data[DOMAIN][entry.entry_id] = client

    # Starte die Plattformen (Sensor, Switch, ...)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Entfernt Entities beim Entladen."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok


async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Ermöglicht ein Reload ohne Neustart."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
