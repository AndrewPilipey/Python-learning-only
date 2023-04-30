import os
import time

spisok = []
for adress, dirs, files in os.walk(r'C:\Users\andre\OneDrive\Рабочий стол\Parsing'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)

print(spisok)