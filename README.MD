# Тестовое задание

## Парсер файла

Для парсинга файла был разработан класс, который содержит следующие атрибуты:

1. self.data - DataFrame с двумя колонками("en"- английское слово "ru"- перевод);
2. self.link - путь к файлу со словами;
3. link_of_en_file - путь для сохранения файла с en словами;
4. link_of_ru_file - путь для сохранения файла с ru словами.

### Пример создания объекта Parser
```python
from parser import Parser
parser = Parser(link="./PythonTest.txt", link_of_en_file="./Russian.txt", link_of_ru_file="./Russian.txt")
```
или 
```python
from parser import Parser
parser = Parser(link="./PythonTest.txt")
```

### Сохранение файлов
```python
parser.save()
```

### Вывести содержимое объекта в консоль
```python
print(parser)
```