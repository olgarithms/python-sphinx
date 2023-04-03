from dataclasses import dataclass


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> str:
        return self.answer[0]
