from app import app, render_template, pd, np, plt



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/titanic')
def csvViewer():
        path = './app/static/data/titanic.csv'
        df   = pd.read_csv(path)
        records = df.head()

        return render_template('show.html', records=records)
