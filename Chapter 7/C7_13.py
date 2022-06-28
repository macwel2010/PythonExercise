import random

responses_file = open("8_ball_responses_C7_13.txt")
response_file_list = []

for i in responses_file:
    file_line = i.rstrip()
    response_file_list.append(file_line)


que = input("\nAsk any question.\n")
print(response_file_list[random.randint(0, 7)])
