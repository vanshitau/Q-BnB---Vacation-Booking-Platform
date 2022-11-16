from qbay.models import (
    register
)
from qbay import app

# Using readlines()
sqlfile = open('Generic_SQLI.txt', 'r')
Lines = sqlfile.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    register(id=line, name=line, email=line, password=line)