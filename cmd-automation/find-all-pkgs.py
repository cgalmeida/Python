#finds all of the Python packages installed

from subprocess import Popen, PIPE
import json
import pprint

# Use the with context manager to run subprocess.Popen()
with Popen(["pip","list","--format=json"], stdout=PIPE) as proc:
  # Pipe the output of subprocess.Popen() to stdout
  result = proc.stdout.readlines()
  
# Convert the JSON payload to a Python dictionary
# JSON is a datastructure similar to a Python dictionary
converted_result = json.loads(result[0])

# Display the result in the IPython terminal
pprint.pprint(converted_result)
