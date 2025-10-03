# Start both frontend and backend servers in separate terminal windows

Write-Host "Starting Agent Debate Arena..." -ForegroundColor Green

# Get the current directory
$ProjectDir = Get-Location

# Start backend in new terminal
Write-Host "Opening backend terminal..." -ForegroundColor Yellow
Start-Process cmd -ArgumentList "/k", "cd /d `"$ProjectDir\backend`" && venv\Scripts\python.exe -m pip install fastapi uvicorn python-dotenv && venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000"

# Start frontend in new terminal  
Write-Host "Opening frontend terminal..." -ForegroundColor Yellow
Start-Process cmd -ArgumentList "/k", "cd /d `"$ProjectDir\frontend`" && npm start"

Write-Host "Terminal windows opened!" -ForegroundColor Green
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "Backend: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Backend API docs: http://localhost:8000/docs" -ForegroundColor Cyan