---
title: "Pandoc Filter to Insert Arbitrary Complex Tables"
linkReferences: true
---

# Pandoc Filter to Insert Arbitrary Complex Tables 

## Dependencies

Make sure you have Pandoc and [pandoc-crossref][crossref] installed (callable from cmd). In addition, Python 3 and the libraries below are required:

```bash
pip install pandocfilters, pypandoc
```

[crossref]: https://github.com/lierdakil/pandoc-crossref

## Usage

Put complex tables in `tables.tex` and `tables.html`. Mark them with [pandoc-crossref][crossref]'s `tbl:table-id` syntax in the comments.

Apply the filter **after** `-F pandoc--crossref` in the command line.

```bash
pandoc -F pandoc-crossref -F custom-table.py README.md -o README.tex
pandoc -F pandoc-crossref -F custom-table.py README.md -o README.html
```


## Example

| Placeholder |
|-------------|
| Table       |

Table: This is a _complex table_, written in `tables.tex` and `tables.html`. {#tbl:custom-table}

See @tbl:custom-table.


Column A | Column B
---------|---------
A1       | B1
A2       | B2

Table: This is a normal table written in markdown, which will not be replaced. {#tbl:normal-table}
