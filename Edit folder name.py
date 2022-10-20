import os

address = 'D:/F盘/生成'
# 'D:/E盘/生成报告3'
# for filename in os.listdir('C:/Users/Serein/Desktop/Python-docx-Add-Image/folder'):
# filename =os.listdir(address)
# for i in range(10):
# os.makedirs(address + '/' + str(i))

txt_path = address + '列表' + '.txt'
txt_file = open(txt_path, 'w')


def file_rename():
    for filename in os.listdir(address):
        old_name = address + '/' + filename
        slicing = filename.split('_')
        print(slicing[0])
        txt_file.write(filename + '=')
        new_name = address + '/检材' + slicing[0]
        txt_file.write('检材' + slicing[0] + '\r\n')
        os.rename(old_name, new_name)


def main():
    file_rename()
    # txt_file.close()


main()
