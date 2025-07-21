
# 💬 ChatterPy - Flask-SocketIO Chat App

A real-time chat application built with **Flask** and **Socket.IO**, following the **MVC architecture** for clean separation of concerns.

---

## 🚀 Features

- Real-time communication
- Multiple chat rooms
- Guest username generator
- Private messaging
- Session-based user tracking
- Centralized logging

---

## 🧱 Project Structure

- **App Initialization** – Configures Flask, SocketIO, and logging
- **Configuration** – Stores app-wide constants and environment settings
- **Routes** – Handles HTTP requests (views/pages)
- **Socket Events** – Manages WebSocket actions like connect, message, join/leave
- **Utilities** – Helper functions (e.g. logging)
- **Templates** – Jinja2 HTML views
- **Static Files** – CSS, JS, assets
- **Log Directory** – Stores output logs
- **Entry Point** – Starts the app server

---

## 🛠️ Setup

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## ▶️ Running the App

```bash
python run.py
```

Then open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🌐 Environment Support (Optional)

Use environment variables or a `.env` file to customize:

* `SECRET_KEY`
* `FLASK_DEBUG`
* `CORS_ORIGINS`

---

## 📝 To-Do

* Add user authentication
* Store chat history in a database
* Admin control panel
* Emoji/media support

---

## 📄 License

MIT – Free to use, modify, and share.

```

