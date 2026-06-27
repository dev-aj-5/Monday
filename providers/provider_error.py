class ProviderError(Exception):
    """
    Base exception for all AI provider errors.
    """
    pass


class ProviderUnavailable(ProviderError):
    """
    Raised when an AI provider is temporarily unavailable.
    Examples:
    - Rate limit exceeded (429)
    - Server unavailable (503)
    - Timeout
    """
    pass


class InvalidAPIKey(ProviderError):
    """
    Raised when an API key is missing or invalid.
    """
    pass


class ProviderConfigurationError(ProviderError):
    """
    Raised when a provider is incorrectly configured.
    Example:
    - Missing model
    - Missing API key
    """
    pass