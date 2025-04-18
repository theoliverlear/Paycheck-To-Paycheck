from datetime import date

from attrs import define

from backend.apps.models.date_utilities import iso_to_django_date


@define
class DictParser:
    def parse(self, dict_data: dict, key: str) -> str | int | float | date:
        normalized_key: str = self.camel_to_snake(key)
        if self.is_date_key(normalized_key):
            self.add_normalized_date_key(dict_data)
            return self.get_django_date(dict_data, normalized_key)
        return dict_data[normalized_key]

    def camel_to_snake(self, key: str) -> str:
        updated_string: str = ""
        for char in key:
            if char.isupper():
                updated_string += char.lower() + "_"
            else:
                updated_string += char.lower()
        print(updated_string)
        return updated_string

    def get_django_date(self, dict_data: dict, key: str) -> date:
        return iso_to_django_date(dict_data[key])

    def is_date_key(self, key: str) -> bool:
        date_in_key: bool = "date" in key
        return date_in_key

    def add_normalized_date_key(self, dict_data: dict, check_date_received: bool = True):
        if check_date_received:
            if 'date_received' in dict_data:
                if dict_data['date_received']:
                    return dict_data
        else:
            dict_data['due_date'] = dict_data['date']
            return dict_data