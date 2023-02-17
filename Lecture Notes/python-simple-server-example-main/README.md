[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=555508835)

This repository includes a very simple Python web site, made for demonstration purposes only. Do **not** use the built-in `HTTPServer` class for production purposes!

To try it out:

1. Open this repository in Codespaces
2. Run the server:

```console
python server.py
```

2. Click 'http://0.0.0.0:8080' in the terminal, which should open the website in a new tab
3. Type different paths after the URL to see the effect on the GET requests in the logs
4. Try POSTing data by sending HTTP POST requests in the JS console:

```console
fetch('/', {method: 'POST', body: 'posted data'})
```

