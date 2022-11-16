import demjson
import xlwt
import pandas as pd

def try_excel():
    json_result = demjson.decode_file('data_case_info.json', encoding='utf-8')
    transform_list = list(json_result['contents'])
    pf = pd.DataFrame(transform_list)
    print(pf)
    file_path = pd.ExcelWriter('name.xlsx')
    pf.to_excel(file_path, encoding='utf-8')
    file_path.save()


try_excel()
