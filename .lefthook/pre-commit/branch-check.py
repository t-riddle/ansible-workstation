import re
import subprocess

pattern = r"(feature|bugfix|maintenance|hotfix|patch)/.*"
branches = subprocess.check_output(["git", "branch"]).splitlines()

for branch in branches:
    if '*' in branch.decode():
        current_branch = branch.decode()[2:]
        print(branch.decode()[2:])

if re.fullmatch(pattern, current_branch):
    print("Branch name is valid!")
elif re.fullmatch(r"(master|main)", current_branch):
    print(
        f"""
        Cannot commit directly to {current_branch}!
        Please create a new branch and open a merge request.
        """
    )
    exit(1)
else:
    print(
        f"""
        {current_branch} does not meet naming requirements.
        Please use the following branch naming standard:
        
        (feature|bugfix|maintenance|hotfix|patch)/description
        
        example: feature/added-feature
        """
    )
    exit(1)