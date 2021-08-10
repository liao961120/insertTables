local inspect = require('inspect')

-- if FORMAT:match 'html' then
--   end


function get_table_caption (tbl)
    -- Remove CUSTOM.TABLE in table caption
    local caption = pandoc.List(tbl.caption.long)
    local e, idx = caption[1].content:find_if(is_custom_table)
    table.remove(caption[1].content, idx)
    tbl.caption.long = pandoc.List(tbl.caption.long)
    
    -- Write caption as latex or html
    local sub_doc = pandoc.Pandoc(tbl.caption.long)

    -- return tbl.caption.long
  end



function is_custom_table(inl)
    return (inl.t) and (inl.t == "Str") and (inl.c == "CUSTOM.TABLE")
  end