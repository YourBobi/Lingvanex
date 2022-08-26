import pandas as pd
import warnings


class Parser:
    link: str
    link_of_en_file: str
    link_of_ru_file: str
    data: pd.DataFrame = pd.DataFrame(columns=['en', 'ru'])

    def __init__(self, link: str, link_of_en_file: str = "./English.txt", link_of_ru_file: str = "./Russian.txt"):
        """
        Constructor

        :param link: link to the information file
        :param link_of_en_file: link to save Russian words
        :param link_of_ru_file: link to save English words
        """
        self.link = link
        self.link_of_en_file = link_of_en_file
        self.link_of_ru_file = link_of_ru_file
        self.set_data()

    def save(self):
        self.save_ru_file()
        self.save_en_file()

    def save_en_file(self):
        with open(self.link_of_en_file, 'w', encoding='utf-8') as file:
            file.write(self.data.iloc[:]['en'].to_string(index=False, header=False))

    def save_ru_file(self):
        with open(self.link_of_ru_file, 'w', encoding='utf-8') as file:
            file.write(self.data.iloc[:]['ru'].to_string(index=False, header=False))

    def set_data(self):
        """
        Saving words in pandas.Dataframe  for next work

        :return: self.data
        """
        warnings.filterwarnings("ignore")
        self.data = pd.DataFrame(columns=['en', 'ru'])

        with open(self.link, 'r', encoding='utf-8') as file:
            for row in file:
                if row[0] != '#' and row != '\n':
                    x = row.strip('\n').split('\t')

                    if ";" in row:
                        en = set(x[0].split(' ; '), )
                        ru = set(x[1].split(' ; '), )

                        for ru_word in ru:
                            for en_word in en:
                                self.data = self.data.append({'en': en_word, 'ru': ru_word}, ignore_index=True)
                    else:
                        self.data = self.data.append({'en': x[0], 'ru': x[1]}, ignore_index=True)

        return self.data

    def __str__(self):
        return self.data.to_string()
