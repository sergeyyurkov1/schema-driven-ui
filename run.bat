@echo off
cls
call .\.venv\Scripts\activate
@REM call .\.venv\Scripts\python app.py
call .\.venv\Scripts\textual run app.py
pause
