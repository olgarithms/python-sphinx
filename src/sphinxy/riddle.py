from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Evaluates given answer against the riddle answer

        Args:
            answer (str): Riddle answer under test

        Returns:
            bool: True if answer is correct, False otherwise
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Gives a hint for the answer

        Yields:
            Iterator[str]: the answer, revealed one letter at a time
        """
        yield from iter(self.answer)
