import os

from docx import Document

address = 'C:/Users/Serein/Desktop/Python-docx-Add-Image/folder/'

path = 'C:/Users/Serein/Desktop/Python-docx-Add-Image/text1.txt'
txt_file = open(path, 'w')


def main():
    for files in os.listdir(address):
        doc = Document('C:/Users/Serein/Desktop/Python-docx-Add-Image/folder/' + files)
        print(address + files)
        tables = doc.tables
        searching_table(tables)


def searching_table(tables):
    try:
        for t in tables:
            rows = t.rows
            columns = t.columns
            rows_length = len(t.rows)
            columns_length = len(t.columns)
            for r_num in range(rows_length):
                r_content = []
                for r_cell in rows[r_num].cells:
                    r_content.append(r_cell.text)
                if r_content[2] == '群组名称':
                    group_name = r_content[3]
                if r_content[2] == '发送者账号':
                    sender_name = r_content[3]
                if r_content[2] == '发送时间':
                    send_time = r_content[3]
                if r_content[2] == '即时信息内容':
                    result = r_content[3]
                    link_x = result.find('https://1122.su/')
                    link_i = result.find('https://sohu.su/')
                    if link_x > -1 or link_i > -1:
                        txt_file.write('\n')
                        txt_file.write(group_name + '=' + sender_name + '=' + send_time + '=')
                        if link_x > -1:
                            text_x = 'https://1122.su/' + result[link_x + 16:link_x + 21]
                            txt_file.write(text_x + '=')
                            print(text_x)
                        if link_i > -1:
                            text = 'https://sohu.su/' + result[link_i + 16:link_i + 20]
                            txt_file.write(text + '=')
                            print(text)

    except:
        return


main()
