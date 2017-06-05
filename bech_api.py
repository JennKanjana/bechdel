import requests
import MySQLdb

r = requests.get('http://bechdeltest.com/api/v1/getAllMovieIds')
for dict in r.json():
  #print dict['imdbid']
  imdbid = dict['imdbid']
  bt = requests.get('http://bechdeltest.com/api/v1/getMovieByImdbId?imdbid=%s' \
    % imdbid)
  bt = bt.json()

  conn = MySQLdb.connect(user="jk", db="bechdel")
  cur = conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS bmovie " \
      "(imdbid INTEGER NOT NULL, rating TEXT, title TEXT, `year` TEXT" \
      ")")
  cur.execute("INSERT INTO bmovie (imdbid, rating, title, `year`) VALUES " \
      "(%s, %s, %s, %s)", (bt["imdbid"], bt["rating"], bt["title"], bt["year"]))


  conn.commit()
