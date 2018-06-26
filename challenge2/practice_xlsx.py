import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

for value in range(1, 101):
    worksheet.write('A'+str(value), value)

workbook.close()