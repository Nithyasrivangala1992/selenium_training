'''
xlrd    :   To read excel files, we use xlrd

To install xlrd
    Go to command --> pip install xlrd==1.2.0

STEPS TO READ EXCEL FILE
    • import xlrd
    • open the workbook
    workbook = xlrd.open_workbook(“path_of_excel_file”)
    • open the worksheet
    worksheet = workbook.sheet_by_name(“SheetName”)
    • Convert sheet object to the generator object
    rows = worksheet.get_rows()
    • Traverse/ use next() on the generator object to fetch the data

• open_workbook :   Opens an existing Excel workbook for reading data.
                    Returns the book object
                    A Book object, represents the opened Excel file.


• sheet_by_name :   We can access a specific sheet in an Excel workbook using the sheet name.
                    Returns the sheet object


• get_rows() :      Used to retrieve all rows from a worksheet as an iterator of row objects.
                    Each row contains a list of cell objects, which can be accessed for their values.
                    Each iteration gives list of Cell objects representing one row.
                    You can access the cell value with .value.

'''
from wsgiref.validate import header_re

import xlrd
## open the excel file
path = r'C:\Users\91949\Desktop\python seleniumM16\sample.xlsx'
workbook = xlrd.open_workbook(path)
print(workbook)                          ## Book object

## open the worksheet
worksheet = workbook.sheet_by_name('candidates_data')
print(worksheet)                         ## Sheet object

## convert the sheet object to the generator object
rows = worksheet.get_rows()
print(rows)                               ## generator object
header = next(rows)
#for ele in rows:
#     print(ele)

# for ele in rows:
#     print(ele[0], ele[1], ele[2], ele[3])

for ele in rows:
    print(ele[0].value, ele[1].value, ele[2].value, ele[3].value)



