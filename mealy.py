def mealy_c_comment(s):
    state = "A"
    outputs = []
    trace = [state]

    for ch in s:
        # Treat any non-star, non-slash character as 'a'
        inp = ch if ch in ("*", "/") else "a"

        if state == "A":
            state, out = ("B", 0) if inp == "/" else ("T", 0)
        elif state == "B":
            state, out = ("C", 0) if inp == "*" else ("T", 0)
        elif state == "C":
            state, out = ("D", 0) if inp == "*" else ("C", 0)
        elif state == "D":
            if inp == "/":
                state, out = ("T", 1)   # Successfully closed comment
            elif inp == "*":
                state, out = ("D", 0)
            else:
                state, out = ("C", 0)
        elif state == "T":
            state, out = ("T", 0)

        outputs.append(out)
        trace.append(state)

    accepted = (1 in outputs) and (outputs[-1] == 1)
    
    print(f"input : {s}")
    print("states: " + " -> ".join(f"({st})" for st in trace))
    print(f"output: {' '.join(str(o) for o in outputs)}")
    print(f"result: {'ACCEPTED' if accepted else 'REJECTED'}\n")


# Accepted tests from slide
mealy_c_comment("/*a*/")
mealy_c_comment("/**/")
mealy_c_comment("/***/")

# Rejected tests from slide
mealy_c_comment("//aaaa")
mealy_c_comment("/**/a")