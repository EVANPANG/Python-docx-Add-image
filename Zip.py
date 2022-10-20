import zipfile
import os

address = 'C:/Users/Serein/Desktop/Python-docx-Add-Image/folder'


def zipfiles(dirpath, outFullName):
    zipz = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        fpath = path.replace(dirpath, '')
        for filename in filenames:
            print(os.path.join(path, filename))
            zipz.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zipz.close()


def main():
    for dirname in os.listdir(address):
        full_address = (address + '/' + dirname)
        zipfiles(full_address, full_address + '.zip')


main()
