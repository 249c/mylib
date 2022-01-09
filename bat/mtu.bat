@echo off

:STARTMENU
echo.
echo =================================
echo MTUの値の確認と設定変更をします。
echo =================================
echo [1] PINGでパケットの断片化が必要か確認する
echo [2] 現在のMTU値を確認する
echo [3] MTUの値を変更する
echo.

set /p MODE="モードを選択してください："

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
:: PINGコマンドでMTU設定値が有効かどうか確認
echo.
set /p PACKETSIZE="パケットサイズを指定してください（例）1500："
echo.
echo on
ping -f -l %PACKETSIZE% www.yahoo.co.jp
@echo off
echo.
goto STARTMENU

:SHOWMTU
:: 現在のMTU設定値を確認する
echo.
echo on
netsh interface ipv4 show interface
@echo off
echo.
goto STARTMENU

:SETMTU
:: MTUの値を変更
echo.
set /p IDX="Idxを指定してください："
echo.
set /p MTUSIZE="MTUサイズを指定してください（例）1200："
echo.
echo on
netsh interface ipv4 set interface %IDX% mtu=%MTUSIZE%
@echo off
echo.
goto SHOWMTU

exit
