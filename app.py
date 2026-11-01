from flask import Flask, render_template

# static_folder='.' allows Flask to serve images directly from your root folder
app = Flask(__name__, static_folder='.')

@app.route('/')
def home():
    # Mapped using your exact uploaded image filenames
    products = [
        {"name": "Cold-Pressed Coconut Oil", "price": "₹280 / Litre", "image": "4Q7A9748.JPG", "desc": "Pure chekku extracted, rich aroma."},
        {"name": "Cold-Pressed Groundnut Oil", "price": "₹260 / Litre", "image": "4Q7A9752.JPG", "desc": "Traditional wooden churned."},
        {"name": "Cold-Pressed Gingelly Oil", "price": "₹340 / Litre", "image": "1773509019588.png", "desc": "Sesame oil for health and traditional cooking."},
        {"name": "Pure Nattu Sakkarai (Jaggery)", "price": "₹90 / Kg", "image": "1773509713924.png", "desc": "Chemical-free unrefined cane sugar."},
        {"name": "Deepam Lamp Oil", "price": "₹150 / Litre", "image": "4Q7A9748.JPG", "desc": "Custom blend for bright, clean burning."}
    ]
    
    address = "1/114, 1/115, Chinnamanaikenpalyam, J.krishnapuram, Sulur, Coimbatore 641671"
    whatsapp_number = "919095553344"
    
    return render_template('index.html', products=products, address=address, whatsapp_number=whatsapp_number)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
    
