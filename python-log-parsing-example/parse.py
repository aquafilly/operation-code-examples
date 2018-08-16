import os
import re

# Regex used to match a timestamp with format: yyyy-MM-dd HH:mm:ss,fff
time_stamp_regex = re.compile(r'^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9],[0-9]{3}')
matches = 0
log_file = os.path.join('C:', os.sep, 'AppointmentSystem', 'Logs', 'TRSServiceLog20180601')
with open(log_file, "r") as in_file:
    for line in in_file:
        datetime_found = time_stamp_regex.match(line)
        if datetime_found:
            log_entry_timestamp = datetime_found.group()
            print(log_entry_timestamp)
        if (time_stamp_regex.search(line)):
            matches += 1
print(matches)