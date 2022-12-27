import abc
import json
from os.path import exists
from typing import Any, Optional


class BaseStorage:
    @abc.abstractmethod
    def save_state(self, state: dict) -> None:
        """Сохранить состояние в постоянное хранилище"""
        pass

    @abc.abstractmethod
    def retrieve_state(self) -> dict:
        """Загрузить состояние локально из постоянного хранилища"""
        pass


class JsonFileStorage(BaseStorage):
    def __init__(self, file_path: Optional[str] = None):
        self.file_path = file_path

    def save_state(self, state: dict) -> None:
        """Сохранить состояние в постоянное хранилище"""
        if self.file_path:
            with open(self.file_path, 'w') as file:
                json.dump(state, file)

    def retrieve_state(self) -> dict:
        """Загрузить состояние локально из постоянного хранилища"""
        if self.file_path and exists(self.file_path):
            with open(self.file_path, 'r') as json_file:
                data = None
                try:
                    data = json.load(json_file)
                except ValueError:
                    pass
            return data
        else:
            return {}


class State:
    """
    Класс для хранения состояния при работе с данными, чтобы постоянно не перечитывать данные с начала.
    Здесь представлена реализация с сохранением состояния в файл.
    В целом ничего не мешает поменять это поведение на работу с БД или распределённым хранилищем.
    """

    def __init__(self, storage: BaseStorage):
        self.storage = storage

    def set_state(self, key: str, value: Any) -> None:
        """Установить состояние для определённого ключа"""
        current_state = self.storage.retrieve_state()
        current_state[key] = value
        self.storage.save_state(current_state)

    def get_state(self, key: str) -> Any:
        """Получить состояние по определённому ключу"""
        current_state = self.storage.retrieve_state()
        return current_state.get(key)


demo_dict = {'first_name': 'user', 'last_name': 'last_demo_name'}

json_class = JsonFileStorage('state2.json')
# json_class.save_state(demo_dict)
print(json_class.retrieve_state())

state_instance = State(json_class)
print(state_instance.get_state('first_name'))
print(state_instance.set_state('first_name', 'TEST'))

json_class_2 = JsonFileStorage()
state_instance_2 = State(json_class_2)
print(state_instance.get_state('first_name'))
print(state_instance.set_state('first_name', 'TEST'))
print(json_class_2.retrieve_state())
