@echo off
cls
call git add *
call git commit -m "commit"
call git push -u origin main
pause