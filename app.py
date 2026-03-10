from flask import Flask, render_template, url_for, flash, request, redirect
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.testing.pickleable import User
from datetime import datetime

from database import db_session, Funcionario
from sqlalchemy import select, and_, func, Select
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'camila'

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Para visualizar esta pagina realize o login'
login_manager.login_message_category = "alert-danger"

@app.teardown_appcontext
def teardown_session(exception=None):
    db_session.remove()

@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    return db_session.execute(user).scalar_one_or_none()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


@app.route('/funcionarios')
@login_required
def funcionarios():
    funcio = select(Funcionario)
    funcio_exe = db_session.execute(funcio).scalars().all()
    print(funcio_exe)
    return render_template("funcionarios.html", funcio_exe=funcio_exe)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form.get('form-cpf')
        senha = request.form.get('form-senha')
        if cpf and senha:
            verificar_cpf = select(Funcionario).where(Funcionario.cpf == cpf)
            resultado_cpf = db_session.execute(verificar_cpf).scalar_one_or_none()
            if resultado_cpf:
                if resultado_cpf.check_password(senha):
                    #login correto
                    login_user(resultado_cpf)
                    flash('Login concluído', 'alert-success')
                    return redirect(url_for('home'))
                else:
                    # senha incorreta
                    flash('Senha incorreta', 'alert-danger')
                    return render_template('login.html')
        flash('insira seu CPF e sua senha', 'alert-danger')
        return render_template('login.html')

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso', 'alert-success')
    return redirect(url_for('login'))


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_funcionario():
    if request.method == 'POST':
        nome = request.form.get('form-nome')
        cpf = request.form.get('form-cpf')
        data_nascimento = request.form.get('form-data_nascimento')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        cargo = request.form.get('form-cargo')
        salario = request.form.get('form-salario')
        data_convertida = datetime.strptime(data_nascimento, '%Y-%m-%d')
        if not nome or not email or not senha or not cpf or not salario or not cargo or not data_nascimento:
            flash('Por favor, preencha todos os campos', 'alert-danger')
            return render_template('cadastro.html')
        verifica_email = select(Funcionario).where(Funcionario.email == email)
        existe_email = db_session.execute(verifica_email).scalar_one_or_none()
        if existe_email:
            flash(f'Email {email} ja cadastrado', 'alert-danger')
            return render_template('cadastro.html')

        try:
            novo_funcionario = Funcionario(nome=nome, email=email, cpf=cpf, data_nascimento=data_convertida, salario=float(salario), cargo=cargo)
            novo_funcionario.set_password(senha)
            db_session.add(novo_funcionario)
            db_session.commit()
            flash(f'Funcionario {nome} cadastrado', 'alert-success')
            return redirect(url_for('login'))
        except SQLAlchemyError as e:
            flash(f'Erro na base de dados ao cadastrar funcionario', 'alert-danger')
            print(f'Erro na base de dados: {e}')
            return redirect(url_for('cadastro_funcionario'))
        except Exception as e:
            flash(f'erro ao cadastrar funcionario', 'alert-danger')
            print(f'Erro ao cadastrar: {e}')
            return redirect(url_for('cadastro_funcionario'))
    return render_template('cadastro.html')


@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")

@app.route('/geometria')
def geometria():
    return render_template("geometria.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("soma realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)

        else:
            flash("preencha o campo", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtracao = n1 - n2
            flash("subtração realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)
        else:
            flash("preencha o campo", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicacao = n1 * n2
            flash("multiplicação realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicacao=multiplicacao)
        else:
            flash("preencha o campo", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            divisao = n1 / n2
            flash("divisão realizada", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, divisao=divisao)
        else:
            flash("preencha o campo", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/triangulo', methods=['GET', 'POST'])
def triangulo():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro = n1 + n1 + n1
            area = n1 * n1 / 2
            flash("cáculos com triângulo realizados ", 'alert-success')
            return render_template("geometria.html",n1=n1, perimetro=perimetro, area=area)
        else:
            flash("preencha o campo", 'alert-danger')

    return render_template("geometria.html")

@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro2 = 2 * 3.14 * n1
            area2 = 3.14 * n1 ** 2
            flash("cáculos com circulo realizados ", 'alert-success')
            return render_template("geometria.html",n1=n1, perimetro2=perimetro2, area2=area2)
        else:
            flash("preencha o campo", 'alert-danger')

    return render_template("geometria.html")

@app.route('/quadrado', methods=['GET', 'POST'])
def quadrado():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro3 = n1 * 4
            area3 = n1 * n1
            flash("cáculos com quadrado realizados ", 'alert-success')
            return render_template("geometria.html",n1=n1, perimetro3=perimetro3, area3=area3)
        else:
            flash("preencha o campo", 'alert-danger')

    return render_template("geometria.html")

@app.route('/hexagono', methods=['GET', 'POST'])
def hexagono():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro4 = n1 * 6
            area4 = n1 * n1 / 2 * 6
            flash("cáculos com hexagono realizados ", 'alert-success')
            return render_template("geometria.html", n1=n1, perimetro4=perimetro4, area4=area4)
        else:
            flash("preencha o campo", 'alert-danger')

    return render_template("geometria.html")

@app.route('/animais')
def animais():
    return render_template("animais.html")


#TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)