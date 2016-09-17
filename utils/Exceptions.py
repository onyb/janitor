class JanitorError(Exception):
    pass

class NetworkError(JanitorError):
    pass

class IncorrectResponseError(JanitorError):
    pass