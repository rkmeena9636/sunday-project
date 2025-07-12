from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Welcome Page</h1>
    <p>This is the main home page.</p>
    <p>Try visiting <a href="/header">/header</a>, <a href="/body">/body</a>, <a href="/footer">/footer</a></p>
    '''

@app.route('/header')
def header():
    return '''
    <header>
        <h2>This is the HEADER</h2>
        <p>Usually contains the logo and nav bar.</p>
    </header>
    '''

@app.route('/body')
def body():
    return '''
    <main>
        <h2>This is the BODY section</h2>
        <p>It has the main content of the website.</p>
    </main>
    '''

@app.route('/footer')
def footer():
    return '''
    <footer>
        <p>Footer © 2025 - All rights reserved.</p>
    </footer>
    '''

if __name__ == '__main__':
    app.run(debug=True)
