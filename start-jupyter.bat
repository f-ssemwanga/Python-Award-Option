@echo off
REM ---------------------------------------------------------------
REM  Python Award Option: start JupyterLab
REM
REM  Double-click this file. JupyterLab opens in your browser,
REM  showing the course folder. Click a Week folder to begin.
REM
REM  Leave the black window open while you work. Closing it stops
REM  JupyterLab and your cells will no longer run.
REM ---------------------------------------------------------------

cd /d "%~dp0"

echo Starting JupyterLab...
echo.
echo Leave this window open while you work.
echo Close it when you have finished for the lesson.
echo.

python -m jupyter lab

REM If JupyterLab failed to start, keep the window open so the
REM error message can be read rather than vanishing instantly.
if errorlevel 1 (
    echo.
    echo ---------------------------------------------------------------
    echo JupyterLab did not start. Show your teacher the message above.
    echo.
    echo The usual fix is to install it first, by running this in a
    echo Command Prompt:
    echo.
    echo     python -m pip install --user jupyterlab
    echo ---------------------------------------------------------------
    echo.
    pause
)
