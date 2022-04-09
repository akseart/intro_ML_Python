 # Функция 1
def foo(a, b):
    """Данная функция суммирует два числа."""
    return a + b


a = """sdfsdfdsf sdfsdf
sdfsdfsdf
# это не комментарий
"""

b = "# sdfsdfds"

# Функция 2
def foo_2(a, b):
    """Данная функция умножает два числа.
    
    Args:
        a (int): первый операнд.
        b (int): второй операнд.
    """
    res = a * b # Умножаем два числа
    return res
