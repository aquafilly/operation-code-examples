import os
import re

# Regex used to match a timestamp with format: yyyy-MM-dd HH:mm:ss,fff
line_regex = re.compile(r'[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9],[0-9]{3}')

log_file = os.path.join('C:', os.sep, 'AppointmentSystem', 'Logs', 'TRSServiceLog20180601')
with open(log_file, "r") as in_file:
    re.findall()
    for line in in_file:
        if (line_regex.search(line)):
            print(line)