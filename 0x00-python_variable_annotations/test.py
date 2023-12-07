import os

# Get all python files in current directory
python_files = [f for f in os.listdir() if f.endswith('.py')]

for file in python_files:
    with open(file, 'r+') as f:
        lines = f.readlines()

        # Check if shebang is present
        if not lines[0].startswith('#!/usr/bin/env python'):
            lines.insert(0, '#!/usr/bin/env python\n')

        # Check if docstring is present
        if not lines[1].startswith('"""'):
            lines.insert(1, '"""\nThis is a Python script.\n"""\n')

        # Write back to file
        f.seek(0)
        f.writelines(lines)