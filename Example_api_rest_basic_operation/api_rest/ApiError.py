class APIError(Exception):
    """All custom API Exceptions"""
    def __init__(self, description, code):
        self.description = description
        self.code = code