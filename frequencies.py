"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    if len(items) == 0:
        pass
    else:
        frequencies.update({str(items[0]) : 1})
        for i in range(1, len(items)):
            if str(items[i]) in frequencies:
                frequencies[str(items[i])] += 1
            else:
                frequencies.update({str(items[i]) : 1})

    return frequencies
