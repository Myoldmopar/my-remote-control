class SuccessfulReturnTypeBase(object):

    def __init__(self):
        self.success = True

    def to_dict(self):
        return {'success': self.success}


class FailureReturnTypeBase(object):

    def __init__(self, message=None):
        self.success = False
        self.message = message

    def to_dict(self):
        return {'success': self.success, 'message': self.message}
