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
        # Dynamically find the relevant browser_user sensor
        all_entities = hass.states.async_all()
        current_user_id = None

        for entity in all_entities:
            if entity.entity_id.startswith('sensor.') and 'browser_user' in entity.entity_id:
                user_data = entity.attributes.get('userData', {})
                if user_data:
                    current_user_id = user_data.get('id')
                    break
        
        if not current_user_id:
            return  # Exit if no valid user ID is found

        # Create the entity with the current user's ID as the owner
        entity_name = call.data['entity_name']
        entity = UserEntity(username=current_user_id, name=entity_name)
        component.add_entities([entity])

    # Register the service with Home Assistant
    hass.services.async_register(DOMAIN, "create_entity", handle_create_entity)
    return True

class UserEntity(Entity):
    def __init__(self, username, name):
        self._username = username
        self._name = name
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return f"{self._username}_{self._name}"

    @property
    def device_state_attributes(self):
        return {
            "created_by": self._username
        }
    
    @property
    def state(self):
        return self._state

    async def async_update(self):
        # Logic for updating the entity's state
        pass
