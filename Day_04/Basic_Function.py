with open("E:/90-Days-Code-Journey/sample.txt", "r") as f:
    for line in f:
        if "python" in line.lower():
            print(" word found")
            print(" Line:", line)
            break
