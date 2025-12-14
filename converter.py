# Файл converter.py
# Автор: Жуков И.С.
# Вариант: 3
# Этот файл является частью проекта 'hello-engineer'

def run_converter():
    """
    Основная функция для запуска калькулятора систем счисления.
    Запрашивает число и исходную систему, выводит число в двух других системах.
    """
    print("\n--- Инженерный калькулятор систем счисления (Вариант 1) ---")
    
    mode = input("Выберите исходную систему (dec, bin, hex): ").strip().lower()
    
    number_str = input("Введите число для конвертации: ").strip()
    
    try:
        if mode == 'dec':
            dec_number = int(number_str)
            print(f"Двоичное (BIN): {bin(dec_number)}")
            print(f"Шестнадцатеричное (HEX): {hex(dec_number)}")
        
        elif mode == 'bin':
            dec_number = int(number_str, 2)
            print(f"Десятичное (DEC): {dec_number}")
            print(f"Шестнадцатеричное (HEX): {hex(dec_number)}")
        
        elif mode == 'hex':
            dec_number = int(number_str, 16)
            print(f"Десятичное (DEC): {dec_number}")
            print(f"Двоичное (BIN): {bin(dec_number)}")
        
        else:
            print("Ошибка: выбран неверный режим. Доступные режимы: dec, bin, hex.")

    except ValueError:
        print(f"Ошибка: Невозможно перевести '{number_str}' из системы '{mode}'. Проверьте корректность числа.")

if __name__ == "__main__":
    run_converter()