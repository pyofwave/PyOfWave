"""
Testing script to ensure I can initialize Delta and Operation objects.
"""

from .. import delta

delta.Operation("test", "spam", "eggs")

delta.Delta(delta.Operation("test", "spam", "eggs", 42))
