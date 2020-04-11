install:
	pip install -r requirements.txt

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name __pycache__ -delete
