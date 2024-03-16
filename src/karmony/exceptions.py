class NonRepeatableError(Exception):
    def __init__(self, message="Non-repeatable request error"):
        super().__init__(message)


class RepeatableError(Exception):
    def __init__(self, message="Repeatable request error"):
        super().__init__(message)


class ContractAddressNotFoundError(NonRepeatableError):
    def __init__(self, message="Contract address not found error"):
        super().__init__(message)


class MaxAddittionalNonceCounterReachedError(NonRepeatableError):
    def __init__(self, message="The limit of the maximum additional nonce counter has been reached"):
        super().__init__(message)
