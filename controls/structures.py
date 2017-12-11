class SuccessfulReturnTypeBase(object):
    def __init__(self):
        self.success = True


class FailureReturnTypeBase(object):
    def __init__(self, message=None):
        self.success = False
        self.message = message
