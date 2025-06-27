# To-Do-Using-Flask
# 📝 Flask To-Do List App

This is a simple and beginner-friendly Flask-based To-Do List web application with user login/logout functionality. It allows you to add, update, and clear tasks with proper session handling and flash messaging.

---

## 🔧 Features

- ✅ User login with hardcoded credentials (`admin` / `1234`)
- ➕ Add new tasks
- 🔁 Toggle task status: **Pending → Working → Done → Pending**
- ❌ Clear all tasks
- 🔒 Session-based login/logout
- 🎨 Styled with custom CSS

---

## 📁 Project Structure

TODO_LIST/
│
├── app/
│ ├── init.py
│ ├── models.py
│ └── routes/
│ ├── auth.py
│ └── task.py
│
├── templates/
│ ├── base.html
│ ├── login.html
│ ├── register.html
│ └── tasks.html
│
├── static/
│ └── css/
│ └── style.css
│
├── run.py
├── Procfile
└── requirements.txt

yaml
Copy
Edit




---

## 🚀 Getting Started (Local Setup)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/todo-flask-app.git
cd TODO_LIST
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install flask flask_sqlalchemy gunicorn
pip install -r requirements.txt
python run.py
Made with ❤️ by Rudradeb Das
