import demjson
import xlwt


def test_page():
    txt_file = open('D:/Python-docx-Add-Image/Json To Str/text.txt', 'w')
    result = demjson.decode_file('data_case_info.json', encoding='utf-8')
    txt_file.write(str(result))


def main():
    test_page()


main()
