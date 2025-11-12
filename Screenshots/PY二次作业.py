import csv, random
import xml.etree.ElementTree as ET

# csv read
with open('books-en.csv', encoding='cp1252') as f:
    rows = list(csv.DictReader(f, delimiter=';'))

# keys
TITLE_key = 'Book-Title'
author_key = 'Book-Author'
price_key = 'Price'
date_key = 'Year-Of-Publication'
publisher_key = 'Publisher'
downloads_key = 'Downloads'

# task1
count = sum(len(r[TITLE_key]) > 30 for r in rows)
print("ans1:", count)

# task2
author = input("author?:")
filtered = []
for r in rows:
    try:
        price_str = r[price_key].replace(',', '.')
        price = float(price_str)
        if author in r[author_key] and price >= 150:
            filtered.append(r)
    except ValueError:
        pass

print('ans2:', len(filtered))
for r in filtered[:3]:
    print(r[author_key], r[TITLE_key], r[price_key])


# task3
bibs = random.sample(rows, 20)
with open('bibliography.txt', 'w', encoding='utf-8') as f:
    for i, b in enumerate(bibs, 1):
        f.write(f"{i}. {b[author_key]}. {b[TITLE_key]} - {b[date_key]}\n")
print('file done')
input("press enter")

# xml
tree = ET.parse('currency.xml')
root = tree.getroot()
all_values = []
for val in root.findall('.//Valute'):
    value_text = val.find('Value').text
    value_num = float(value_text.replace(',', '.'))
    all_values.append(value_num)

avg_value = sum(all_values) / len(all_values) if all_values else 0

for val in root.findall('.//Valute'):
    value_text = val.find('Value').text
    value_num = float(value_text.replace(',', '.'))

    if int(val.find('Nominal').text) in (10, 500) and value_num > avg_value:
        print(f"{val.find('CharCode').text}: {value_num}")  


# extra task1
publishers = set()
for r in rows :
    publishers.add(r[publisher_key])

print("ans3:", len(publishers))
for pub in sorted(publishers)[:20]:
    print(pub)


# extra task2
books_with_downloads = []
for r in rows:
    try:
        downloads = int(r[downloads_key])
        books_with_downloads.append(r)
    except KeyError:
        pass
sorted_books = sorted(books_with_downloads, key=lambda x: int(x[downloads_key]) ,reverse=True)

 
print('ans4:', len(sorted_books[:20]))
for r in sorted_books[:20]:
    print(r[TITLE_key], r[author_key], r[downloads_key])