---
header-includes: |
    \usepackage{framed,xcolor}
    \definecolor{shadecolor}{gray}{0.9}
    \newenvironment{mybox}[1]
        { \begin{shaded}\noindent\textbf{#1}. }
        { \end{shaded} }

    <style>
    .Box {
        background: rgb(100, 209, 171);
        padding: 0.5em;
        border-radius: 0.3em;
    }
    .Box::before {
        content: attr(title);
        font-weight: bold;
    }
    .Box p {
        margin: 0.5em 0;
    }
    </style>
---

A paragraph. A paragraph. A paragraph. A paragraph. A paragraph. 

::: {.Box title="Title of the box"}
This is a custom block. This is a custom block. This is a custom block. This is a custom block. 
This is a custom block. This is a custom block. 

This is a custom block. This is a custom block. This is a custom block. 
:::::::::::


A paragraph. A paragraph. A paragraph. A paragraph. A paragraph. A paragraph. A paragraph. A paragraph. A paragraph. A paragraph. A paragraph. 