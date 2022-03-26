class Error(Exception):
    """All custom Arithmetic Exceptions"""
    def __init__(self, description, code):
        self.description = description
        self.code = code
