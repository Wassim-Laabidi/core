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