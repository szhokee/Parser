import bs4
import requests
import xml.etree.ElementTree as ET

main_url = 'https://trade59.ru/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
data = []

def get_soup(url):
    res = requests.get(url, headers=headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')

categories_page = get_soup(main_url + 'catalog.html?cid=7')
categories = categories_page.findAll('a', class_='cat_item_color')

for cat in categories:
    subcategories_page = get_soup(main_url + cat['href'])
    subcategories = subcategories_page.findAll('a', class_='cat_item_color')
    for subcat in subcategories:
        iphones_page = get_soup(main_url + subcat['href'])
        iphones = iphones_page.findAll('div', class_='items-list')
        for iphone in iphones:
            title = iphone.find('a')['title'].strip()
            price = iphone.find('div', class_='price').text.strip()
            url = iphone.find('a')['href'].strip()
            img = iphone.find('div', class_='image')['style'].split('url(')[1].split(')')[0].replace('/tn/', '/source/')
            
            item = ET.Element('item')
            ET.SubElement(item, 'title').text = title
            ET.SubElement(item, 'price').text = price
            ET.SubElement(item, 'url').text = main_url + url
            ET.SubElement(item, 'img').text = main_url + img
            
            data.append(item)

root = ET.Element('data')
for item in data:
    root.append(item)

tree = ET.ElementTree(root)

tree.write('iphones.xml', encoding='utf-8', xml_declaration=True)




#----------------------------------------------------------------------------------------------------------------------------------------

# import bs4
# import requests
# import xlsxwriter

# main_url = 'https://trade59.ru/'
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# data = [['Название', 'Цена', 'Ссылка', 'Картинка']]

# def get_soup(url):
#     res = requests.get(url, headers=headers)
#     return bs4.BeautifulSoup(res.text, 'html.parser')

# categories_page = get_soup(main_url + 'catalog.html?cid=7')
# categories = categories_page.findAll('a', class_='cat_item_color')

# for cat in categories:
#     subcategories_page = get_soup(main_url + cat['href'])
#     subcategories = subcategories_page.findAll('a', class_='cat_item_color')
#     for subcat in subcategories:
#         iphones_page = get_soup(main_url + subcat['href'])
#         iphones = iphones_page.findAll('div', class_='items-list')
#         for iphone in iphones:
#             title = iphone.find('a')['title'].strip()
#             price = iphone.find('div', class_='price').text.strip()
#             url = iphone.find('a')['href'].strip()
#             img = iphone.find('div', class_='image')['style'].split('url(')[1].split(')')[0].replace('/tn/', '/source/')
#             data.append([title, price, main_url + url, main_url + img])

# with xlsxwriter.Workbook('iphones.xlsx') as workbook:
#     worksheet = workbook.add_worksheet()

#     for row_num, info in enumerate(data):
#         worksheet.write_row(row_num, 0, info)


#----------------------------------------------------------------------------------------------------------------------------------------


# import bs4
# import requests
# import xlsxwriter

# main_url = 'https://trade59.ru/'
# headers = {'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
# data = [['Hаименование', 'Цена', 'Ссылка', 'Картинка' ]]

# def get_soup (url):
#     res = requests.get(url, headers)
#     return bs4. BeautifulSoup (res.text, 'html.parser')

# categories_page = get_soup(main_url+'catalog.html?cid=7')
# categories = categories_page.findAll('a', class_='cat_item_color')

# for cat in categories:
#     subcategories_page = get_soup (main_url+cat['href'])
#     subcategories = subcategories_page.findAll('a', class_='cat_item_color')
#     for subcat in subcategories:
#         iphones_page = get_soup (main_url+subcat['href'])
#         iphones = iphones_page.findAll('div', class_='items-list')
#         for iphone in iphones:
#             title = iphone.find('a')['title'].strip()
#             price = iphone.find('div', class_='price').find(text=True).strip()
#             url = iphone.find('a') [ 'href'].strip()
#             img = iphone.find('div', class_='image') [ 'style'].split('url(')[1].split(')')[0].replace('/tn/', '/source/')
#             data.append([title, price, main_url+url, main_url+img])

# with xlsxwriter. Workbook ('iphones.xlsx') as workbook:
#     worksheet = workbook.add_worksheet()

#     for row_num, info in enumerate (data):
#         worksheet.write_row(row_num, 0, info)
