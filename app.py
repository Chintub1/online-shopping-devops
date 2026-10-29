from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "change-this-for-your-own-deployment"

PRODUCTS = [
    {"id": 1, "name": "Everyday Backpack", "price": 39.99, "emoji": "🎒", "description": "A light backpack for work, class, and weekends.", "category": "Accessories"},
    {"id": 2, "name": "Steel Water Bottle", "price": 14.50, "emoji": "🧴", "description": "Reusable bottle to keep your drink close by.", "category": "Accessories"},
    {"id": 3, "name": "Wireless Headphones", "price": 59.00, "emoji": "🎧", "description": "Comfortable headphones for music and study.", "category": "Electronics"},
    {"id": 4, "name": "Desk Lamp", "price": 24.75, "emoji": "💡", "description": "A simple lamp for a brighter study desk.", "category": "Home"},
]


def cart_count():
    return sum(session.get("cart", {}).values())


@app.get("/")
def home():
    search_query = request.args.get("q", "").strip()
    selected_category = request.args.get("category", "").strip()
    categories = sorted({product["category"] for product in PRODUCTS})
    filtered_products = [
        product for product in PRODUCTS
        if search_query.casefold() in product["name"].casefold()
        and (not selected_category or product["category"] == selected_category)
    ]
    return render_template(
        "index.html",
        products=filtered_products,
        categories=categories,
        search_query=search_query,
        selected_category=selected_category,
        cart_count=cart_count(),
    )


@app.get("/cart")
def cart():
    quantities = session.get("cart", {})
    items = []
    total = 0
    for product in PRODUCTS:
        quantity = quantities.get(str(product["id"]), 0)
        if quantity:
            subtotal = product["price"] * quantity
            items.append({**product, "quantity": quantity, "subtotal": subtotal})
            total += subtotal
    return render_template("cart.html", items=items, total=total, cart_count=cart_count())


@app.post("/cart/add/<int:product_id>")
def add_to_cart(product_id):
    if any(product["id"] == product_id for product in PRODUCTS):
        quantities = session.get("cart", {})
        key = str(product_id)
        quantities[key] = quantities.get(key, 0) + 1
        session["cart"] = quantities
    return redirect(url_for("home"))


@app.post("/cart/remove/<int:product_id>")
def remove_from_cart(product_id):
    quantities = session.get("cart", {})
    quantities.pop(str(product_id), None)
    session["cart"] = quantities
    return redirect(url_for("cart"))


@app.post("/cart/clear")
def clear_cart():
    session["cart"] = {}
    return redirect(url_for("cart"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
