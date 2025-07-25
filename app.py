from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"  # para mensagens flash

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Exemplo simples de validação
        if username == "admin" and password == "1234":
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("login"))
        else:
            flash("Usuário ou senha inválidos.", "danger")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)