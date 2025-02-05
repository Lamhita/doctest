# How to install

## Local Deployment
1. To ensure a clean installation, create a new Python environment:
`cd ~/venv`
`python3 -m venv doctest`

2. Change to your git directory and clone the repository, e.g.:
`cd ~/git`
`git clone https://github.com/Lamhita/doctest.git`

3. Activate the environment:
`source ~/venv/doctest/bin/activate`
4. Install mkdocs:
`pip install mkdocs`
5. Install the `material` theme and swagger plugin:
`pip install mkdocs-material mkdocs-render-swagger-plugin`
6. Enable PlantUML support:
`pip install plantuml-markdown`
7. Enable advanced markdown syntax:
`pip install pymdown-extensions`
8. Build the documentation:
`mkdocs build`
9. Serve the docs on your local machine:
`mkdocs serve`
10. Wait for a moment until you see:
`INFO    -  [21:50:16] Serving on http://127.0.0.1:8000/`
You're set and done!
Open the [link](http://127.0.0.1:8000/) locally

