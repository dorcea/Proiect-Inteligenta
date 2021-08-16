from flask import Flask

app = Flask(__name__)

@app.route('/')
def principala():
    return "Salut!"

@app.route('/about')
def despre():
    return "Despre pagina!"

if __name__=="__main__":
    app.run(debug=True)
