def convert_kg_to_float(val):
    """
    Convert the weight (kg) value to a float
     - Remove "kg" suffix
     - Convert to float type
    """
    new_val = val.replace(' kg','')
    return float(new_val)

def convert_reps_to_int(val):
    """
    Convert the repetitions value to an int
    """
    return int(val)
