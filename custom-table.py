import os
import json
import pypandoc
from pandocfilters import RawBlock, toJSONFilter, walk


def InsertCustomTables(key, value, format, meta):
    custom_tables = get_custom_tables(format)

    if key == 'Div' and value[0][0].startswith("tbl:"):
        crossRefLabel = value[0][0]
        caption = get_table_caption(value[1][0]["c"], format)
        table = custom_tables.get(crossRefLabel, None)
        if table is None: return RawBlock(format, caption)
        table = insert_caption(caption, table, crossRefLabel, format)
        return RawBlock(format, table)


def get_table_caption(tbl, format):
    caption_block = tbl[1][1]
    caption_block = clean_custom_label(caption_block)
    caption = stringify2(caption_block, format)
    return caption


def clean_custom_label(caption_block):
    def action(key, value, format, meta):
        if key == 'Str' and value == "CUSTOM.TABLE": return []
    return walk(caption_block, action, "", {})


def stringify2(x, format="html"):
    """Write tree to text by calling Pandoc
    """
    doc = '{ "pandoc-api-version": [1, 22],"meta": { "linkReferences": { "t": "MetaBool", "c": true}}, "blocks":'
    doc = doc + json.dumps(x) + '}'

    # Catch result from Pandoc Writer
    with open("temp.json", "w", encoding="utf-8") as f: f.write(doc)
    result = pypandoc.convert_file('temp.json', format)
    os.remove(f'temp.json')
    return result


def get_custom_tables(format="latex"):
    CUSTOM_TABLES = {}

    cmt_s, cmt_e, end = '<!--', '-->', '<!-- END -->'
    if format == 'latex': cmt_s, cmt_e, end = '%%%%', '%%%%', '%% END %%'
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
    with open("log", "w") as f: f.write(caption)
    if format == "latex":
        caption = '\\caption{' + caption + '}'
        tgt = '\\end{table}'
        # repl = caption + '\\label{' + crossRefLabel + '}' + '\\end{table}'
        repl = caption + '\\end{table}'
        return table_text.replace(tgt, repl)
    if format == 'html':
        caption = '<caption>' + caption + '</caption>'
        tgt = f'<table>'
        repl = f'<table id="{crossRefLabel}">' + caption
        return table_text.replace(tgt, repl)


if __name__ == "__main__":
    toJSONFilter(InsertCustomTables)
