import re



class Time:
    def __init__(self, data: dict[str, str]):
        """
        Initialize the Time object with sanitized attribute names.

        Args:
            data (dict): A dictionary where keys are attribute names and values are their corresponding values.
        """
        self.data = data
        for key, value in data.items():
            # Sanitize key (remove all special characters, spaces, numbers except underscore)
            sanitized_key = re.sub(r"[^a-zA-Z_]", "", key)
            try:
                setattr(self, sanitized_key, str(value))
            except AttributeError:
                pass # Ignore invalid attribute names