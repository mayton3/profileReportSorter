import csv

input_file = 'report.txt'
output_file = 'report_sorted.csv'

# Функция для проверки, что строка с данными (пропускаем заголовок и пустые строки)
def is_data_line(line):
    # Простая проверка: строка должна содержать хотя бы два числа и поле filename:function
    parts = line.strip().split()
    if len(parts) < 6:
        return False
    # Проверим, что второй столбец можно преобразовать в число (tottime)
    try:
        float(parts[1])
        return True
    except ValueError:
        return False

data = []

with open(input_file, 'r') as f:
    for line in f:
        if is_data_line(line):
            parts = line.strip().split(None, 5)  # Разделяем на 6 частей (последняя - filename:lineno(function))
            ncalls = parts[0]
            tottime = float(parts[1])
            percall = parts[2]
            cumtime = parts[3]
            percall2 = parts[4]
            location = parts[5]
            data.append([ncalls, tottime, percall, cumtime, percall2, location])

# Сортировка данных по tottime по убыванию, если нужно по возрастанию - ascending=True
data.sort(key=lambda x: x[1], reverse=False)

# Запись в CSV
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    # Запишем заголовок
    writer.writerow(['ncalls', 'tottime', 'percall', 'cumtime', 'percall2', 'filename:lineno(function)'])
    # Запишем отсортированные данные
    writer.writerows(data)
