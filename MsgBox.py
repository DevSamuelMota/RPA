import ctypes
import sys

msg = sys.argv[1]
title = sys.argv[2]
style = int(sys.argv[3])

ctypes.windll.user32.MessageBoxW(0, msg, title, style)

# Styles
# 0: ok
# 1: OK|Cancel
# 2: Abort|Retry|Ignore
# 3: Yes|No|Cancel
# 4: Yes|No
# 5: Retry|Cancel
# 6: Cancel|Try Again|Continue
