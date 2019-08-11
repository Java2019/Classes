from ExcelClass import GetDataFromExcel
import pprint

Excel = GetDataFromExcel('~/Python/lec3/Excel/Взносы.xls')

pprint.pprint(Excel.get_data())

s = int(input('Enter the number: '))

while s < 0:
    s = int(input('Enter the number: '))

print(s + 3)
