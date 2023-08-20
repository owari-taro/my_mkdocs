import requests


def hello_world(url: str):
    """
    this is a sample hello world
    :param str url: _description_
    """
    print("hello world")


class Person:
    """
    このゲームのユーザーを表す
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def play(self, message: str):
        """
        just print message

        :param str message: _description_
        """
        print(message)
