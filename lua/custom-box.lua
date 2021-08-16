if FORMAT:match 'latex' then
    function Div(el)
        if el.classes[1] == "Box" then
        -- insert element in front
        table.insert(
            el.content, 1,
            pandoc.RawBlock("latex", "\\begin{mybox}{" .. el.attributes.title .. "}"))
        -- insert element at the back
        table.insert(
            el.content,
            pandoc.RawBlock("latex", "\\end{mybox}"))
        end
        return el
    end
end
