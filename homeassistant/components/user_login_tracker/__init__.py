from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers import service
import logging

DOMAIN = "user_activity_tracker"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    async def handle_user_login_event(event):
        _LOGGER.info("User login detected. Triggering automation.")
        
        await hass.async_add_executor_job(
            hass.states.set,
            f"{DOMAIN}.user_logged_in",
            "true"
        )

    hass.bus.async_listen('user_logged_in', handle_user_login_event)
    return True