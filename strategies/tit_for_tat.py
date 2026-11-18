def play(history):
    if len(history)>0:
        if history[-1][1] == "C":
            return "C"
        if history[-1][1] == "D":
            return "D"
    else:
        return "C"