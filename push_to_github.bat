@echo off
echo ======================================================================
echo Pushing ASR Benchmark Toolkit to GitHub: akhil-07-cyber
echo ======================================================================
set "PATH=%~dp0.tools\mingit\cmd;%PATH%"
git push -u origin main
echo ======================================================================
echo Push complete!
echo ======================================================================
pause
