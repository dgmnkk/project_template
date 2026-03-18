import pandas as pd


def read_from_console() -> str:
    """
    Зчитує текст із консолі (стандартний ввід).

    Returns:
        str: Рядок, введений користувачем.

    Example:
        >>> text = read_from_console()
        Введіть текст: Hello
        >>> print(text)
        Hello
    """
    text = input("Введіть текст: ")
    return text


def read_from_file(filepath: str) -> str:
    """
    Зчитує вміст текстового файлу за допомогою
    вбудованих можливостей Python.

    Args:
        filepath (str): Шлях до файлу для читання.

    Returns:
        str: Вміст файлу у вигляді рядка.

    Raises:
        FileNotFoundError: Якщо файл не знайдено.

    Example:
        >>> text = read_from_file("data/input.txt")
        >>> print(text)
        Hello from file
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def read_from_file_pandas(filepath: str) -> str:
    """
    Зчитує вміст CSV-файлу за допомогою бібліотеки pandas.

    Args:
        filepath (str): Шлях до CSV-файлу для читання.

    Returns:
        str: Рядкове представлення DataFrame.

    Raises:
        FileNotFoundError: Якщо файл не знайдено.

    Example:
        >>> text = read_from_file_pandas("data/input.csv")
        >>> print(text)
           name  age
        0  Alice   30
    """
    df = pd.read_csv(filepath)
    return df.to_string()