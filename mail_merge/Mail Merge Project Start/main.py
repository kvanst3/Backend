#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

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
