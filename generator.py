import argparse

class Text():
    def __init__(self, filename):
        self.train = filename

    def fit(self):
        # читаем из файла, парсим текст, генерим биграммы, lowercase - предобработка
        pass

    def generate(self, lenght: int):
        # генерируем новый текст длины lenght, создаем файл с новым текстом
        pass

def main():
    pass

if __name__ == '__main__':
    main()