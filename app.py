from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dasbor():
    return render_template('index.html', title='Dasbor')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html', title='Tentang')

@app.route('/foto')
def galeri():
    return render_template('foto.html', title='Foto')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html', title='Kontak')

if __name__ == '__main__':
    app.run(debug=True)