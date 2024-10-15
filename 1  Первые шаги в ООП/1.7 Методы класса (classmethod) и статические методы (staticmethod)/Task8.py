from string import ascii_lowercase, digits

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        parts = number.split('-')
        if len(parts) != 4:
            return False
        return all(part.isdigit() and len(part) == 4 for part in parts)

    @staticmethod
    def check_name(name):
        words = name.split()
        if len(words) != 2:
            return False
        return all(all(char in CardCheck.CHARS_FOR_NAME for char in word) for word in words)
 