import sys
import json
import os

PRINT_TARGET = os.getenv("SCRIPT_PRINT_TARGET")

def log(msg, print_target=PRINT_TARGET):
    if not print_target:
        print(msg)
    elif print_target.lower() == "stderr":
        print(msg, file=sys.stderr)
    elif print_target.lower() == "none":
        return
    else:
        raise Exception(f"Unknown print target: {print_target}")

log("::group::Script Output")
log("Script starting")
output = {"element1": "Foo", "element2": 2, "element3": "bar"}
# print("I'm a screw up!")
print(json.dumps(output))
log("Script ending")
log("::endgroup::")