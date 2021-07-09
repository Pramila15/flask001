# python3 app.py
<li>pip3 install flask</li>
<li>pip3 install Flask-RESTFUL</li>
<li>pip3 install Flask-JWT</li>
<li>pip3 install Flask-SQLAlchemy</li>
<ul>
<li>pip3 freeze</li>
<li>pip install virtualenv</li>
  <li>vitualenv venv --python=python3 </li>
  <li> source venv/bin/activate </li>
  <li> deactivate </li>
</ul>

#### Docker Commands
```
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
```
docker build . -t docker-flask
docker run -p 5000:5000 -t -i docker-flask:latest

To check -
docker ps
docker ps -a

To kill the port already in use
sudo lsof -i tcp:<port number>
kill -9 <pid>
