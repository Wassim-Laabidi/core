# from homeassistant.core import HomeAssistant
# from homeassistant.helpers.typing import ConfigType
# import logging

# DOMAIN = "dynamic_dashboards"
# _LOGGER = logging.getLogger(__name__)

# async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
#     async def handle_get_dashboard(call):
#         user_id = call.context.user_id
#         _LOGGER.info(f"Service call received. User ID: {user_id}")

#         # Only set the dashboard URL if user_id is not None
#         if user_id:
#             dashboard_url = f"/lovelace-{user_id}/default_view"
#             hass.states.async_set(f"{DOMAIN}.dashboard_url", dashboard_url)
#             _LOGGER.info(f"Dashboard URL set to: {dashboard_url}")
#         else:
#             _LOGGER.warning("User ID is None. Dashboard URL not set.")

#     hass.services.async_register(DOMAIN, "get_dashboard", handle_get_dashboard)
#     return True
