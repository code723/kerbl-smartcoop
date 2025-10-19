"""Config flow for Kerbl SmartCoop."""
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class KerblSmartCoopFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Kerbl SmartCoop", data=user_input)

        schema = vol.Schema({
            vol.Required("email"): str,
            vol.Required("password"): str
        })
        return self.async_show_form(step_id="user", data_schema=schema)
