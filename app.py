from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config.from_object('config.Config')

# Example credentials (username and hashed password)
USER_CREDENTIALS = {
    "admin": generate_password_hash("password123")  # Change this!
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USER_CREDENTIALS and check_password_hash(USER_CREDENTIALS[username], password):
            session['user'] = username
            return redirect(url_for('landing'))
        flash("Invalid username or password.")
    return render_template('login.html')

@app.route('/landing')
def landing():
    if 'user' not in session:
        return redirect(url_for('login'))
    # Add your subdomain links here
    services = {
        "Jellyfin": "http://jellyfin.haackcluster.nl",
        "qBittorrent": "http://torrent.haackcluster.nl",
        "Sonarr": "http://sonarr.haackcluster.nl",
        "Radarr": "http://radarr.haackcluster.nl",
        "Prowlarr": "http://prowlarr.haackcluster.nl"
    }
    return render_template('landing.html', services=services)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
