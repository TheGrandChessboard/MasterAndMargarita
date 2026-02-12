"""Tests for the main module."""
import sys
from io import StringIO
from unittest.mock import patch

# Import the module to test
sys.path.insert(0, '/home/runner/work/MasterAndMargarita/MasterAndMargarita')
import main


def test_main_prints_book_name():
    """Test that main() prints the correct book name."""
    # Capture stdout
    captured_output = StringIO()
    with patch('sys.stdout', captured_output):
        main.main()
    
    output = captured_output.getvalue()
    assert "The Master and Margarita" in output


def test_main_function_exists():
    """Test that main function exists and is callable."""
    assert callable(main.main)
    assert hasattr(main, 'main')


def test_main_returns_none():
    """Test that main() returns None."""
    result = main.main()
    assert result is None
