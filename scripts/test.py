import os

with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    print("key=value", file=f)