def print_to_console(text: str) -> None:
    """
    Виводить текст у консоль (стандартний вивід).

    Args:
        text (str): Текст для виведення.

    Example:
        >>> print_to_console("Hello!")
        Hello!
    """
    print(text)


def write_to_file(text: str, filepath: str) -> None:
    """
    Записує текст до файлу за допомогою
    вбудованих можливостей Python.

    Args:
        text (str): Текст для запису.
        filepath (str): Шлях до файлу для запису.
                        Якщо файл не існує — буде створений.

    Example:
        >>> write_to_file("Hello!", "data/output.txt")
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)