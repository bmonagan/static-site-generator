# Static Site Generator

A Python-based static site generator that converts markdown content into fully-rendered HTML pages.

## Features

- **Markdown to HTML Conversion**: Converts markdown files to HTML with full support for:
  - Headings (h1-h6)
  - Paragraphs
  - Bold and italic text
  - Links and images
  - Ordered and unordered lists
  - Code blocks
  - Block quotes

- **Template Support**: Uses HTML templates with `{{ Title }}` and `{{ Content }}` placeholders

- **Static Asset Management**: Automatically copies CSS, images, and other static files to the output directory

- **Nested Block Structure**: Properly handles complex nested markdown structures including lists with inline formatting

## Project Structure

```
├── src/                          # Source code
│   ├── main.py                   # Entry point
│   ├── page_generation.py        # Page generation logic
│   ├── MDblock_to_html.py        # Markdown block to HTML conversion
│   ├── block_type.py             # Block type detection
│   ├── block_type_to_html_tag.py # Block type to HTML tag mapping
│   ├── markdown_blocks.py        # Markdown block parsing
│   ├── text_to_textnodes.py      # Text to text node conversion
│   ├── text_to_children.py       # Text to child nodes conversion
│   ├── splitnodes.py             # Text node splitting
│   ├── textTransform.py          # Text node to HTML node conversion
│   ├── htmlnode.py               # Base HTML node class
│   ├── parentnode.py             # Parent node class (containers)
│   ├── leafnode.py               # Leaf node class (text/elements)
│   ├── textnode.py               # Text node class
│   ├── extract_title.py          # Extract page title from markdown
│   ├── extraction.py             # Text extraction utilities
│   └── file_management.py        # File handling utilities
├── content/                      # Markdown source files
│   └── index.md                  # Main content
├── template.html                 # HTML template
├── static/                       # Static assets (CSS, images)
│   ├── index.css
│   └── images/
├── public/                       # Generated HTML output (auto-created)
├── testing/                      # Test suite
└── main.sh                       # Build script
```

## Installation

### Requirements
- Python 3.7+

### Setup

1. Clone or download the project
2. Ensure Python 3 is installed on your system

## Usage

### Running the Generator

Execute the main build script:

```bash
./main.sh
```

Or run directly with Python:

```bash
python3 src/main.py
```

This will:
1. Clear the `public/` directory
2. Copy static assets from `static/` to `public/`
3. Convert markdown from `content/index.md` to HTML
4. Apply the template from `template.html`
5. Output the final HTML to `public/index.html`

### Creating Content

1. **Edit `content/index.md`**: Write your markdown content
2. **Update `template.html`**: Customize your HTML template with `{{ Title }}` and `{{ Content }}` placeholders
3. **Add assets**: Place CSS and images in `static/` directory
4. **Run generator**: Execute `./main.sh` to build

### Markdown Syntax

The generator supports standard markdown:

```markdown
# Heading 1
## Heading 2
### Heading 3
...
###### Heading 6

This is a paragraph.

**Bold text** and *italic text*

- Unordered list item
- Another item

1. Ordered list item
2. Another item

> This is a block quote
> Multiple lines supported

![Alt text](/path/to/image.png)

[Link text](https://example.com)

`inline code`

\`\`\`
code block
with multiple lines
\`\`\`
```

### Template

The `template.html` file uses two placeholders:

- `{{ Title }}` - Replaced with the h1 heading from your markdown
- `{{ Content }}` - Replaced with the generated HTML content

Example:

```html
<!doctype html>
<html>
  <head>
    <title>{{ Title }}</title>
  </head>
  <body>
    <article>{{ Content }}</article>
  </body>
</html>
```

## How It Works

### Pipeline

1. **Markdown Parsing**: Splits markdown into blocks (paragraphs, headings, lists, etc.)
2. **Block Type Detection**: Identifies each block's type
3. **Block Conversion**: Converts each block to HTML elements
4. **Inline Processing**: Handles text formatting within blocks (bold, italic, links, images)
5. **HTML Tree Building**: Creates a tree of HTML nodes (parent nodes contain children)
6. **Rendering**: Converts the HTML tree to string output
7. **Template Application**: Applies template and writes final HTML file

### Class Hierarchy

- **HTMLNode**: Base class for all HTML elements
  - **ParentNode**: Container elements (div, ul, blockquote, etc.)
  - **LeafNode**: Text or self-closing elements (p, img, a, etc.)

- **TextNode**: Represents inline text with formatting (bold, italic, link, image, code)

## Testing

Run the test suite:

```bash
python3 -m pytest testing/
```

Individual test files are available in the `testing/` directory.

## Output

The generator creates an optimized HTML file in `public/index.html` with:
- Valid HTML5 structure
- Proper semantic elements
- Self-closing tags for images
- Attribute escaping for special characters
- Proper nesting of elements

## Example Output

Input markdown with a quote:

```markdown
> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
```

Generates:

```html
<blockquote>"I am in fact a Hobbit in all but size." -- J.R.R. Tolkien</blockquote>
```

## License

This is a project from [Boot.dev](https://www.boot.dev) Python course.
