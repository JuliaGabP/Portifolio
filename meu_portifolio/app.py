from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

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

# Rota para abrir um arquivo PDF de trabalho
@app.route('/pdfs/<path:filename>')
def download_file(filename):
    return send_from_directory('pdfs', filename)

if __name__ == '__main__':
    app.run(debug=True)
