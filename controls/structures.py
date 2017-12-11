class SuccessfulReturnTypeBase(object):
    """
    A structure for unifying successful return types from a variety of functions.
    The class has a success variable that will be True.  Derived types can then build on this.
    """

    def __init__(self):
        self.success = True

    def to_dict(self):
        """Utility function to convert this structure into a dictionary"""
        return {'success': self.success}


class FailureReturnTypeBase(object):
    """
    A structure for unifying failure return types from a variety of functions.
    The class has a success variable that will be False, and a message variable. Derived types can then build on this.
    """

    def __init__(self, message=None):
        """
        Construct a failure-based return type, which will set the success variable to False, and also store a message.

        :param message: A message to be stored on the class to provide context to the error.
        """
        self.success = False
        self.message = message

    def to_dict(self):
        """Utility function to convert this structure into a dictionary"""
        return {'success': self.success, 'message': self.message}
