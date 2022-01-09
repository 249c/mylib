@echo off
echo タイマー機能
echo 設定時間（秒）：10秒
echo.
pause
cls

for /l %%a in (10,-1,1) do (
    echo;
    echo あと %%a 秒
    timeout /t 1 > nul
    cls
)

echo 時間です
pause
