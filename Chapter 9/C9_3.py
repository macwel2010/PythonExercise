code_dict = {
    "a": "a!",
    "b": "b!",
    "c": "c!",
    "d": "d!",
    "e": "e!",
    "f": "f!",
    "g": "g!",
    "h": "h!",
    "i": "i!",
    "j": "j!",
    "k": "k!",
    "l": "l!",
    "m": "m!",
    "n": "n!",
    "o": "o!",
    "p": "p!",
    "q": "q!",
    "r": "r!",
    "s": "s!",
    "t": "t!",
    "u": "u!",
    "v": "v!",
    "w": "w!",
    "x": "x!",
    "y": "y!",
    "z": "z!",
    ".": "#",
    ",": "*",
    " ": "$",
}
code_file = open("code_C9_3.txt", "r")
code_file_content = code_file.read().lower()
decode_file = open("decode_C9_3.txt", "w")
for i in code_file_content:
    if i in code_dict:
        decode_file.write(code_dict[i])
    else:
        print("nothing found")
decode_file.close()
