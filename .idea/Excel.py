import xlrd
import pprint

def get_data():

    excel = xlrd.open_workbook('~/Python/lec3/Excel/Взносы.xls')
    sheet = excel.sheet_by_index(0)

    row_number = sheet.nrows

    table = {}

    if not row_number == 0:
        table = {sheet.row(i)[0]:sheet.row(i)[1] for i in range(0,row_number)}
    else:
        print('Указанный файл не заполнен')

    pprint.pprint(table)

get_data()
