from parser import Parser

FILE_FOR_PARSE = "./txt_files/PythonTest.txt"
SAVE_RU = "./txt_files/Russian.txt"
SAVE_EN = "./txt_files/English.txt"

if __name__ == '__main__':
    # Set information
    parser = Parser(link=FILE_FOR_PARSE, link_of_en_file=SAVE_EN, link_of_ru_file=SAVE_RU)

    # Saving two files
    parser.save()

