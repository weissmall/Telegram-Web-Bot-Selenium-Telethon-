# Импорт для таймера (stdlib)
import time

# Основной драйвер Селениум
from selenium import webdriver
from functions import *


# Главная функция
def main():
    
    # @SCROLL_COUNT — Количество сообщений, при котором можно останавливать скролл
    # @SCROLL_SETTINGS — Настройки скроллинга. Либо мы скроллим в % соотношении от высоты поля
    #                   Либо мы скроллим на определенное количество пикселей
    # @TYPICAL_FILENAME — шаблон для имени файла, например "message"
    #                   В таком случае файлы будут называться message_***.FILEFORMAT
    # @TYPICAL_FILE_FORMAT — формат конечного файла(ов)
    # @PATH_TO_FILE — путь до папки, в которую будут сохранятся файлы
    # @HTML_DIVIDER — разделитель, который будет записываться после HTML-кода сообщения
    
    SCROLL_COUNT = 1000
    SCROLL_SETTINGS = {'type' : 'percent', 'value' : 50}
    # SCROLL_SETTINGS = {'type' : 'pixel', 'value' : 2000}
    
    TYPICAL_FILENAME = 'message'
    TYPICAL_FILE_FORMAT = 'txt'
    PATH_TO_FILE = 'folder/'
    
    # Создаем переменную с эмулированным Chrome
    driver = webdriver.Chrome('chromedriver.exe')  # Указываем путь до драйвера
    
    # Заходим по адресу get(addr) 
    driver.get('http://web.telegram.org/z/')
    
    # Запускаем функцию поиска чата
    check_for_url(driver)
    
    time.sleep(1)
    wait_for_new_messagesses(driver)
    elems = scroll_to_top(driver, SCROLL_COUNT, SCROLL_SETTINGS)
    save_messages(PATH_TO_FILE, TYPICAL_FILENAME, TYPICAL_FILE_FORMAT, elems)

# Если файл запущен как главный, то запускаем главную функцию
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exit program by pressing ^C')
        