import sys
import json

print("Script starting", file=sys.stderr)
output = {"element1": "Foo", "element2": 2, "element3": "bar"}
print(json.dumps(output))
print("Script ending", file=sys.stderr)