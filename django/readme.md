# Django

### Using a Virtual Environment
1. **Create a virtual environment:**
    ```bash
    python3 -m venv <path/to/venv>
    ```

2. **Activate the virtual environment:**
    - **For macOS/Linux:**
        ```bash
        source <path/to/venv/>bin/activate
        ```
    - **For Windows:**
        ```bash
        path\to\venv\Scripts\activate
        ```

3. **Install Django within the virtual environment:**
    ```bash
    python3 -m pip install django
    ```

### Using `pipx` for Isolated Python Application Installations
1. **Install `pipx` using Homebrew:**
    ```bash
    brew install pipx
    ```

2. **Install Django using `pipx`:**
    ```bash
    pipx install django
    ```

### Override the Error (Not Recommended)
If you want to bypass the restriction (not recommended as it can break your Python installation or OS), you can use the `--break-system-packages` flag:
```bash
python3 -m pip install django --break-system-packages
```

Or, modify your `pip.conf` file:
1. **Open or create the `pip.conf` file:**
    ```bash
    nano ~/.config/pip/pip.conf
    ```

2. **Add the following line to the file:**
    ```ini
    [global]
    break-system-packages = true
    ```

After setting this, you can install Django using `pip` as usual:
```bash
python3 -m pip install django
```


# Writing dependencies
 To write dependencies we use following command
```bash
pip freeze > requirements.txt
```

we write dependencies as follows 
```text
django==3.0.3
```

# Version

```bash
pip show <package>
```


# Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```