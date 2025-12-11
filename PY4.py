from itertools import combinations


items = [
    ('r', 3, 25),  
    ('p', 2, 15),  
    ('a', 2, 15),  
    ('m', 2, 20),  
    ('i', 1, 5),   
    ('k', 1, 15),  
    ('x', 3, 20), 
    ('t', 1, 25),  
    ('f', 1, 15),  
    ('d', 1, 10),  
    ('s', 2, 20), 
    ('c', 2, 20)   
]


BACKPACK_SIZE= 9  
DISEASE = 'паранойя'
START_POINTS= 15


TOTAL_VALUE_ALL = sum(item[2] for item in items)

def calculate_score(taken_items):
    """Вычисляет итоговый счёт"""
    taken_value = sum(item[2] for item in taken_items)
    return START_POINTS + 2 * taken_value - TOTAL_VALUE_ALL

def find_valid_combinations():
    """Находит все валидные комбинации предметов"""
    valid_combinations = []
    
    
    for r in range(1, len(items) + 1):
        for combo in combinations(items, r):
            
            if DISEASE == 'паранойя' and not any(item[0] == 'd' for item in combo):
                continue
                
        
            total_size = sum(item[1] for item in combo)
            if total_size <= BACKPACK_SIZE:
                score = calculate_score(combo)
                if score > 0:
                    valid_combinations.append((combo, score, total_size))
    
    return valid_combinations

def display_backpack_layout(combo):
    """Отображает layout рюкзака в виде 3x3 сетки"""
    backpack = [['[ ]' for _ in range(3)] for _ in range(3)]
    
    row, col = 0, 0
    for item in combo:
        size = item[1]
        symbol = f'[{item[0]}]'
        
        for _ in range(size):
            if col >= 3:
                col = 0
                row += 1
            if row >= 3:
                break
            backpack[row][col] = symbol
            col += 1
    
    print("Расположение в рюкзаке:")
    for row in backpack:
        print(' '.join(row))

def main():
    print(f"=== Решение для Варианта 6 ===")
    print(f"Размер рюкзака: 3x3 ({BACKPACK_SIZE} ячеек)")
    print(f"Болезнь: {DISEASE}")
    print(f"Стартовые очки выживания: {START_POINTS}")
    print(f"Обязательный предмет: антидот (d)\n")
    
    solutions = find_valid_combinations()
    
    if not solutions:
        print("Действительных решений не найдено!")
        return
    

    solutions.sort(key=lambda x: x[1], reverse=True)
    
    print(f"Найдено {len(solutions)} действительных решений\n")
    
    
    for i, (combo, score, used_size) in enumerate(solutions[:5], 1):
        print(f"--- Решение {i} ---")
        print(f"Предметы: {[item[0] for item in combo]}")
        print(f"Занято места: {used_size}/{BACKPACK_SIZE}")
        print(f"Очки предметов: {sum(item[2] for item in combo)}")
        print(f"Итоговые очки выживания: {score}")
        
        display_backpack_layout(combo)
        print()


def verify_specific_solution():
    print("=== Проверка конкретного решения ===")
    
    
    solution_items = ['t', 'k', 'f', 'm', 'c', 's', 'd']
    taken = [item for item in items if item[0] in solution_items]
    
    total_size = sum(item[1] for item in taken)
    total_value = sum(item[2] for item in taken)
    score = calculate_score(taken)
    
    print(f"Предметы: {solution_items}")
    print(f"Общий размер: {total_size}")
    print(f"Общая ценность: {total_value}")
    print(f"Итоговый счёт: {score}")
    
    display_backpack_layout(taken)

if __name__ == "__main__":
    main()
    print("\n" + "="*50)
    verify_specific_solution()
    