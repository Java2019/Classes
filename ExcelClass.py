import xlrd


class GetDataFromExcel:

    def __init__(self, val=''):
        self.val = val

    def get_data(self) -> dict:

        excel = xlrd.open_workbook(self.val)
        sheet = excel.sheet_by_index(0)

        row_number = sheet.nrows

        table = dict()

        if not row_number == 0:
            table = {sheet.row(i)[0]: sheet.row(i)[1] for i in range(0, row_number)}
        else:
            print('Указанный файл не заполнен')

        return table
