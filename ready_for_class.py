import sys

errors = 0

if sys.version_info[0] < 3:
    print("- Error: Must be using Python 3.6"); errors += 1
else:
    print('+ Python 3')
try:
    import numpy as np
    print('+ Found numpy')
except:
    print("- Error: Missing numpy"); errors += 1

try:
    import pandas as pd
    print('+ Found pandas')
except:
    print("- Error: Missing pandas"); errors += 1

try:
    import tensorflow
    print('+ Found tensorflow')
except:
    print("- Error: Missing tensorflow"); errors += 1

try:
    import keras
    print('+ Found keras')
except:
    print("- Error: Missing keras"); errors += 1

if errors == 0:
    print('You\'re ready!')
else:
    print('You have %d thing(s) to fix...'%errors)
