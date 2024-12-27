@echo off
cls
call git init
call git add *
call git commit -m "first commit"
call git branch -M main
call git remote add origin https://github.com/sergeyyurkov1/schema-driven-ui.git
call git push -u origin main
@REM 
pause