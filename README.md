# About
This repository has a python code to configurate user list and password list for a pichfork attack in Burp Suite


## When is it useful?
If you face a website, which has limited authentication attempts, but also contains a weakness of resetting attempts counter after a successful login attempt - you might want to create a payloads, 
where Burp Suite will use one attempt to login on site and another to try a password for another user. This code helps you with this goal and creates all neccessary files for a brute force attack.


## How does it work?
At first it declares a variables, where:
- **input_passlist** takes a file with passwords for a brute force
- **output_passlist** takes a name of a file with modified password list which will be created after code execution
- **output_userlist** takes a name of a file with two users which will be created after code execution
- **user1** takes a login of the first user, for which you know both credentials
- **user2** takes a login of the user, password for which you want to brute force
- **password1** takes a password of the first user

After receiving all data for variables code proceeds to the main action. It creates file **output_passlist** and alternatly inputs password for the known user and password from the **input_passlist**.
At the same time, code creates another file for users and alternatly adds known username and username whose password you want to brute force. It creates as many users as there passwords in the new list.


## How to use it?
At first - download this python file to the folder, which (preferably) contains your initial password file.
To achieve your goal of creating files that you need - you must just change value of the variables counted above. 


Instead of "passlist.txt" paste the name of your file (or path to the file) with passwords.
```py
input_passlist = "your_file_name.txt"
```

Instead of "new_passlist.txt" write a desired name for the modified file with passwords.
```py
output_passlist = "new_passlist.txt"
```

Instead of "userlist.txt" write a desired name for the newly created file with usernames.
```py
output_userlist = "userlist.txt"
```

Instead of "john" write a username for which you have a valid password.
```py
user1 = "john"
```

Instead of "admin" write a username, passwords for which will be brute forced.
```py
user2 = "admin"
```

Instead of "correct_password" write a valid password for the user1.
```py
password1 = "correct_password"
```

## Conclusion
And so you are ready to go! Run the code and use new created file as a payload for pitchfork attack in Burp Suite. 

Happy hacking! 👾
