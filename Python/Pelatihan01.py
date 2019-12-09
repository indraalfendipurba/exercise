import xlsxwriter

#import pandas as pd
#wb = openpyxl.Workbook()
#ws = wb.active
#ws['A1'] = 'Ini adalah kata dalam kolom A baris 1, dibuat pakai Python'
#wb.save('D:\Project\Python\Latihan\pelatihan1.xlsx')

wb = xlsxwriter.Workbook("Pelatihan1.xlsx")
ws = wb.add_worksheet()

