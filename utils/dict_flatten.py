def flatten(objective:dict) -> dict:
    # Iterates over objective dictionary and flattens it
    # assigning the leaves of the tree to the corresponding keys
    # of the final diccionary. It should iterate over
    # objective using a list as a stack

    stack:dict = [objective]
    result:dict = {}

    while stack:
        current:dict = stack.pop()

        for key, value in current.items():
            if isinstance(value, dict):
                stack.append(value)
            else:
                result[key] = value

    return result
