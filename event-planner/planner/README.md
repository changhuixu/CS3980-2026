# Event Planner app

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install fastapi beanie uvicorn bcrypt pydantic[email] pydantic-settings pyjwt python-multipart httpx pytest coverage
# MacOS or Linux
pip freeze > requirements.txt
# Windows Powershell
# pip freeze | Out-File -Encoding UTF8 requirements.txt

# pip uninstall -r requirements.txt -y
```

```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

## My `.env` file

```bash
DATABASE_URL=mongodb://localhost:27017/my_database
SECRET_KEY=66568560338b14221aa1c8c78caf19a9064a74e8bf32ef35d86cc051617c622b
```
