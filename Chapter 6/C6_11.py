name = input("Enter your name : ")
desc = input("Describe yourself : ")
html = open(r"F:\Practice programms\Chapter 6\Web_page_C6_10.html", "w")
html.write(
    f"<html><head></head><body><center><h1>{name}</h1></center><hr />{desc}<hr /></body></html>"
)
print("Your web page has been created.")
