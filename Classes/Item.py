import sys


sys.stdout.reconfigure(encoding='utf-8')


class Item:
    def __init__(
        self,
        name: str,  # Название предмета
        description: str = '',  # Описание предмета
        use_text: str = 'Этот предмет красивый',
        rare: str = 'обычная',
    ):
        self.name = name
        self.description = description
        self.use_text = use_text
        self.rare = rare
        self.dict_rare = {
            'обычная': 1,
            'необычная': 1.1,
            'редкая': 1.3,
            'эпическая': 1.6,
            'легендарная': 1.8,
            'мифическая': 2
        }#бафы редкостей, потом изменить проценты


    def print_info_about_item(self):
        print('Имя предмета:', self.name)
        print(self.description)


    def use(self):
        print(self.use_text)