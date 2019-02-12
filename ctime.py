#!/usr/bin/env python

import time

ctime = time.strftime(
    '%Y-%m-%d %H:%M:%S',time.localtime(time.time())
)

print(ctime
      )