@echo off

:STARTMENU
echo.
echo =================================
echo MTU�̒l�̊m�F�Ɛݒ�ύX�����܂��B
echo =================================
echo [1] PING�Ńp�P�b�g�̒f�Љ����K�v���m�F����
echo [2] ���݂�MTU�l���m�F����
echo [3] MTU�̒l��ύX����
echo.

set /p MODE="���[�h��I�����Ă��������F"

if %MODE% == 1 (
  goto PING
)else if %MODE% == 2 (
  goto SHOWMTU
)else if %MODE% == 3 (
  goto SETMTU
)
cls
goto STARTMENU

:PING
:: PING�R�}���h��MTU�ݒ�l���L�����ǂ����m�F
echo.
set /p PACKETSIZE="�p�P�b�g�T�C�Y���w�肵�Ă��������i��j1500�F"
echo.
echo on
ping -f -l %PACKETSIZE% www.yahoo.co.jp
@echo off
echo.
goto STARTMENU

:SHOWMTU
:: ���݂�MTU�ݒ�l���m�F����
echo.
echo on
netsh interface ipv4 show interface
@echo off
echo.
goto STARTMENU

:SETMTU
:: MTU�̒l��ύX
echo.
set /p IDX="Idx���w�肵�Ă��������F"
echo.
set /p MTUSIZE="MTU�T�C�Y���w�肵�Ă��������i��j1200�F"
echo.
echo on
netsh interface ipv4 set interface %IDX% mtu=%MTUSIZE%
@echo off
echo.
goto SHOWMTU

exit
