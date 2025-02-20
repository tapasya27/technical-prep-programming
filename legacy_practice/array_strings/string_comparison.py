def string_compression(string):
    if len(string) == 0:
        return ""

    prev = string[0]
    count = 0
    compressed = []
    for c in string:

        if prev == c:
            count += 1
        else:
            compressed.append(prev)
            compressed.append(str(count))
            count = 1
        prev = c

    compressed.append(prev)
    compressed.append(str(count))
    output = "".join(compressed)
    if len(output) > len(string):
        return string
    else:
        return output

print(string_compression("AAAccaaAAbCCCCCb"))
