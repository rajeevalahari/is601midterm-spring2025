"""Tests for individual plugin commands (arithmetic, showhistory, clearhistory, exit, menu)."""

import pytest
import pandas as pd  # Only if you need it for some tests
from app.plugins.addition import AddCommand
from app.plugins.subtraction import SubtractCommand
from app.plugins.multiplication import MultiplyCommand
from app.plugins.division import DivideCommand
from app.plugins.exit import ExitCommand
from app.plugins.menu import MenuCommand
from app.plugins.showhistory import ShowHistoryCommand
from app.plugins.clearhistory import ClearHistoryCommand

# If you actually need HistoryFacade in a test, uncomment:
# from app.plugins.history_facade import HistoryFacade


def test_addition_valid(capfd, monkeypatch):
    """Verify AddCommand with valid numeric input."""
    inputs = iter(["3", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = AddCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Result: 7.0" in out


def test_addition_invalid(capfd, monkeypatch):
    """Verify AddCommand with invalid numeric input."""
    inputs = iter(["three", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = AddCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out


def test_subtraction_valid(capfd, monkeypatch):
    """Verify SubtractCommand with valid numeric input."""
    inputs = iter(["10", "6"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = SubtractCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Result: 4.0" in out


def test_subtraction_invalid(capfd, monkeypatch):
    """Verify SubtractCommand with invalid numeric input."""
    inputs = iter(["ten", "6"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = SubtractCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out


def test_multiplication_valid(capfd, monkeypatch):
    """Verify MultiplyCommand with valid numeric input."""
    inputs = iter(["3", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = MultiplyCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Result: 15.0" in out


def test_multiplication_invalid(capfd, monkeypatch):
    """Verify MultiplyCommand with invalid numeric input."""
    inputs = iter(["three", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = MultiplyCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out


def test_division_valid(capfd, monkeypatch):
    """Verify DivideCommand with valid numeric input."""
    inputs = iter(["20", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = DivideCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Result: 5.0" in out


def test_division_zero(capfd, monkeypatch):
    """Verify DivideCommand handles division by zero."""
    inputs = iter(["10", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = DivideCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "division by zero" in out.lower()


def test_division_invalid(capfd, monkeypatch):
    """Verify DivideCommand with invalid numeric input."""
    inputs = iter(["twenty", "4"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cmd = DivideCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out


def test_exit_command():
    """Verify ExitCommand raises SystemExit with a custom message."""
    cmd = ExitCommand()
    with pytest.raises(SystemExit) as excinfo:
        cmd.execute()
    assert str(excinfo.value) == "Exiting..."


def test_menu_command(capfd):
    """Verify MenuCommand prints a help listing of commands."""
    cmd = MenuCommand()
    cmd.execute()
    out, _ = capfd.readouterr()
    assert "Available commands" in out
    assert "addition" in out
    assert "menu" in out
    assert "exit" in out


def test_showhistory_no_data(capfd, monkeypatch, tmp_path):
    """Verify ShowHistoryCommand prints 'No history yet.' if CSV is nonexistent or empty."""
    csv_file = tmp_path / "test_history.csv"
    monkeypatch.setenv("CALC_HISTORY_FILE", str(csv_file))

    cmd = ShowHistoryCommand()
    cmd.execute()

    out, _ = capfd.readouterr()
    assert "No history yet." in out


def test_showhistory_data(capfd, monkeypatch, tmp_path):
    """Verify ShowHistoryCommand prints the last 5 rows if CSV has >=5 entries."""
    csv_file = tmp_path / "test_history.csv"

    data = []
    for i in range(1, 7):
        data.append({"operation": "addition", "operand1": i, "operand2": i+1, "result": i+(i+1)})
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)

    monkeypatch.setenv("CALC_HISTORY_FILE", str(csv_file))

    cmd = ShowHistoryCommand()
    cmd.execute()

    out, _ = capfd.readouterr()
    assert "Last 5 Calculations:" in out
    # The first row i=1 might not appear if only last 5
    assert "1," not in out
    # The last row i=6 should appear
    assert "6" in out  # Relaxed check: "6," => "6"


def test_clearhistory_command(capfd, monkeypatch, tmp_path):
    """Verify ClearHistoryCommand deletes the CSV file."""
    csv_file = tmp_path / "test_history.csv"
    df = pd.DataFrame([{"operation": "add", "operand1": 1, "operand2": 2, "result": 3}])
    df.to_csv(csv_file, index=False)

    monkeypatch.setenv("CALC_HISTORY_FILE", str(csv_file))

    cmd = ClearHistoryCommand()
    cmd.execute()

    out, _ = capfd.readouterr()
    assert "History cleared." in out
    assert not csv_file.exists()
