import xlrd
workbook = xlrd.open_workbook("E:\\model (4).xlsx")
name = workbook.sheet_names()
print(name)