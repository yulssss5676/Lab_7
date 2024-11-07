# ��������� �������� � ������ ��� ��������
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

# ������� ��� ��������� ��� ������� ��������
def print_cars(cars):
    for car, details in cars.items():
        print(f"{car} - �������: {details['price']} USD, ³�: {details['age']} ����")

# ������� ��� ��������� ������ ������
def add_car(cars, model, price, age):
    cars[model] = {"price": price, "age": age}
    print(f"������ ��������� {model}.")

# ������� ��� ��������� ������
def delete_car(cars, model):
    try:
        del cars[model]
        print(f"�������� ��������� {model}.")
    except KeyError:
        print(f"�������: ��������� {model} �� ��������.")

# ������� ��� ���������� �������� �� �������
def print_sorted_cars(cars):
    sorted_cars = dict(sorted(cars.items()))
    print("³����������� ������ ���������:")
    print_cars(sorted_cars)

# ������� ��� ���������� �������� ������� ���� ������� �� 6 ����
def average_price_old_cars(cars):
    old_cars = [details['price'] for details in cars.values() if details['age'] > 6]
    if old_cars:
        average_price = sum(old_cars) / len(old_cars)
        print(f"������� ������� ���������, �� ���� �������� 6 ����: {average_price:.2f} USD")
    else:
        print("���� ���������, �� ���� �������� 6 ����.")

# �������� ���� ��� ������ � ������������
while True:
    print("\n����:")
    print("1 - ��������� ��� ������� ��������")
    print("2 - ��������� ������ ������")
    print("3 - ��������� ������")
    print("4 - ���������� �������� �� �������")
    print("5 - ���������� �������� ������� ���� ������� �� 6 ����")
    print("0 - ����� � ��������")

    choice = input("������ ����� ������ ����: ")

    if choice == "1":
        print_cars(cars)
    elif choice == "2":
        model = input("������ ������ ���������: ")
        price = float(input("������ ������� ���������: "))
        age = int(input("������ �� ���������: "))
        add_car(cars, model, price, age)
    elif choice == "3":
        model = input("������ ������ ��������� ��� ���������: ")
        delete_car(cars, model)
    elif choice == "4":
        print_sorted_cars(cars)
    elif choice == "5":
        average_price_old_cars(cars)
    elif choice == "0":
        print("����� � ��������...")
        break
    else:
        print("������� ����, ��������� �� ���.")
