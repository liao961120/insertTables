---
title: "Pandoc Filter to Insert Arbitrary Complex Tables"
linkReferences: true
links-as-notes: true
header-includes: |
    \usepackage{multirow}
---

Outputs: 
[Web Page](https://yongfu.name/pandoc-filter/) /
[LaTeX](https://yongfu.name/pandoc-filter/README.tex) /
[PDF](https://yongfu.name/pandoc-filter/README.pdf) /
[Overleaf](https://www.overleaf.com/docs?snip_uri=https://yongfu.name/pandoc-filter/README.tex&engine=xelatex)


## Dependencies

Make sure you have Pandoc and [pandoc-crossref][crossref] installed (callable from cmd). 
In addition, Python 3 and [`pandocfilters`](https://github.com/jgm/pandocfilters) are required:

```bash
pip install pandocfilters
```

[crossref]: https://github.com/lierdakil/pandoc-crossref


## Usage

Write your complex tables in HTML in `tables.html` and in LaTeX in `tables.tex`.
<https://tablesgenerator.com> is a good resource for constructing complex tables.
To insert tables into the output HTML/LaTeX document, 
use the syntax `<COMMENT> tbl:table-id <COMMENT>` to mark the beginning and
`<COMMENT> END <COMMENT>` to mark the end of a table definition in `tables.html` and `tables.tex`.
`<COMMENT>` corresponds to `%` in LaTeX and `<!--` and `-->` in HTML. 
`tbl:table-id` is the identifier of the table used for cross-referencing in the markdown source. 
Refer to [pandoc-crossref][crossref] for details of cross referencing tables.

To compile the documents, apply the filter `custom-table.py` **AFTER** `pandoc--crossref` in the command line.

```bash
pandoc -F pandoc-crossref -F custom-table.py README.md -o README.tex
pandoc -F pandoc-crossref -F custom-table.py README.md -o README.html
```


## Example

| Placeholder |
|-------------|
| Table       |

Table: This is a _complex table_, **written** in `tables.tex` and `tables.html`. {#tbl:custom-table}

See @tbl:custom-table.


Column A | Column B
---------|---------
A1       | B1
A2       | B2

Table: This is a normal table written in markdown, which will not be replaced. {#tbl:normal-table}
