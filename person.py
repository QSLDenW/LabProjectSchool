class Person:
    def __init__(self, name: str):
        """
        Initialize a Person instance.

        :param name: Name of the person.
        """
        self.name = name

    def introduce(self) -> str:
        """
        Introduce the person.

        :return: A string introducing the person.
        """
        return f"Hello, I am {self.name}."