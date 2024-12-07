from attr import attr
from attrs import define


@define
class Identifiable:
    _id: int = attr(default=0)
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id