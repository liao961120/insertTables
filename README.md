---
title: "Pandoc Filter to Insert Arbitrary Complex Tables"
linkReferences: true
tblPrefix: "Table"
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
pandoc -F pandoc-crossref --lua-filter insertTables.lua README.md -o README.tex
pandoc -F pandoc-crossref --lua-filter insertTables.lua README.md -o README.html
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


### Custom Caption Positions

By default, `insertTables.lua` looks for the string `\begin{tabular` and inserts the caption before it. In circumstances where `\begin{tabular}` or `\begin{tabularx}` are not present in the table's code, this filter will fail. To deal with these cases, you have to tell `insertTables.lua` where to insert the caption by placing the anchor `%caption%` in your table's code. This may also be useful when you want to place the caption **below** the table body. This can be achieved by placing the anchor `%caption%` **after** the `tabular` environment:

```latex
\begin{table}[]
    \centering
    \begin{tabular}{lllll}
        \hline
        \textbf{} & \multicolumn{4}{l}{Column Span} \\ \hline
        \multirow{2}{*}{Row Span} & a & b & d & f \\
         & c & d & e & g \\ \hline
        \end{tabular}
    %caption%
\end{table}
```

which results in @custom-caption-position.

| Placeholder |
|-------------|
| Table       |

Table: For LaTeX tables, you can define the position of the caption with the string `%caption%` in `tables.tex`. {#tbl:custom-caption-position}

