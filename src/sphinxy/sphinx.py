from sphinxy.riddle import Riddle


class IncorrectAnswer(Exception):
    """Use this exception to indicate an incorrect answer."""

    ...


class Sphinx:
    def __init__(self, name: str):
        self._name = name
        self._riddle = Riddle(
            question=(
                "What goes on four legs in the morning, two legs at noon, "
                "and three legs in the evening?"
            ),
            answer="man",
        )

    def introduce(self) -> str:
        """The Sphinx introduces itself

        Returns:
            str: A string introduction
        """
        return (
            f"Greetings, mortals. I am {self._name}. I have guarded the city of Thebes"
            "for centuries and posed riddles to those who dared to approach me."
        )

    def update_riddle(self, riddle: Riddle) -> str:
        """Updates stored riddle

        Args:
            riddle (Riddle): The new riddle to store

        Returns:
            str: A confirmation that the riddle has been updated
        """
        self._riddle = riddle
        return "I have updated my riddle. Are you ready to solve it?"

    def pose_riddle(self, include_hint: bool = False) -> tuple[str, str]:
        """Poses the stored riddle and a hint, if requested.

        Args:
            include_hint (bool, optional): Set to True to ask for hint. Defaults to False.

        Returns:
            tuple[str, str]: The riddle and a hint or an empty string if no hint requested
        """
        hint = ""
        if include_hint:
            hint = (
                f"Hint: The answer starts with the letter '{self._riddle.get_hint()}'."
            )
        return (self._riddle.question, hint)

    def check_riddle_answer(self, answer: str, return_hint: bool = False) -> str:
        """Evaluates the answer given for he riddle.

        Args:
            answer (str): The given answer to the riddle.
            return_hint (bool, optional): Controls whether a hint for the riddle should be returned.
                Defaults to False.

        Raises:
            IncorrectAnswer: Exception for incorrect answer.

        Returns:
            str: The result of the evaluation of the answer.
        """

        if self._riddle.check_answer(answer):
            return "Your answer was correct. You may pass."
        elif return_hint:
            return (
                "Your answer was wrong. Hint: The answer starts with the letter "
                f"'{self._riddle.get_hint()}'."
            )
        else:
            raise IncorrectAnswer("Your answer was wrong. You shall not pass.")

    @staticmethod
    def sleep(duration: int = 5) -> str:
        """Puts the Sphinx to sleep for requested durationn

        Args:
            duration (int, optional): Sleep duration in years. Defaults to 5.

        Returns:
            str: A confirmation that the Sphinx will sleep for the requested period
        """
        return f"I am tired of waiting. I will sleep for {duration} years."
