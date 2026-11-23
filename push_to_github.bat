@echo off
title GitHub Push Tool - ASR Benchmark Toolkit
echo ======================================================================
echo Pushing ASR Benchmark Toolkit to GitHub
echo Repository: akhil-07-cyber/ASR-Model-Benchmarking-Toolkit--CaseStudy
echo Author: Malli Akhil (USN: 23BTRCL209)
echo ======================================================================
echo.
set "PATH=%~dp0.tools\mingit\cmd;%PATH%"

echo GitHub requires a Personal Access Token (PAT) to upload files.
echo If you do not have one yet:
echo   1. Open: https://github.com/settings/tokens/new
echo   2. Under 'Note', type: ASR-Benchmarking
echo   3. Check the 'repo' box
echo   4. Scroll to bottom and click 'Generate token'
echo   5. Copy the generated token (starts with ghp_...)
echo.
set /p TOKEN="Paste your GitHub Token here and press Enter: "

if "%TOKEN%"=="" (
    echo.
    echo [ERROR] No token entered. Push cancelled.
    pause
    exit /b 1
)

echo.
echo Pushing files to GitHub main branch...
git push https://%TOKEN%@github.com/akhil-07-cyber/ASR-Model-Benchmarking-Toolkit--CaseStudy.git main -u

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo SUCCESS! All files and the 15-page PDF report have been pushed to:
    echo https://github.com/akhil-07-cyber/ASR-Model-Benchmarking-Toolkit--CaseStudy
    echo ======================================================================
) else (
    echo.
    echo [ERROR] Push failed. Please check that the token has 'repo' permissions and is copied correctly.
)
pause
