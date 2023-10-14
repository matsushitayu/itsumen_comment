@echo off
setlocal enabledelayedexpansion

for /L %%i in (0, 8, 1000) do (
    echo Running script with index %%i
    python vocaloid_get_threadkeys.py %%i
)

endlocal
