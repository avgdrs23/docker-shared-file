#!/usr/bin/env python3

import time
import sys

name=sys.argv[1]
time_of=int(sys.argv[2])
filename="data/file.txt"

while True:
   with open(filename, "a") as f:
      f.write(f"{name} was here:\n")
      #f.flush()
   time.sleep(time_of)



   
