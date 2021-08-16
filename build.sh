pandoc -F pandoc-crossref --lua-filter insertTables.lua README.md -o docs/index.html -s
pandoc -F pandoc-crossref --lua-filter insertTables.lua README.md -o docs/README.tex -s
