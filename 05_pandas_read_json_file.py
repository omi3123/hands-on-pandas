# Read JSON File in Pandas

import pandas as pd
df = pd.read_json('data.json')
print(df)

# JSON Not Structured as List?

import pandas as pd
import json
with open('data.json') as f:
    data = json.load(f)
df = pd.json_normalize(data)
print(df)

# Deeply Nested JSON

# Suppose json file contains:
[
  {
    "ID": 1,
    "Student": {
      "Name": "Ali",
      "Details": {"Age": 20, "City": "Lahore"}
    }
  },
  {
    "ID": 2,
    "Student": {
      "Name": "Zara",
      "Details": {"Age": 21, "City": "Islamabad"}
    }
  }
]
import json
import pandas as pd
with open('deep_nested.json') as f:
    data = json.load(f)
df = pd.json_normalize(data, record_path=None)
print(df)
