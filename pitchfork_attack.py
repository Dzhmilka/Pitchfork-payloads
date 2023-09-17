input_passlist = "passlist.txt" # Existing file with passwords for brute force
output_passlist = "new_passlist.txt" # File with modified password list
output_userlist = "userlist.txt" # File with users

user1 = "john" # Login with known password
user2 = "admin" # Login to be brute forced
password1 = "correct_password" # Correct password for the first user

with open(input_passlist, "r") as inpass, open(output_passlist, "w") as outpass:
    line_count = sum(1 for line in inpass)
    inpass.seek(0)
    
    with open(output_userlist, "w") as outuser:
        for i, line in enumerate(inpass):
            word = line.strip()
            outpass.write(f"{password1}\n{word}")
            outuser.write(f"{user1}\n{user2}")

            if i < line_count - 1:
                outpass.write("\n")
                outuser.write("\n")

print(f"Modified password list: {output_passlist}")
print(f"Created user list: {output_userlist}")