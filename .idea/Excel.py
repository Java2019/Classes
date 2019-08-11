import xlrd

def get_data():

    excel = xlrd.open_workbook('~/Python/lec3/Excel/Взносы.xls')
    sheet = excel.sheet_by_index(0)

    row_number = sheet.nrows

    table = []

    if not row_number == 0:
        table = [str(sheet.row(i)[0]) for i in range(0,row_number)]
        #for i in range(0, row_number):
        #    table.append(str(sheet.row(i)[0]))
    else:
        print('Указанный файл не заполнен')

    print(table)


get_data()
