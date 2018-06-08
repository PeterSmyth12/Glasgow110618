import sqlite3
conn = sqlite3.connect("ps_trending.sqlite")
c = conn.cursor()

c.execute('SELECT query, max(tweet_volume) FROM trends where tweet_volume > 0 and substr(query,1,1) = "#" group by query order by tweet_volume desc')
all_rows = c.fetchall()

for x in all_rows:
    print x[0], x[1]
