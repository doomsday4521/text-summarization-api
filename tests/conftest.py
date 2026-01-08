import sys
from pathlib import Path

import pytest
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))
from app.main import app
@pytest.fixture(autouse=True)
def reset_app_state():
    app.state.rate_limiter = None
    yield