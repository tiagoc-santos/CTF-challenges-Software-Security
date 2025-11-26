# Challenge `I challenge you for a race` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Race Condition with symbolic link
- Where: Where is the vulnerability present
  - `challenge/read_file.c` from the line 14 to 21
- Impact: What results of exploiting this vulnerability
  - Allows an non authorized user to read the content of the `flag` file

## Steps to reproduce

1. Create a `dummy` file that you have access to (`touch dummy`)
2. Create a symbolic link to that file (`ln -sf dummy pointer`) 
3. Run the `read_file.c` with the symbolic link as argument
4. At the same time as 3, change the symbolic link to the file you want access to (`challenge/flag`).

Note: These steps need to be repeated in a loop until the timing matches. `access()` must check the symlink while it points to a file you own (`dummy`), but the program must read the file after the symlink has been switched to the `flag`. Thus, step 4 must happen after the access verification and before the program reads the content.

[(POC)](i_challenge_you_for_a_race_poc.sh)
