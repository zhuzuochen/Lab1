import re
import csv

def part1():
    with open('task1-en.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("=== Часть 1 ===")
    
    pattern1 = r'\b[0-9]\b'
    numbers_less_than_10 = re.findall(pattern1, text)
    print("Все целые числа меньше 10:")
    print(numbers_less_than_10)
    
    pattern2 = r'\b(?=.*[a-zA-Zа-яА-Я])(?=.*\d)[a-zA-Zа-яА-Я\d]+\b'
    alphanumeric = re.findall(pattern2, text)
    print("\nВсе сочетания с буквами и цифрами:")
    print(alphanumeric)

def part2():
    with open('task2.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    print("\n=== Часть 2 ===")
    
    pattern = r'https?://[^"\'\s]+\.(?:jpg|jpeg|png|gif|bmp|svg|webp)(?:\?[^"\'\s]*)?'
    image_links = re.findall(pattern, html, re.IGNORECASE)
    
    print("Все ссылки на изображения:")
    for link in image_links:
        print(link)

def part3():
    with open('task3.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    id_pattern = re.compile(r'\b\d{1,20}\b')
    surname_pattern = re.compile(r'\b[A-Za-zА-Яа-яёЁ]+\b')  
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    date_pattern = re.compile(r'\b(\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})\b')
    site_pattern = re.compile(r'\bhttps?://[^\s]+\b')

    ids = list(dict.fromkeys(id_pattern.findall(content)))
    surnames = list(dict.fromkeys(surname_pattern.findall(content)))
    emails = list(dict.fromkeys(email_pattern.findall(content)))
    dates = list(dict.fromkeys(date_pattern.findall(content)))
    sites = list(dict.fromkeys(site_pattern.findall(content)))

    min_len = min(len(ids), len(surnames), len(emails), len(dates), len(sites))

    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Surname', 'Email', 'Registration Date', 'Website'])
        for i in range(min_len):
            writer.writerow([ids[i], surnames[i], emails[i], dates[i], sites[i]])

    print(f"\n=== Часть 3 завершена ===")
    print(f"Извлечено записей: {min_len}")
    print("Сохранено в output.csv")

def extra():
    with open('task_add.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n=== Дополнительная часть ===")
    
    date_pattern = r'(?<=\s)(?:\d{4}[-/.]\d{1,2}[-/.]\d{1,2}|\d{1,2}[-/.]\d{1,2}[-/.]\d{4})'
    dates = re.findall(date_pattern, content)
    
    email_pattern = r'(?<=\s)[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
    emails = re.findall(email_pattern, content, re.IGNORECASE)
    
    website_pattern = r'(?<=\s)https?://[^\s]+'
    websites = re.findall(website_pattern, content)
    
    print(f"Найдено дат: {len(dates)}")
    for i, date in enumerate(dates[:5], 1):
        print(f"  {i}. {date}")
    
    print(f"\nНайдено email: {len(emails)}")
    for i, email in enumerate(emails[:5], 1):
        print(f"  {i}. {email}")
    
    print(f"\nНайдено сайтов: {len(websites)}")
    for i, website in enumerate(websites[:5], 1):
        print(f"  {i}. {website}")

if __name__ == "__main__":
    part1()
    part2()
    part3()
    extra()