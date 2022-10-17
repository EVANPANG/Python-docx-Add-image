@echo Thanks for use this program!

@set /p Address= Image Address 
@set /p Sample= Sample 
@set /p Quantity= Quantity 

@python test.py %Address% %Sample% %Quantity%
pause