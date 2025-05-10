import json
import os

EXPENSES_FILE = "expenses.json"
CATEGORIES = ["entertainment", "food", "technology", "other"]

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(data):
    with open(EXPENSES_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_category(new_category):
    if new_category not in CATEGORIES:
        CATEGORIES.append(new_category)
        print("Kateqoriya əlavə olundu.")
    else:
        print("Bu kateqoriya artıq mövcuddur.")

def add_expense(title, category, amount):
    if category not in CATEGORIES:
        print("Kateqoriya mövcud deyil.")
        return
    data = load_expenses()
    data.append({"title": title, "category": category, "amount": amount})
    save_expenses(data)
    print("Xərc əlavə olundu.")

def delete_expense(title):
    data = load_expenses()
    new_data = [e for e in data if e["title"] != title]
    save_expenses(new_data)
    print("Xərc silindi.")

def update_expense(title, new_amount):
    data = load_expenses()
    for e in data:
        if e["title"] == title:
            e["amount"] = new_amount
            break
    save_expenses(data)
    print("Xərc yeniləndi.")

def menu():
    while True:
        print("\n1. add_category\n2. add_expense\n3. delete_expense\n4. update_expense\n5. çıxış")
        choice = input("Seçim: ")
        
        if choice == "1":
            add_category(input("Yeni kateqoriya: "))
        elif choice == "2":
            add_expense(
                input("Başlıq: "),
                input("Kateqoriya: "),
                float(input("Məbləğ: "))
            )
        elif choice == "3":
            delete_expense(input("Silinəcək başlıq: "))
        elif choice == "4":
            update_expense(
                input("Yenilənəcək başlıq: "),
                float(input("Yeni məbləğ: "))
            )
        elif choice == "5":
            break
        else:
            print("Yanlış seçim.")

if __name__ == "__main__":
    menu()
