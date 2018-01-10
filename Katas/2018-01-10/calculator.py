class NegativeNumberException(ArithmeticError):
    def __init__(self, error_message):
        self.error_message = error_message


class StringCalculator:
    def __init__(self):
        self.delimiter = ","

    def get_delimiters(self, number_string):
        parts = number_string.split(sep="\n")
        first_char = number_string[2]
        if first_char == "[":
            delimiters = [x.replace("]", "") for x in parts[0].split(sep="[")]
            return delimiters
        return [first_char]

    def reset_delimiters(self, number_string, delimiters):
        new_number_string = number_string
        for delimiter in delimiters:
            new_number_string = new_number_string.replace(
                delimiter, self.delimiter)
        return new_number_string

    def check_for_negatives(self, numbers):
        negatives = []
        negatives_exists = False
        for a_number in numbers:
            if a_number < 0:
                negatives.append(str(a_number))
                negatives_exists = True
        if negatives_exists:
            raise NegativeNumberException(
                "negatives not allowed: " + ",".join(negatives))

    def sum_number_string(self, number_string):
        numbers = [
            int(a_number)
            for a_number in number_string.split(sep=self.delimiter)
            if a_number != "" and int(a_number) < 1000
        ]
        self.check_for_negatives(numbers)
        return sum(numbers)

    def clean_number_string(self, number_string):
        return number_string.replace("//", "").replace("[", "").replace("]", "")

    def add(self, number_string):
        if number_string == "":
            return 0

        if "//" in number_string:
            cleaned_number_string = self.clean_number_string(number_string)
            delimiters = self.get_delimiters(number_string)
            number_string = self.reset_delimiters(cleaned_number_string, delimiters)

        if "\n" in number_string:
            number_string = self.reset_delimiters(number_string, ["\n"])

        if self.delimiter in number_string:
            return self.sum_number_string(number_string)

        return int(number_string)
