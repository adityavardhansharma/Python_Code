pip install tqdm

import time
for i in range(10):
    time.sleep(1)
    from tqdm import tqdm
import time
for i in tqdm(range(10)):
    time.sleep(1)

    