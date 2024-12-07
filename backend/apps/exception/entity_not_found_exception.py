from backend.apps.entity.identifiable import Identifiable


class EntityNotFoundException(Exception):
    DEFAULT_MESSAGE: str = 'Entity not found with ID: '
    def __init__(self, identifiable: Identifiable, message: str = DEFAULT_MESSAGE):
        type_string: str = str(type(identifiable))
        self.id_string: str = str(identifiable.id)
        self.message: str = f"{message} {type_string} - {self.id_string}"
        super().__init__(self.message)