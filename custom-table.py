import os
# import json
# import pypandoc
from pandocfilters import RawBlock, toJSONFilter, walk


def InsertCustomTables(key, value, format, meta):
    custom_tables = get_custom_tables(format)

    try: crossref = value[0][0]
    except: return None
    if key == 'Div' and crossref in custom_tables:
        caption = get_table_caption(value[1][0]["c"], format)
        table = custom_tables[crossref]
        table = insert_caption(caption, table, crossref, format)
        return RawBlock(format, table)


def get_table_caption(tbl, format):
    # with open("log", "w") as f: json.dump(tbl[1][1], f)
    caption = stringify3(tbl[1][1], format)
    # with open("log", "w") as f: f.write(caption)
    return caption


# def stringify2(x, format="html"):
#     """Write tree to text by calling Pandoc
#     """
#     doc = '{ "pandoc-api-version": [1, 22],"meta": { "linkReferences": { "t": "MetaBool", "c": true}}, "blocks":'
#     doc = doc + json.dumps(x) + '}'

#     # Catch result from Pandoc Writer
#     with open("temp.json", "w", encoding="utf-8") as f: f.write(doc)
#     result = pypandoc.convert_file('temp.json', format)
#     os.remove(f'temp.json')
#     return result


def stringify3(tree, format):
    """Custom interpretor for a partial tree, 
    expects a caption with a single paragraph (e.g., no code blocks)
    """
    result = []

    def go(key, val, format):
        if key == 'Plain':
            resolv = stringify3(val, format)
            result.append(resolv)
        elif key == 'Strong':
            resolv = stringify3(val, format)
            result.append(writeStrong(resolv, format))
        elif key == 'Emph':
            resolv = stringify3(val, format)
            result.append(writeEmph(resolv, format))
        elif key in ['Str', 'MetaString']:
            result.append(val)
        elif key == 'RawInline':
            result.append(val[1])
        elif key == 'Code':
            result.append(writeCode(val[1], format))
        elif key == 'Math':
            result.append(writeMath(val[1], format))
        elif key == 'Space' or key == 'SoftBreak' or key == 'LineBreak':
            result.append(" ")

    if isinstance(tree, list):
        for elem in tree:
            key, value = elem.get("t"), elem.get("c")
            go(key, value, format)
    elif isinstance(tree, dict):
        key, value = tree.get("t"), tree.get("c")
        go(key, value, format)

    return ''.join(result)


def get_custom_tables(format="latex"):
    CUSTOM_TABLES = {}

    cmt_s, cmt_e, end = '<!--', '-->', '<!-- END -->'
    if format == 'latex': cmt_s, cmt_e, end = '%', '%', '% END %'
    if format == 'latex': format = 'tex'
    format = 'tables.' + format
    if not os.path.exists(format): return {}

    with open(format, encoding="utf-8") as f:
        f = [ l for l in f ]

    inTable = False
    for line in f:
        if line.startswith(cmt_s) and "tbl:" in line:
            label = line.strip().lstrip(cmt_s).rstrip(cmt_e).strip()
            CUSTOM_TABLES[label] = ""
            inTable = True
        if line.startswith(cmt_s) and end in line:
            inTable = False
        if inTable:
            CUSTOM_TABLES[label] += line
    
    return CUSTOM_TABLES


def insert_caption(caption, table_text, crossRefLabel, format):
    if format == "latex":
        caption = '\\caption{' + caption + '}'
        tgt = '\\begin{tabular}'
        repl = f"{caption}\n{tgt}"
        return table_text.replace(tgt, repl)
    if format == 'html':
        caption = '<caption>' + caption + '</caption>'
        tgt = f'<table>'
        repl = f'<table id="{crossRefLabel}">' + caption
        return table_text.replace(tgt, repl)

# Custom writers used in stringify3()
def writeCode(x, format):
    if format == 'latex' or format == 'tex': return '\\texttt{' + x + '}'
    if format == 'html': return f"<code>{x}</code>"
    if format == 'markdown': return f"`{x}`"
    return x

def writeMath(x, format):
    if format == 'latex' or format == 'tex': return '\\(' + x + '\\)'
    if format == 'html': return f'<span class="math inline">{x}</span>'
    if format == 'markdown': return f"${x}$"
    return x

def writeStrong(x, format):
    if format == 'latex' or format == 'tex': return '\\textbf{' + x + '}'
    if format == 'html': return f'<strong>{x}</strong>'
    if format == 'markdown': return f"**{x}**"
    return x

def writeEmph(x, format):
    if format == 'latex' or format == 'tex': return '\\emph{' + x + '}'
    if format == 'html': return f'<em>{x}</em>'
    if format == 'markdown': return f"_{x}_"
    return x

if __name__ == "__main__":
    toJSONFilter(InsertCustomTables)
