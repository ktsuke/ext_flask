from flask import Flask, render_template
app = Flask("projeto")

@app.route("/")
def root():
    nome="João Victor"
    produtos=[{"nome":"Ração", "preço":19,99}
    {"nome":"play", "preço":3000,00}]

    return render_template ("alo.html", n=nome, aProdutos=produtos),200

@app.route("/teste")
def teste():
    return "Nova rota teste", 200

app.run()

