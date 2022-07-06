text_file = open(r"F:\Practice programms\Extras\text.txt", "r")
file_content = text_file.read()
file_content = file_content.replace("minute", "second")
text_file.close()

retext = open(r"F:\Practice programms\Extras\text.txt", "w")
retext.write(file_content)
retext.close()
