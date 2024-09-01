import re

class MyString:
    def __init__(self, value=''):
        self._value = None
        self.value = value 

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        sanitized_value = re.sub(r'[.!?]+', '.', self._value)
        sentences = [s for s in sanitized_value.split('.') if s.strip()]
        return len(sentences)
