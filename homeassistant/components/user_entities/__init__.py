import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_USERNAME
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_component import EntityComponent

DOMAIN = "user_entities"

async def async_setup(hass: HomeAssistant, config: dict):
    component = EntityComponent(hass, DOMAIN, DOMAIN)
    
    @callback
    def handle_create_entity(call):
        current_user = call.context.user_id  # Get the current user's ID
        username = call.data[CONF_USERNAME]
        
        if current_user != username:
            return  # Do not create the entity if it belongs to a different user
        
        entity_name = call.data['entity_name']
        entity = UserEntity(username, entity_name)
        component.add_entities([entity])


class UserEntity(Entity):
    def __init__(self, username, name):
        self._username = username
        self._name = name
        self._state = None

    @property
    def name(self):
        return f"{self._username}_{self._name}"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        # Add logic for updating the entity state
        pass
