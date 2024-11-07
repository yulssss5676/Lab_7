# Створення словника з даними про автомобілі
cars = {
    "Toyota_Camry": {"price": 12000, "age": 7},
    "Honda_Civic": {"price": 9000, "age": 5},
    "Ford_Focus": {"price": 8000, "age": 8},
    "BMW_3Series": {"price": 15000, "age": 10},
    "Mercedes_CClass": {"price": 20000, "age": 6},
    "Nissan_Altima": {"price": 11000, "age": 7},
    "Mazda_6": {"price": 10000, "age": 4},
    "Volkswagen_Passat": {"price": 9500, "age": 9},
    "Chevrolet_Malibu": {"price": 8700, "age": 3},
    "Hyundai_Elantra": {"price": 9200, "age": 6}
}

# Функція для виведення всіх значень словника
def print_cars(cars):
    for car, details in cars.items():
        print(f"{car} - Вартість: {details['price']} USD, Вік: {details['age']} років")

# Функція для додавання нового запису
def add_car(cars, model, price, age):
    cars[model] = {"price": price, "age": age}
    print(f"Додано автомобіль {model}.")

# Функція для видалення запису
def delete_car(cars, model):
    try:
        del cars[model]
        print(f"Видалено автомобіль {model}.")
    except KeyError:
        print(f"Помилка: Автомобіль {model} не знайдено.")

# Функція для сортування словника за ключами
def print_sorted_cars(cars):
    sorted_cars = dict(sorted(cars.items()))
    print("Відсортований список автомобілів:")
    print_cars(sorted_cars)

# Функція для обчислення середньої вартості авто старших за 6 років
def average_price_old_cars(cars):
    old_cars = [details['price'] for details in cars.values() if details['age'] > 6]
    if old_cars:
        average_price = sum(old_cars) / len(old_cars)
        print(f"Середня вартість автомобілів, вік яких перевищує 6 років: {average_price:.2f} USD")
    else:
        print("Немає автомобілів, вік яких перевищує 6 років.")

# Головний цикл для діалогу з користувачем
while True:
    print("\nМеню:")
    print("1 - Виведення всіх значень словника")
    print("2 - Додавання нового запису")
    print("3 - Видалення запису")
    print("4 - Сортування словника за ключами")
    print("5 - Обчислення середньої вартості авто старших за 6 років")
    print("0 - Вихід з програми")

    choice = input("Введіть номер пункту меню: ")

    if choice == "1":
        print_cars(cars)
    elif choice == "2":
        model = input("Введіть модель автомобіля: ")
        price = float(input("Введіть вартість автомобіля: "))
        age = int(input("Введіть вік автомобіля: "))
        add_car(cars, model, price, age)
    elif choice == "3":
        model = input("Введіть модель автомобіля для видалення: ")
        delete_car(cars, model)
    elif choice == "4":
        print_sorted_cars(cars)
    elif choice == "5":
        average_price_old_cars(cars)
    elif choice == "0":
        print("Вихід з програми...")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")
