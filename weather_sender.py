import ezgmail

print(ezgmail.LOGGED_IN)

ezgmail.send('customcaneco@gmail.com', 'You\'re late', """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
""", mimeSubtype='html')
