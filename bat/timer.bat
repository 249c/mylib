@echo off
echo �^�C�}�[�@�\
echo �ݒ莞�ԁi�b�j�F10�b
echo.
pause
cls

for /l %%a in (10,-1,1) do (
    echo;
    echo ���� %%a �b
    timeout /t 1 > nul
    cls
)

echo ���Ԃł�
pause
