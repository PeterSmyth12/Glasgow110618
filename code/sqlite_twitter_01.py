# creating a table in sqlite
import sqlite3

conn = sqlite3.connect("ps_trending.sqlite")
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn="trends", nf="timestamp", ft="Text"))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn="trends", cn="woeid", ct="INTEGER"))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn="trends", cn="name", ct="Text"))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn="trends", cn="url", ct="Text"))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn="trends", cn="tweet_volume", ct="INTEGER"))
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn="trends", cn="query", ct="Text"))

conn.commit()
conn.close()
