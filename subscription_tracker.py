import json
import os
from datetime import datetime

DATA_FILE = "subscriptions.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_data(subscriptions):
    with open(DATA_FILE, "w") as file:
        json.dump(subscriptions, file, indent=4)

def add_subscription(subscriptions):
    name = input("Enter service name: ")
    cost = float(input("Enter monthly cost (₹): "))
    date = input("Enter next renewal date (YYYY-MM-DD): ")
    
    subscriptions.append({
        "name": name,
        "cost": cost,
        "renewal_date": date
    })
    print(f"Subscription to '{name}' added.")

def view_subscriptions(subscriptions):
    if not subscriptions:
        print("No subscriptions found.")
        return
    print("\nYour Subscriptions:")
    for i, sub in enumerate(subscriptions, start=1):
        print(f"{i}. {sub['name']} - ₹{sub['cost']} - Next Renewal: {sub['renewal_date']}")
    print()

def delete_subscription(subscriptions):
    view_subscriptions(subscriptions)
    if subscriptions:
        try:
            choice = int(input("Enter the number to delete: "))
            if 1 <= choice <= len(subscriptions):
                removed = subscriptions.pop(choice - 1)
                print(f"Deleted subscription to '{removed['name']}'.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

def show_total_cost(subscriptions):
    total = sum(sub["cost"] for sub in subscriptions)
    print(f"\nTotal Monthly Subscription Cost: ₹{total:.2f}\n")

def menu():
    subscriptions = load_data()
    
    while True:
        print("\n--- Subscription Tracker ---")
        print("1. Add Subscription")
        print("2. View Subscriptions")
        print("3. Delete Subscription")
        print("4. Show Total Monthly Cost")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_subscription(subscriptions)
        elif choice == "2":
            view_subscriptions(subscriptions)
        elif choice == "3":
            delete_subscription(subscriptions)
        elif choice == "4":
            show_total_cost(subscriptions)
        elif choice == "5":
            save_data(subscriptions)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
