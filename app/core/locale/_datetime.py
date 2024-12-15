from datetime import datetime, timedelta
import random

class DateTime:
    """
    DateTime class to generate datetime objects
    """

    @staticmethod
    def get_date(between_yr:str="2020-2025", format:str="%d/%m/%Y", era:str=""):
        """
        Get date based on the era
        """
        if "now"==era:
            return datetime.now().strftime(format)
        try:
            _from = between_yr.split("-")[0]
            _to = between_yr.split("-")[1]
            _rand_yr = random.randint(int(_from), int(_to))
            _date = (datetime.now() - timedelta(days=random.randint(1,10000)))
            _yr = _date.year
            return _date.strftime(format).replace(str(_yr), str(_rand_yr))

        except Exception as e:
            return str(e)
        
    @staticmethod
    def get_time(era:str="now"):
        """
        Get time based on the era
        """
        if era=="past":
            return (datetime.now() - timedelta(hours=random.randint(1, 23))).time()
        elif era=="future":
            return (datetime.now() + timedelta(hours=random.randint(1, 23))).time()
        return datetime.now().time()
    
    @staticmethod
    def get_datetime(era:str="past", format:str="%d/%m/%Y %H:%M:%S"):
        """
        Get datetime based on the era
        """
        if era=="past":
            return (datetime.now() - timedelta(days=random.randint(1,1000))).strftime(format)
        elif era=="future":
            return (datetime.now() + timedelta(days=random.randint(1,1000))).strftime(format)
        return datetime.now().strftime(format)

print(DateTime.get_datetime(""))