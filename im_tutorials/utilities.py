def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def flatten_lists(lst):
    """Remove nested lists."""
    return [item for sublist in lst for item in sublist]
