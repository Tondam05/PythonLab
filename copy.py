l = [35,53,(525,6743),64,63,[743,754,757]]
def flatten(xs):
    result = []
    if isinstance(xs, (list, tuple)):
        for x in xs:
            result.extend(flatten(x))
    else:
        result.append(xs)
    return result

print(flatten(l))