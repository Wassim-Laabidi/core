from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import service

DOMAIN = "dynamic_dashboards"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    async def handle_get_dashboard(call):
        user_id = call.context.user_id
        dashboard_url = f"/lovelace-{{user}}/default_view"
        await hass.async_add_executor_job(
            hass.states.set,
            f"{DOMAIN}.dashboard_url",
            dashboard_url
        )

    hass.services.async_register(DOMAIN, "get_dashboard", handle_get_dashboard)
    return True
