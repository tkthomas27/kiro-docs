#!/usr/bin/env python3
import urllib.request
import urllib.error
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString

# Base URLs
BASE_URL = "https://kiro.dev"
DOCS_ROOT = "https://kiro.dev/docs/"

# List of Kiro IDE documentation pages in logical reading order
PAGES = [
    ("", "Get Started"),
    ("getting-started/installation/", "Installation"),
    ("getting-started/first-project/", "First Project"),
    ("chat/", "Chat Interface"),
    ("steering/", "Steering & Guidance"),
    ("specs/", "Spec-Driven Development"),
    ("hooks/", "Agent Hooks"),
    ("mcp/", "Model Context Protocol (MCP)"),
    ("cli/", "Command Line Interface (CLI)"),
    ("web/", "Web Interface"),
    ("guides/learn-by-playing/", "Learn by Playing"),
    ("privacy-and-security/", "Privacy & Security"),
]

def fetch_page(path):
    url = DOCS_ROOT + path
    print(f"Fetching: {url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_table(table_elem):
    rows = table_elem.find_all('tr')
    md_rows = []
    has_header = False
    
    for row in rows:
        th_cells = row.find_all('th')
        td_cells = row.find_all('td')
        cells = th_cells if th_cells else td_cells
        if not cells:
            continue
            
        cell_texts = []
        for cell in cells:
            txt = get_children_markdown(cell).strip().replace('|', '\\|')
            cell_texts.append(txt)
            
        md_rows.append("| " + " | ".join(cell_texts) + " |")
        
        if th_cells:
            has_header = True
            sep_cells = ["---" for _ in cell_texts]
            md_rows.append("| " + " | ".join(sep_cells) + " |")
            
    if not has_header and len(md_rows) > 0:
        first_row_cells = rows[0].find_all(['td', 'th'])
        sep_cells = ["---" for _ in range(len(first_row_cells))]
        md_rows.insert(1, "| " + " | ".join(sep_cells) + " |")
        
    return "\n\n" + "\n".join(md_rows) + "\n\n"

def to_markdown(elem):
    if elem is None:
        return ""
    if isinstance(elem, NavigableString):
        return str(elem)
    
    name = elem.name
    classes = elem.get('class', [])
    if classes is None:
        classes = []
        
    # Skip code headers (e.g. language labels like "json" in block code containers)
    if name == 'div' and 'docsearch-exclude' in classes:
        pre = elem.find('pre')
        if pre:
            return to_markdown(pre)
            
    if name == 'p':
        return "\n\n" + get_children_markdown(elem) + "\n\n"
    elif name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        level = int(name[1])
        # Demote headings down by 1 level so they nest nicely under the main page title (# Title)
        m_level = "#" * (level + 1)
        text = get_children_markdown(elem).strip()
        # Clean double newlines from heading content
        text = re.sub(r'\s+', ' ', text)
        return f"\n\n{m_level} {text}\n\n"
    elif name in ['strong', 'b']:
        return f"**{get_children_markdown(elem)}**"
    elif name in ['em', 'i']:
        return f"*{get_children_markdown(elem)}*"
    elif name == 'code':
        # Check if inside a pre block
        is_block = False
        p = elem.parent
        while p:
            if p.name == 'pre':
                is_block = True
                break
            p = p.parent
        if is_block:
            return elem.get_text()
        else:
            return f"`{elem.get_text()}`"
    elif name == 'pre':
        code = elem.find('code')
        lang = ""
        if code and code.get('class'):
            for cls in code.get('class'):
                if cls.startswith('language-'):
                    lang = cls.split('-')[1]
                    break
        code_text = code.get_text() if code else elem.get_text()
        if not code_text.endswith('\n'):
            code_text += '\n'
        return f"\n\n```{lang}\n{code_text}```\n\n"
    elif name == 'ul':
        return "\n" + get_children_markdown(elem) + "\n"
    elif name == 'ol':
        return "\n" + get_children_markdown(elem) + "\n"
    elif name == 'li':
        parent_is_ol = (elem.parent and elem.parent.name == 'ol')
        prefix = "1. " if parent_is_ol else "- "
        item_text = get_children_markdown(elem).strip()
        item_text = item_text.replace('\n', '\n    ')
        return f"{prefix}{item_text}\n"
    elif name == 'a':
        text = get_children_markdown(elem).strip()
        if not text:
            return "" # Skip empty anchor links
        href = elem.get('href', '')
        if href.startswith('/'):
            href = f"{BASE_URL}{href}"
        return f"[{text}]({href})"
    elif name == 'img':
        alt = elem.get('alt', '')
        src = elem.get('src', '')
        if src.startswith('/'):
            src = f"{BASE_URL}{src}"
        return f"![{alt}]({src})"
    elif name == 'blockquote':
        text = get_children_markdown(elem).strip()
        quoted = "\n".join([f"> {line}" for line in text.split('\n')])
        return f"\n\n{quoted}\n\n"
    elif name == 'table':
        return parse_table(elem)
    elif name in ['thead', 'tbody', 'tr', 'td', 'th']:
        return ""
    elif name in ['div', 'section', 'article', 'span', 'html', 'body', 'main']:
        return get_children_markdown(elem)
    else:
        return get_children_markdown(elem)

def get_children_markdown(elem):
    parts = []
    for child in elem.children:
        parts.append(to_markdown(child))
    return "".join(parts)

def clean_markdown(md_text):
    # Collapse multiple consecutive newlines (3 or more) to exactly 2
    md_text = re.sub(r'\n{3,}', '\n\n', md_text)
    # Remove whitespace from the end of lines
    md_text = re.sub(r'[ \t]+\n', '\n', md_text)
    return md_text.strip()

def main():
    combined_markdown = []
    
    # Add main repository header
    combined_markdown.append("# Kiro IDE Comprehensive Documentation")
    combined_markdown.append(f"\n*Compiled on {datetime.now().strftime('%B %d, %Y')}*\n\n---\n")
    
    success_count = 0
    for path, title in PAGES:
        html = fetch_page(path)
        if not html:
            print(f"Skipping page due to error: {title} ({path})")
            continue
            
        soup = BeautifulSoup(html, 'html.parser')
        # Find the prose div containing the actual article. 
        # The Next.js page renders a small shell/placeholder with class 'prose' first,
        # then renders the full hydrated content block inside a second 'prose' div.
        prose_divs = soup.find_all(class_='prose')
        
        target_prose = None
        for div in prose_divs:
            if len(div.get_text()) > 150: # Find the real content container
                target_prose = div
                break
                
        if not target_prose and prose_divs:
            # Fallback to the first prose div if we couldn't find one with enough text
            target_prose = prose_divs[-1]
            
        if target_prose:
            # Format the page section
            page_md = f"# {title}\n\n"
            page_md += get_children_markdown(target_prose)
            page_md = clean_markdown(page_md)
            
            combined_markdown.append(page_md)
            combined_markdown.append("\n\n---\n\n")
            success_count += 1
            print(f"Successfully compiled: {title}")
        else:
            print(f"Could not find article prose for: {title}")

    if success_count > 0:
        # Join sections and clean up trailing separators
        full_document = "".join(combined_markdown).rstrip("\n- ") + "\n"
        
        # Save to kiro_docs.md
        with open("kiro_docs.md", "w") as f:
            f.write(full_document)
        print(f"\nSuccessfully compiled {success_count} sections into kiro_docs.md")
        
        # Write metadata.json
        metadata = {
            "last_updated": datetime.now().strftime("%B %d, %Y %I:%M %p"),
            "sections_count": success_count,
            "char_count": len(full_document),
            "word_count": len(full_document.split())
        }
        with open("metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)
        print("Updated metadata.json")
    else:
        print("Failed to scrape any documentation pages.")

if __name__ == "__main__":
    main()
