"""Helper functions."""

def flatten_dict(d, parent_key='', sep='_'):
    """Flatten a nested dictionary.
    Args:
        d (dict): Nested dictionary.
        parent_key (str): Parent key.
        sep (str): Separator.
    Returns:
        dict: Flattened dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            # Recursively flatten nested dictionaries
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
