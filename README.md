# About
This repository contains Python code to configure user list and password list for a pitchfork attack in Burp Suite.


## When is it useful?
This code is useful when dealing with a website that has a limited number of authentication attempts but also features a weakness that resets the attempt counter after a successful login. In such cases, you may want to create payloads where Burp Suite uses one attempt to log in to the site with one user and another attempt to try a password for a different user. This code helps you achieve this goal and creates all the necessary files for a brute force attack.


## How does it work?
First, it declares variables where:
- **input_passlist** takes a file with passwords for brute force;
- **output_passlist** takes the name of a file for the modified password list to be created after code execution;
- **output_userlist** takes the name of a file for two users, which will be created after code execution;
- **user1** takes the login of the first user, for whom you know both credentials;
- **user2** takes the login of the user whose password you want to brute force;
- **password1** takes the password of the first user;

After receiving all the data for these variables, the code proceeds to the main action. It creates the **output_passlist** file and alternately inserts passwords for the known user and passwords from the **input_passlist**.
At the same time, the code creates another file for users and alternately adds the known username and the username for which you want to brute force the password. It creates as many users as there are passwords in the new list.


## How to use it?
At first: Download this Python file to the folder that ideally contains your initial password file.
To achieve your goal of creating the necessary files, you only need to change the values of the variables listed above. 


Replace "passlist.txt" with the name of your file (or the file's path) containing passwords:
```py
input_passlist = "passlist.txt"
```

Replace "new_passlist.txt" with your desired name for the modified file containing passwords:
```py
output_passlist = "new_passlist.txt"
```

Replace "userlist.txt" with your desired name for the newly created file containing usernames:
```py
output_userlist = "userlist.txt"
```

Instead of "john", enter the username for which you have a valid password:
```py
user1 = "john"
```

Instead of "admin", enter the username for which passwords will be brute-forced:
```py
user2 = "admin"
```

Instead of "correct_password", enter the valid password for user1:
```py
password1 = "correct_password"
```

## Conclusion
And so, you are ready to go! Run the code and use the newly created files as a payload for a pitchfork attack in Burp Suite. 

Happy hacking! 👾
