#!/usr/bin/python3
"""A class User that inherits from BaseModel."""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class represent user data and inherit from BaseModel.

    Public class attribute:
        email: str - empty.
        password: str - empty.
        first_name: str - empty.
        last_name: str - empty.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the User class.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword argument.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
