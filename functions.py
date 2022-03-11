import time

from selenium.webdriver.common.by import By
import selenium.common.exceptions

# Функция проверки открытого чата
def check_for_url(driver):
    # Бесконечный цикл, из которого выход после нахождения окна чата
    while True:
        # Обработка исключений
        # Если чат не будет найден, то функция find_element_by_class_name выдаст исключение
        try:
            # поиск элемента с классом MessageList
            driver.find_element(By.CLASS_NAME, 'MessageList')
            # Если исключение не сработалоЮ то выход из цикла
            break
        
        except selenium.common.exceptions.NoSuchElementException:
            # Запись в консоль, что чат не открыт
            print('Is not opened')
            # Задержка обновления в 2 секунды
            time.sleep(2)
    
    # Если чат открыт, то запись в консоль и выход из функции
    print('chat is opened')
    return

# Функция нажатия на стрелку "Новых сообщений"
def wait_for_new_messagesses(driver):
    while True:
        try:
            # Поиск в DOM кода элемента стрелки и выход из цикла, если найдено
            driver.find_element(By.CLASS_NAME, 'ScrollDownButton')
            break
        
        # Пока не найдено, будет вызываться исключение. Пропуск его.
        except selenium.common.exceptions.NoSuchElementException:
            pass
    
    # Сохранение элемента для клика
    scroll_btn = driver.find_element(By.CLASS_NAME, 'ScrollDownButton')
    
    # Пока у кнопки есть класс "revealed" клик по ней
    # Этот класс означает, что кнопка видима и на неё можно нажать
    while not scroll_btn.get_attribute('class').find('revealed') == -1:
        try:
            scroll_btn.click()
        
        # Если не получается сделать клик на элемент и он исчез,
        # то выход из функции
        # except selenium.common.exceptions.ElementClickInterceptedException:
        except:
            return

# Функция проверки канала/группы на то, что достигнуто его начало
def is_channes_beginning(driver):
    try:
        element = driver.find_element(By.CLASS_NAME, 'ActionMessage')
        if element.get_attribute('data-message-id') == '1':
            print('Beginning of the [channel/group] found!')
            return True

    # except selenium.common.exceptions.NoSuchElementException:
    except:
        return False

    return False

# Отправление в браузер JS скрипт, который скроллит область сообщений на заданное кол-во px/%

def exec_scroll(driver, type, value):
    if type == 'percent':
        code = """
            var af_height = document.getElementsByClassName("MessageList")[0].scrollTop;
            var af_scroll_len = af_height - (af_height / {});
            document.getElementsByClassName('MessageList')[0].scrollTo(0, af_scroll_len);
        """.format(value / 100)
        print(value / 100)
        driver.execute_script(code)
        return True
    
    elif type == 'pixel':
        code = """
            var af_height = document.getElementsByClassName("MessageList")[0].scrollTop;
            var af_scroll_len = af_height - {};
            document.getElementsByClassName('MessageList')[0].scrollTo(0, af_scroll_len);
        """.format(value)
        driver.execute_script(code)
        return True
    
    else:
        return False    
        
# Функция скролла чата
def scroll_to_top(driver, limit, settings):
    
    # Коллекция сообщений
    msg_set = dict()

    # Условие, при котором заканчивается скролл
    
    while len(msg_set) < limit:
        for el in driver.find_elements(By.CLASS_NAME, 'message-list-item'):
        
            try:
                if not (el.get_attribute('id')) in msg_set:
                    msg_set[str(el.get_attribute('id'))] = el.get_attribute('innerHTML')
                    
                    temp = el.find_element(By.CLASS_NAME, 'content-inner')
                    
                    print("test")
                    print(temp.get_attribute('innerHTML'))
                    print("test2")
                    
                    # msg_set[str(el.get_attribute('id'))] = element.get_attribute('innerHTML');
            except Exception as error:
                print('Error of getting message\n{}'.format(error))
                continue
    
        # Вызов функции скролла
        if not exec_scroll(driver, settings['type'], settings['value']):
            print('Unexceptable scroll error. [Type/Value] undefined')
            
        # Если достигнуто начала канала, то выход из него, прекращая скролл, и переход к следующему этапу
        if is_channes_beginning(driver):
            break
            
        print ( len(msg_set) )    
    
    # Возвращение из функции результат — словарь сообщений
    print('$' * 40, '\n' , 'Scroll was success')
    return msg_set

# Функция сохранения сообщений в файлы
def save_messages(path, filename, format, elems):
    
    error_counter = {
        'TypeError' : 0,
        'SavingError' : 0,
        'OtherError' : 0
    }
    
    try:
        for id in elems:
            try:
                path_to_file = path + filename + '_' + id + '.' + format
                
                with open(path_to_file, 'ab') as w_file:
                    w_file.write(elems[id].encode('utf-8'))
            except:
                error_counter['SavingError'] += 1
                continue
            
    except TypeError:
        error_counter['TypeError'] += 1
    except:
        error_counter['OtherError'] += 1
    
    # Бэклог ошибок
    for key in error_counter:
        print('There was {} of "{}" exceptions from {} messages' . format(error_counter[key], key, len(elems)))