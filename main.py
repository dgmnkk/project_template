from app.io.input import read_from_console, read_from_file, read_from_file_pandas
from app.io.output import print_to_console, write_to_file


def main():
    console_text = read_from_console()
    file_text     = read_from_file("data/input.txt")
    pandas_text   = read_from_file_pandas("data/input.csv")

    print("\n=== З консолі ===")
    print_to_console(console_text)

    print("\n=== З файлу (python) ===")
    print_to_console(file_text)

    print("\n=== З файлу (pandas) ===")
    print_to_console(pandas_text)

    combined = "\n".join([console_text, file_text, pandas_text])
    write_to_file(combined, "data/output.txt")
    print("\n>>> Результати записано у data/output.txt")


if __name__ == "__main__":
    main()