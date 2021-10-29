import numpy as np
from main import *

passed = 0
failed = 0
for i in range(1,100):
    try:
        main()
        passed += 1
    except:
        failed += 1
        continue
print(f"Passed: {passed},\nFailed: {failed}")