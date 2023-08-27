from datetime import datetime
import re
import pytz


def convert_timestamp_to_datetime(timestamp):
    if timestamp is None:
        return None

    # Convert the timestamp (milliseconds since epoch) to a datetime object
    timestamp_seconds = int(timestamp) / 1000.0
    dt_utc = datetime.utcfromtimestamp(timestamp_seconds)

    # Define the IST timezone
    ist = pytz.timezone('Asia/Kolkata')

    # Convert UTC datetime to IST
    dt_ist = dt_utc.replace(tzinfo=pytz.utc).astimezone(ist)

    # Format the datetime as a SQL DATETIME string (YYYY-MM-DD HH:MM:SS)
    return dt_ist.strftime('%Y-%m-%d %H:%M:%S')
# function to remove emojis from the texts


def remove_emojis(text):
    if text is None:
        return None
    # Define a regular expression pattern to match emojis
    emoji_pattern = re.compile("["
                               "\U0001F600-\U0001F64F"  # Emoticons
                               "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
                               "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
                               "\U0001F700-\U0001F77F"  # Alchemical Symbols
                               "\U0001F780-\U0001F7FF"  # Geometric Shapes
                               "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               "\U0001FA00-\U0001FA6F"  # Chess Symbols
                               "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               "\U0001FB00-\U0001FBFF"  # Symbols and Pictographs Extended-B
                               "\U0001FC00-\U0001FCFF"  # Symbols and Pictographs Extended-C
                               "\U0001FD00-\U0001FDFF"  # Symbols and Pictographs Extended-D
                               "\U0001FE00-\U0001FEFF"  # Combining Diacritical Marks Extended
                               "\U0001FF00-\U0001FFFF"  # Combining Diacritical Marks Extended
                               "\U00002702-\U000027B0"  # Dingbats
                               "\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)

    # Use the sub() method to remove emojis from the text
    cleaned_text = emoji_pattern.sub(r'', text)

    return cleaned_text


def convert_to_sql_datetime(date_str):
    if date_str == "":
        return None
    # Define the input format of your date string
    input_format = "%d/%m/%Y %H:%M"

    # Parse the input date string into a datetime object
    date_obj = datetime.strptime(date_str, input_format)

    # Convert the datetime object to SQL datetime format
    sql_datetime = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    return sql_datetime
