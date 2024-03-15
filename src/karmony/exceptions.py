class NonRepeatableError(Exception):
    def __init__(self, message="Non-repeatable request error"):
        super().__init__(message)


class RepeatableError(Exception):
    def __init__(self, message="Repeatable request error"):
        super().__init__(message)


class ContractAddressNotFoundError(NonRepeatableError):
    def __init__(self, message="Contract address not found error"):
        super().__init__(message)
