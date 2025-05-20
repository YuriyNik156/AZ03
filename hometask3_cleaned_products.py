# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

import csv

def clean_sofa_price(sofa_price):
    # Удаляем "₽/мес." и преобразуем в число
    cleaned = sofa_price.replace('руб.', '').replace(' ', '').strip()
    if cleaned == '':
        raise ValueError("Пустая строка вместо цены")
    return int(cleaned)

# Чтение данных из исходного CSV файла и их обработка
input_file = 'products.csv'
output_file = 'cleaned_products.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        try:
            clean_row = [clean_sofa_price(row[0])]
            writer.writerow(clean_row)
        except ValueError as e:
            print(f"Пропущена строка: {row} — {e}")

print(f"Обработанные данные сохранены в файл {output_file}")