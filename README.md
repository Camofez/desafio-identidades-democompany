# Python environment setup

Follow these steps on Windows PowerShell to create and use a virtual environment for this project.

1. Create a virtual environment in the project root (creates `.venv`):

```
python -m venv .venv
```

2. Activate the virtual environment (PowerShell):

```
.\.venv\Scripts\Activate.ps1
```

If you get a policy error when activating, run this one-liner to allow activation for the current session (does not change machine policy):

```
powershell -ExecutionPolicy Bypass -NoProfile -Command "& { .\.venv\Scripts\Activate.ps1 }"
```

3. Upgrade pip and install dependencies:

```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Or run the included bootstrap script from PowerShell to automate steps 1–3:

```
.\scripts\bootstrap.ps1
```
