def plusdoi(functie):
    def wrapper(*args, **kwargs):
        return functie(2, *args, **kwargs)  #   functie(2, 6) V

    return wrapper


def pluscinci(functie):
    def wrapper(*args, **kwargs):  # kwargs = [2]
        return functie(5, *args, **kwargs)  # functie(5, 2, 6)

    return wrapper


@pluscinci
@plusdoi
def adunare(primul, urmatorul, curentul):
    return f"{primul=} {urmatorul=} {curentul=}"


print(adunare(6))
