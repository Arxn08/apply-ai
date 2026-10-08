#!/usr/bin/env python3
"""
Apply.ai (Job Autofill Copilot) Runner Script
Usage:
    python3 run.py
"""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
VENV_PYTHON = ROOT / ".venv" / "bin" / "python"

# If not already running inside .venv, switch to the virtual environment python
if VENV_PYTHON.exists() and sys.executable != str(VENV_PYTHON):
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), __file__] + sys.argv[1:])

if __name__ == "__main__":
    import uvicorn
    print("\n🚀 Starting Apply.ai backend server on http://localhost:8000 ...")
    print("📖 Interactive Swagger API Docs: http://localhost:8000/docs\n")
    uvicorn.run("backend.api.main:app", host="0.0.0.0", port=8000, reload=True)
