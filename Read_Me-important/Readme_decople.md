
# 📚 Notes: Secure Django Secret Data Using `python-decouple`

## ✅ What is `python-decouple`?

* A Python library to **separate config settings** (like `SECRET_KEY`, DB credentials, API keys) from the source code.
* Reads environment variables from a `.env` file.
* Helps keep secret data **secure, flexible, and manageable**.

---

## 🧠 Why Use It?

| Benefits                   | Description                                   |
| -------------------------- | --------------------------------------------- |
| 🔐 Security                | Keeps secrets out of version control (`.git`) |
| 🌍 Environment Flexibility | Different configs for dev, prod, staging      |
| 🧼 Cleaner Code            | No hardcoded secrets in `settings.py`         |

---

## 🛠 How to Install?

```bash
pip install python-decouple
```

---

## 📝 Step-by-Step Setup

### 1. Create `.env` file in your project root:

```env
SECRET_KEY=django-insecure-abc123
DEBUG=True
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypass
```

> ⚠️ Add `.env` to `.gitignore`

---

### 2. Modify `settings.py` to use `decouple`

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

### 3. Optional: Cast data types

```python
DEBUG = config('DEBUG', default=False, cast=bool)
PORT = config('PORT', default=5432, cast=int)
```

---

## 🔐 Security Best Practices

* ✅ Add `.env` to `.gitignore`
* ✅ Never hardcode passwords or keys in `settings.py`
* ✅ Use `.env.example` to show structure of variables

---

## 📁 Folder Structure

```
your_project/
├── .env               # secret keys
├── .gitignore         # must include `.env`
├── manage.py
└── your_project/
    └── settings.py    # uses config() from decouple
```

---

## ✅ Summary Table

| Key Concept     | Description                               |
| --------------- | ----------------------------------------- |
| `config()`      | Fetch values from `.env`                  |
| `cast=bool/int` | Convert to desired Python type            |
| `.env`          | Store sensitive/environment-specific data |
| `.gitignore`    | Always exclude `.env`                     |
