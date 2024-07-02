import pytest
import sys
from datetime import datetime
from seasons import main

def test_invalid_input_exit_code(monkeypatch, capsys):
    # Mock user input to simulate an invalid input
    monkeypatch.setattr('builtins.input', lambda _: 'February 6th, 1998')

    with pytest.raises(SystemExit) as exc_info:
        main()

    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Error: " in captured.err
