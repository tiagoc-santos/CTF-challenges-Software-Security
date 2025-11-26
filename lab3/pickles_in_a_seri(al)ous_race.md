# Challenge `Pickles in a seri(al)ous race ` writeup

- Vulnerability: What type of vulnerability is being exploited
  - Race Condition with remote code execution
- Where: Where is the vulnerability present
  - `mustard.stt.rnl.tecnico.ulisboa.pt:25653` server code (specially in lines 98 - 100)
- Impact: What results of exploiting this vulnerability
  - Allows an user to execute code remotely

## Steps to reproduce

1. Open two separate connections to the server where one is in classy note mode and the other is in free note mode
2. Wait until both connections reach the point where they must choose between reading and writing
3. In the free note connection, create a note whose contents are a serialized object produced with `pickle.dumps()`. The `__reduce__` method of the serialized class contains the commands you want executed (In this case, we use `find` and `cat` to list and read files in the `home` directory). Send this to the server.
4. In the classy note connection, read the note created in step 3. Because classy mode reads notes using `pickle.loads()`, the code in the `__reduce__` method will execute on the server. This causes the server to run your commands and, in this case, output the contents of `/home`, including the flag.

Note: Step 2 is required because switching between modes causes the directory and everything inside it to be deleted. If the free note connection ran first and the classy note connection followed, the note would be removed before the second connection could read it. By synchronizing both connections at the point where they choose between reading and writing, we ensure the note persists.

[(POC)](pickles_in_a_seri(al)ous_race_poc.py)
