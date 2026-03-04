🔗 Mini URL Shortener

A simple and functional URL Shortening web application built using Flask and SQLite.
This application allows users to convert long URLs into short, shareable links and tracks click counts.

🚀 Features

Generate short URLs from long links

Automatic redirection to original URL

Click tracking functionality

Database-backed link storage

Clean and responsive UI

Lightweight and easy to run locally

🛠 Tech Stack

Backend: Python (Flask)

Database: SQLite

Frontend: HTML5, CSS3

Version Control: Git & GitHub

📂 Project Structure

mini_url_shortener/

app.py

templates/

index.html

static/

style.css

urls.db (auto-generated)

⚙️ How It Works

User submits a long URL.

Application generates a random 6-character short code.

The original URL and short code are stored in the database.

When the short link is accessed:

The app retrieves the original URL

Increments the click counter

Redirects the user

▶️ Installation & Setup
1️⃣ Clone the repository

git clone https://github.com/sonam212/MiniUrlShortener.git

cd MiniUrlShortener

2️⃣ Install dependencies

pip install flask

3️⃣ Run the application

python app.py

4️⃣ Open in browser

http://127.0.0.1:5000

📈 Future Improvements

Custom short codes

URL validation improvements

Analytics dashboard

QR code generation

Deployment to cloud (Render / Railway)

👩‍💻 Author

Sonam Sharma
GitHub: https://github.com/sonam212

LinkedIn: https://www.linkedin.com/in/sonam-sharma-3b1636304
