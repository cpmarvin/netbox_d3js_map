from flask import Flask,render_template
from mutils import get_netbox_connections
app = Flask(__name__)


@app.route('/')
def topology_netbox():
    df = get_netbox_connections()
    df['capacity'] = 1000
    df['util'] = 1000
    print(df)
    netbox_links = df.to_dict(orient='records')
    return render_template('topology_netbox.html', values=netbox_links)

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = '8801',
        threaded = True
        )
