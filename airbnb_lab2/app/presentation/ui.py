from flask import Flask, render_template

from airbnb_lab2.app.presentation.controllers.user_controller import user_bp
from airbnb_lab2.app.presentation.controllers.housing_controller import housing_bp
from airbnb_lab2.app.presentation.controllers.booking_controller import booking_bp
from airbnb_lab2.app.presentation.controllers.payment_controller import payment_bp

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

app.register_blueprint(user_bp)
app.register_blueprint(housing_bp)
app.register_blueprint(booking_bp)
app.register_blueprint(payment_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)