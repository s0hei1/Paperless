class ThreeDigitStr(str):

    def __new__(cls, value):
        if not value.isdigit():
            raise ValueError("ThreeDigitStr only accepts digits")

        if len(value) != 3:
            raise ValueError("ThreeDigitStr only accepts three digits")

        return str.__new__(cls, value)

    def to_int(self):
        return int(self)
