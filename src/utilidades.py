from datetime import datetime, timedelta

def current_time():
    """Devuelve la fecha y hora actual en formato legible."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def days_between(date1, date2):
    """Calcula la diferencia en días entre dos fechas."""
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def add_days(date_str, days):
    """Suma un número de días a una fecha dada."""
    date = datetime.strptime(date_str, "%Y-%m-%d")
    new_date = date + timedelta(days=days)
    return new_date.strftime("%Y-%m-%d")
