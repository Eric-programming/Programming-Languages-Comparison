try:
    raise ValueError("invalid!")
except ValueError as error:
    print(str(error) + " input")
finally:
    print("Finishd")
