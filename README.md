
# Bitly
## Описание
Проект создан для сокращения или подсчета кликов по ссылке. Для получения сокращенной ссылки необходимо передать программе ссылку для сокращения. В ином случае, если вы хотите узнать сколько раз переходили по вашей сслыку, необходимо передать сокращенную ссылку.


## Запуск

Для запуска скрипта у вас уже должен быть установлен Python3.
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей.

## Скачайте код
Установите зависимости командой:
```python
  pip install -r requirements.txt
```
Запустить скрипт командой
```python
  python main.py --url $Ваша_Ссылка$
```

## Пример запуска скрипта
Для получения сокращенной ссылки, необходимо написать команду в таком формате:

```python
  python main.py --url https://translate.google.ru
```

Для получения количества кликов, необходимо написать команду в таком формате:

```python
  python main.py --url bit.ly/3uujaSR
```

## Переменные окружения
Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл .env рядом с main.py и запишите туда данные в таком формате: ПЕРЕМЕННАЯ=значение.

url - ссылки для работы кода, документацию можно найти на сайте [Сократить ссылку Bitly](https://gist.github.com/dvmn-tasks/58f5fdf7b8eb61ea4ed1b528b74d1ab5).

BITLINK_TOKEN - см токен на сайте [Bitly](https://app.bitly.com).

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
