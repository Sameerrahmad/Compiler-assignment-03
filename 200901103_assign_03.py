import xml.etree.ElementTree as ET
import openpyxl

# Parse the XML file
tree = ET.parse('200901103_assign_03.xml')
root = tree.getroot()
data = []
for book in root.findall('book'):
  book_data = {}
  book_data['Book_Id'] = book.get('id')
  book_data['Author_Name'] = book.find('author').text
  book_data['Title'] = book.find('title').text
  book_data['Genre'] = book.find('genre').text
  book_data['Price'] = book.find('price').text
  book_data['Publish_date'] = book.find('publish_date').text
  book_data['Description'] = book.find('description').text

  data.append(book_data)
# Creating a new Excel workbook
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(['Book_Id', 'Author_Name', 'Title', 'Genre', 'Price', 'Publish_date', 'Description'])
# Add the data for each book
for book in data:
  worksheet.append([book['Book_Id'], book['Author_Name'], book['Title'], book['Genre'], book['Price'], book['Publish_date'], book['Description']])
# Save the workbook
workbook.save('200901103_assign_03.xlsx')