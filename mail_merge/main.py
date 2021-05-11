names = []
with open("./mail_merge/Input/Names/invited_names.txt") as file:
    for name in file.readlines():
        names.append(name.strip())

with open("./mail_merge/Input/Letters/starting_letter.txt") as file:
    content = file.read()
    for name in names:
        new_content = content.replace("[name]", name)
        with open(f"./mail_merge/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
            f.write(new_content)