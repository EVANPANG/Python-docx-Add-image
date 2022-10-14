echo Thanks for use this program!

set /p Address= Image Address
@REM set /p Quantity = Quantity 
@REM set /p Count = Count

python Connect.py %Address% 
@REM %Quantity% %Count%
pause