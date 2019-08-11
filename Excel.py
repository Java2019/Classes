from ExcelClass import GetDataFromExcel
import pprint

Excel = GetDataFromExcel('~/Python/lec3/Excel/Взносы.xls')

pprint.pprint(Excel.get_data())
