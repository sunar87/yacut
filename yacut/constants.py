import string


LENGTH_UNIQUE_ID = 6
USER_INPUT_LIMIT = 16
VALID_SYMBOLS = string.ascii_letters + string.digits

NO_REQUEST_BODY = 'Отсутствует тело запроса'
REQUIRED_URL = '"url" является обязательным полем!'
ID_NOT_FOUND = 'Указанный id не найден'
NAME_IS_OCCUPIED = 'Предложенный вариант короткой ссылки уже существует.'
INVALID_NAME_FOR_LINK = 'Указано недопустимое имя для короткой ссылки'

NAME_IS_OCCUPIED_FLASH = 'Имя {custom_id} уже занято!'
REEXP_FOR_CUSTOM_ID = "^[a-zA-Z0-9]+$"
REEXP_FOR_URL = '^(http|https):'
