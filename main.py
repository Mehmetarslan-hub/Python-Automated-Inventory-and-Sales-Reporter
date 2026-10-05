import random
import os

DATA_FILE = "depo.txt"
REPORT_FILE = "gunluk_rapor.txt"

def initialize_demo_inventory():
    """Generates initial dummy inventory data if file does not exist."""
    content = """Laptop - 15 - 25000
Kulaklik - 50 - 1500
Klavye - 30 - 2000
Fare - 8 - 800
Monitor - 20 - 7000"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        f.write(content)

def load_inventory(filepath):
    """Parses inventory data from text file into a dictionary."""
    inventory = {}
    if not os.path.exists(filepath):
        initialize_demo_inventory()

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                parts = line.strip().split("-")
                item_name = parts[0].strip()
                quantity = int(parts[1].strip())
                price = int(parts[2].strip())
                inventory[item_name] = {"quantity": quantity, "price": price}
    except Exception as e:
        print(f"[ERROR] Failed to load inventory: {e}")
        return None

    return inventory

def process_sales_and_generate_report(inventory):
    """Simulates daily sales, updates stock, and outputs structured report."""
    total_revenue = 0
    top_earner_product = ""
    max_product_revenue = 0

    print("\n" + "=" * 50)
    print("      DAILY INVENTORY & SALES SIMULATION")
    print("=" * 50)

    with open(REPORT_FILE, "w", encoding="utf-8") as report:
        report.write("==================================================\n")
        report.write("            DAILY SALES REPORT\n")
        report.write("==================================================\n")

        for product, details in inventory.items():
            demand = random.randint(1, 10)
            current_stock = details["quantity"]

            sold = demand if demand <= current_stock else current_stock
            if sold == current_stock:
                print(f"[ALERT] Stock depleted for: {product}")

            details["quantity"] -= sold
            revenue = sold * details["price"]
            total_revenue += revenue

            if revenue > max_product_revenue:
                max_product_revenue = revenue
                top_earner_product = product

            log = f"{product:<12} | Sold: {sold:<2} | Remaining: {details['quantity']:<2} | Revenue: {revenue:>8} TL\n"
            report.write(log)
            print(log.strip())

        report.write("-" * 50 + "\n")
        report.write(f"Total Store Revenue : {total_revenue} TL\n")
        report.write(f"Top Performing Item : {top_earner_product} ({max_product_revenue} TL)\n")
        report.write("==================================================\n")

    print("\n[SUCCESS] Sales simulation completed. Report generated -> 'gunluk_rapor.txt'")

def main():
    inventory = load_inventory(DATA_FILE)
    if inventory:
        process_sales_and_generate_report(inventory)

if __name__ == "__main__":
    main()