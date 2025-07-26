from flask import Flask, render_template, request
import csv

app = Flask(__name__)
THRESHOLD = 30
CSV_FILE = "inventory.csv"

def read_inventory():
    with open(CSV_FILE, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

@app.route("/")
def home():
    return render_template("home.html", THRESHOLD=THRESHOLD)

@app.route("/inventory")
def inventory():
    items = read_inventory()
    return render_template("inventory.html", title="Full Inventory", items=items, THRESHOLD=THRESHOLD)

@app.route("/below")
def below():
    items = [item for item in read_inventory() if int(item['Quantity']) < THRESHOLD]
    categories = sorted(set(item['ItemType'] for item in items))
    selected_category = request.args.get("category")
    if selected_category:
        items = [item for item in items if item['ItemType'] == selected_category]
    return render_template("inventory.html", title="Items Below Threshold",
                           items=items, categories=categories,
                           selected_category=selected_category, path="below", THRESHOLD=THRESHOLD)

@app.route("/above")
def above():
    items = [item for item in read_inventory() if int(item['Quantity']) >= THRESHOLD]
    categories = sorted(set(item['ItemType'] for item in items))
    selected_category = request.args.get("category")
    if selected_category:
        items = [item for item in items if item['ItemType'] == selected_category]
    return render_template("inventory.html", title="Items Above Threshold",
                           items=items, categories=categories,
                           selected_category=selected_category, path="above", THRESHOLD=THRESHOLD)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
