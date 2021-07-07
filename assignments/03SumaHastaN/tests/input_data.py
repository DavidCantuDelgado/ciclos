# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["9"],
        # Outputs
        ["", "45"],
        # Message in case of failure
        "La suma no es correcta."
    ),
    # Test case 2
    (
        # Inputs
        ["155"],
        # Outputs
        ["", "12090"],
        # Message in case of failure
        "La suma no es correcta"
    ),
    # Test case 3
    (
        # Inputs
        ["12090"],
        # Outputs
        ["", "73090095"],
        # Message in case of failure
        "La suma no es correcta"
    ),
    # Test case 4
    (
        # Inputs
        ["0"],
        # Outputs
        ["", "0"],
        # Message in case of failure
        "¿Consideraste el caso de que el input sea 0?"
    )
]

