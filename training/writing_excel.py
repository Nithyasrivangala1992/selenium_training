from openpyxl import Workbook

from training.reading_excel import worksheet

##create the new excel workbook
workbook = Workbook()
##intialize the worksheet
worksheet = workbook.active
##set the title for the worksheet(optional)
worksheet.title = 'M16_data'
##write the data into the excel file
worksheet['A1'] = 'name'
worksheet['B1'] = 'place'
worksheet['C1'] = 'phone number'
worksheet['D1'] = 'email_id'
print(worksheet.values)
data = [
    ['Nithya','Nizamabad',9908431679,'nithya@gmail.com'],
    ['Manhita','Hyderabad',8456712564,'Mannhita@gmail.com'],
    ['Sudheer','Bangalore',9490984622,'sudheer@gmail.com'],
    ['Padmalatha','Nizamabad',9000490132,'Padma@gmail.com'],
    ['Laxmana chary','Nizamabad',9573328587,'chary@gmail.com'],
    ['Rahul','Nizamabad',9550524020,'rahul@gmail.com']
]
for ele in data:
    worksheet.append(ele)
##save the file
#workbook.save('M16.xlsx')
##To save the excel file in different location
workbook.save(r'C:\Users\91949\PycharmProjects\selenium_training\training\M16.xlsx')
