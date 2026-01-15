def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("#") and len(line) > 1 and line[1] != "#":
            return line[1:].strip()
    raise ValueError("No title found in markdown. Title must be the first line starting with '# '")