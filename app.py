from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({"message": "Opção de pagamento criado."})

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({"message": "Pagamento confirmado."})

@app.route('/payments/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return 'Pagamento em pix.'

if __name__ == '__main__':
    app.run(debug=True)