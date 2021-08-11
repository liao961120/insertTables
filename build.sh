pandoc -F pandoc-crossref -F custom-table.py README.md -o docs/index.html -s
pandoc -F pandoc-crossref -F custom-table.py README.md -o docs/README.tex -s
