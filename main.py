from flask import Flask, render_template

menu = {
    "Inicio": {},
    "Oferta Educativa": {
        "Licenciaturas e Ingenierías": {
            "Ing. Sistemas Computacionales": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ing. Electrónica": {
                "Plan de Estudios": {},
                "Programa": {}
            }
        },
        "Posgrado": {}
    },
    "Contacto": {}
}

app = Flask(__name__)

@app.route("/")
def mostrar_menu_flask():
    return render_template("menu.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)