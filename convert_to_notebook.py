import json
import os

# Define the notebook structure
notebook = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.10"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# Read the Python file and convert to notebook cells
with open('D:\\Thesis Paper\\Noton Folder\\Final\\Finals\\thesis_claude\\PI-PINN_Standalone.py', 'r') as f:
    content = f.read()

# Split the content into sections based on markdown headers
sections = content.split('## ')[1:]  # Skip the first empty element

for section in sections:
    # Split into header and code
    lines = section.split('\n')
    header = lines[0].strip()
    code = '\n'.join(lines[1:])

    # Add markdown cell for the header
    notebook["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [f"# {header}"]
    })

    # Add code cell for the content
    notebook["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "source": code.split('\n'),
        "outputs": []
    })

# Save the notebook
with open('D:\\Thesis Paper\\Noton Folder\\Final\\Finals\\thesis_claude\\PI-PINN_Standalone.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Jupyter notebook created successfully!")