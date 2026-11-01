from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Mapped to your exact uploaded filenames in the static folder
    products = [
        {"name": "Cold-Pressed Coconut Oil", "price": "₹280 / Litre", "image": "coconut oil pouches.jpg", "desc": "Pure chekku extracted, rich aroma."},
        {"name": "Cold-Pressed Groundnut Oil", "price": "₹260 / Litre", "image": "groundnut oil 1liter.png", "desc": "Traditional wooden churned."},
        {"name": "Cold-Pressed Gingelly Oil", "price": "₹340 / Litre", "image": "gingelly oils.jpg", "desc": "Sesame oil for health and traditional cooking."},
        {"name": "Pure Nattu Sakkarai (Jaggery)", "price": "₹90 / Kg", "image": "castor oils.jpg", "desc": "Chemical-free unrefined cane sugar."},
        {"name": "Deepam Lamp Oil", "price": "₹150 / Litre", "image": "sunflower oil pouches.jpg", "desc": "Custom blend for bright, clean burning."}
    ]
    
    address = "1/114, 1/115, Chinnamanaikenpalyam, J.krishnapuram, Sulur, Coimbatore 641671"
    whatsapp_number = "919095553344"
    
    return render_template('index.html', products=products, address=address, whatsapp_number=whatsapp_number)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
    
