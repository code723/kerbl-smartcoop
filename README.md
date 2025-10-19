# Kerbl SmartCoop Home Assistant Integration

Diese Integration bindet den **Kerbl SmartCoop Stallcontroller** in Home Assistant ein.

## Installation

1. [HACS](https://hacs.xyz) installieren.
2. In HACS → Integrationen → Custom Repositories:
   - URL: `https://github.com/deinuser/kerbl-smartcoop`
   - Kategorie: `Integration`
3. Danach die Integration "Kerbl SmartCoop" installieren.
4. Home Assistant neu starten.
5. Unter **Einstellungen → Integrationen** nach "Kerbl SmartCoop" suchen und mit deinen Zugangsdaten verbinden.

## Entwicklung
- API-Client wird über `aiohttp` umgesetzt.
- Entities: Türsteuerung, Fütterung, Temperatur, Luftfeuchtigkeit.
