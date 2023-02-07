from flask import Flask, request
from flask_session import Session

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

Session(app)

visit_count = 0

@app.route('/')
def index():
    global visit_count
    visit_count += 1
    client_ip = request.remote_addr
    return f"Your IP address is {client_ip}. Number of visits in this session: {visit_count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
