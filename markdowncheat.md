<!--- Invisible comment -->
<!--- Useful info: https://daringfireball.net/projects/markdown/syntax -->
# Heading level 1

This is paragraph.

For line break inside the paragragh, use  
multiple spaces at the end of line.

### Citation
> This the citation.
It works for the whole block.

### Code
```bash
echo "This is the code block!"
```

This is the inline code: `echo "Inline code!"`

## Heading level 2

## Lists
* bullet list begins with stars
- or with dashes
- another item with following blockkquote

    > Indented blockquote - must be indented by 4 spaces and in separate paragraph

- another item with following code block

        ```bash
        echo "Indented code block - must be indented by 8 spaces and in separate paragraph"

- last item

## Links and internal links

This is [common link](http://test.com).

This is [internal link = anchor](anch)

### Link made from name</a>

### <a name="anch">Heading level 3 with anchor</a>

## Images
Inline-style: 
![alt text](/path/to/image.jpg "Logo Title Text 1")

Reference-style: 
![alt text][logo]
...
[logo]: /path/to/image.jpg "Logo Title Text 2"
<img title="Perfect Picture" src="/path/to/image.jpg" align="right" width="650px">

## Tables

### Full syntax
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

### Simplified syntax
Syntax | Description
-- | --
Header | Title
Paragraph | Text