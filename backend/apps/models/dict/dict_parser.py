from datetime import date

from attrs import define

from backend.apps.models.date_utilities import iso_to_django_date


@define
class DictParser:
    def parse(self, dict_data: dict, key: str) -> str | int | float | date:
        if self.is_date_key(key):
            self.add_normalized_date_key(dict_data)
            return self.get_django_date(dict_data, key)
        return dict_data[key]

    def get_django_date(self, dict_data: dict, key: str) -> date:
        return iso_to_django_date(dict_data[key])

    def is_date_key(self, key: str) -> bool:
        return "date" in key

    def add_normalized_date_key(self, dict_data: dict):
        dict_data['due_date'] = dict_data['date']
        return dict_data