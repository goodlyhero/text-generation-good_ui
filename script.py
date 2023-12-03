"""
Simple extension that changes some styles to make interface more friendly... especially for mobile users.
"""

from pathlib import Path

def custom_js():
    path_to_js = Path(__file__).parent.resolve() / 'script.js'
    return open(path_to_js, 'r').read()

def setup():
    """
    Gets executed only once, when the extension is imported.
    """
    pass

