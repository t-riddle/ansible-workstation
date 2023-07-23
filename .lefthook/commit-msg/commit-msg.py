import re
import sys

pattern = r"(feat|fix|maint|ci|docs|chore)[!]{0,1}\:.*"
commit_file = sys.argv[1]


def head(filename, count=1):
    with open(filename, 'r') as f:
        lines = [f.readline() for line in range(1, count+1)]
        return lines


commit_orig = head(commit_file, 1)
commit = commit_orig[0].replace("\r", "").replace("\n", "")

if re.fullmatch(pattern, commit):
    print("Commit message is valid!")
else:
    print(
        f""""'{commit}' does not match the required commit pattern. Should follow syntax:
        (feat|fix|maint|ci|docs|chore): (message)
        For breaking changes, add '!' after the prefix.

        Example: 'feat: Added feature XYZ' or 'feat!: Added non-backwards compatible change XYZ'
        """
    )
    exit(1)