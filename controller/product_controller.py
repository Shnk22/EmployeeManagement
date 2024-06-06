from app import app
@app.route('/product/add')
def product():
    return "Add your products"