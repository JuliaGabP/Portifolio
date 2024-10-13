from flask import Flask, render_template, session, send_from_directory
from flask_session import Session

app = Flask(__name__)

# Configurar a sessão do Flask para armazenar dados no lado do servidor
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Rota para a página inicial
@app.route('/')
def index():
# Verificar se já existe um contador de visitas
    if 'visits' not in session:
        session['visits'] = 0
    # Incrementar o contador de visitas
    session['visits'] = session['visits'] + 1
    
    # Renderizar a página principal e passar o contador de visitas
    return render_template('index.html', visits=session['visits'])

# Rota para a página de trabalhos
@app.route('/works')
def works():
    return render_template('works.html')

# Rota para a página de cursos gratuitos
@app.route('/courses')
def courses():
    return render_template('courses.html')

# Rota para a página de inglês
@app.route('/english')
def english():
    return render_template('english.html')

# Rota para a página de certificações
@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

# Rota para abrir um arquivo PDF de trabalho
@app.route('/pdfs/<path:filename>')
def download_file(filename):
    return send_from_directory('pdfs', filename)

if __name__ == '__main__':
    app.run(debug=True)
