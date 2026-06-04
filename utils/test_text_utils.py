"""
Unit tests for text_utils module.
"""

import pytest
from text_utils import split_text_by_newline


class TestSplitTextByNewline:
    """Test cases for split_text_by_newline function."""
    
    def test_basic_split(self):
        """Test basic newline splitting."""
        text = "Hello\nWorld"
        result = split_text_by_newline(text)
        assert result == ["Hello", "World"]
    
    def test_multiple_lines(self):
        """Test splitting multiple lines."""
        text = "Line 1\nLine 2\nLine 3\nLine 4"
        result = split_text_by_newline(text)
        assert result == ["Line 1", "Line 2", "Line 3", "Line 4"]
    
    def test_empty_lines_filtered(self):
        """Test that empty lines are filtered by default."""
        text = "Hello\n\nWorld\n\n"
        result = split_text_by_newline(text)
        assert result == ["Hello", "World"]
    
    def test_empty_lines_kept(self):
        """Test keeping empty lines when keep_empty=True."""
        text = "Hello\n\nWorld"
        result = split_text_by_newline(text, keep_empty=True)
        assert result == ["Hello", "", "World"]
    
    def test_whitespace_only_lines_filtered(self):
        """Test that lines with only whitespace are filtered."""
        text = "Hello\n   \nWorld\n\t\n"
        result = split_text_by_newline(text)
        assert result == ["Hello", "World"]
    
    def test_whitespace_only_lines_kept(self):
        """Test that lines with only whitespace are kept when keep_empty=True."""
        text = "Hello\n   \nWorld"
        result = split_text_by_newline(text, keep_empty=True)
        assert result == ["Hello", "   ", "World"]
    
    def test_empty_string(self):
        """Test with empty string input."""
        text = ""
        result = split_text_by_newline(text)
        assert result == []
    
    def test_single_line(self):
        """Test with single line (no newlines)."""
        text = "Hello World"
        result = split_text_by_newline(text)
        assert result == ["Hello World"]
    
    def test_windows_line_endings(self):
        """Test with Windows-style line endings (CRLF)."""
        text = "Hello\r\nWorld\r\nPython"
        result = split_text_by_newline(text)
        assert result == ["Hello", "World", "Python"]
    
    def test_mixed_line_endings(self):
        """Test with mixed line ending styles."""
        text = "Hello\nWorld\r\nPython\rTest"
        result = split_text_by_newline(text)
        assert result == ["Hello", "World", "Python", "Test"]
    
    def test_trailing_newline(self):
        """Test with trailing newline."""
        text = "Hello\nWorld\n"
        result = split_text_by_newline(text)
        assert result == ["Hello", "World"]
    
    def test_leading_newline(self):
        """Test with leading newline."""
        text = "\nHello\nWorld"
        result = split_text_by_newline(text)
        assert result == ["Hello", "World"]
    
    def test_type_error(self):
        """Test that TypeError is raised for non-string input."""
        with pytest.raises(TypeError):
            split_text_by_newline(123)
        
        with pytest.raises(TypeError):
            split_text_by_newline(None)
        
        with pytest.raises(TypeError):
            split_text_by_newline(["Hello", "World"])
    
    def test_unicode_content(self):
        """Test with unicode characters."""
        text = "Hello 世界\nBonjour 🌍\nПривет"
        result = split_text_by_newline(text)
        assert result == ["Hello 世界", "Bonjour 🌍", "Привет"]
    
    def test_special_characters(self):
        """Test with special characters."""
        text = "Hello@World!\n#Python$\n%Test&"
        result = split_text_by_newline(text)
        assert result == ["Hello@World!", "#Python$", "%Test&"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
