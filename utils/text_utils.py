"""
Text utility functions for processing and manipulating text data.
"""


def split_text_by_newline(text: str, keep_empty: bool = False) -> list[str]:
    """
    Split text by newline characters.
    
    Args:
        text (str): The input text to split
        keep_empty (bool): If True, keep empty lines in the result. 
                          If False, filter out empty lines. Default is False.
    
    Returns:
        list[str]: A list of strings, each representing a line from the input text
    
    Examples:
        >>> split_text_by_newline("Hello\\nWorld")
        ['Hello', 'World']
        
        >>> split_text_by_newline("Hello\\n\\nWorld", keep_empty=True)
        ['Hello', '', 'World']
        
        >>> split_text_by_newline("Hello\\n\\nWorld", keep_empty=False)
        ['Hello', 'World']
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    
    lines = text.splitlines()
    
    if keep_empty:
        return lines
    
    return [line for line in lines if line.strip()]
