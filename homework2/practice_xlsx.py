import xlsxwriter

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

for value in range(1, 51):
    worksheet.write('A'+str(value), 'A'+str(value))
    worksheet.write('B'+str(value), 'B'+str(value))
    worksheet.write('C'+str(value), 'C'+str(value))
    worksheet.write('D'+str(value), 'D'+str(value))

workbook.close()