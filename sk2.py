def main():
    # Списки для хранения первых 100 и последних 100 строк
    first_lines = []
    last_lines = []

    print("Введите текст (для окончания ввода введите пустую строку):")

    while True:
        line = input()
        if line.strip() == "":
            break
        
        # Сохраняем первую часть
        if len(first_lines) < 100:
            first_lines.append(line)
        
        # Управляем последними 100 строками
        if len(last_lines) < 100:
            last_lines.append(line)
        else:
            last_lines.pop(0)  # Удаляем первую строку, чтобы сохранить размер
            last_lines.append(line)

    # Объединяем списки
    combined_lines = first_lines + last_lines
    
    # Записываем результат в файл
    with open('output.txt', 'w') as f:
        for line in combined_lines:
            f.write(line + '\n')

    print("Результат записан в файл output.txt")

if __name__ == "__main__":
    main()
