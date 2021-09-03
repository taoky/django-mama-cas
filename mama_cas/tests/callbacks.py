from mama_cas.exceptions import InternalError


def raise_exception(ticket):
    """Raise an exception for testing purposes."""
    raise InternalError('Error in attribute callback')
