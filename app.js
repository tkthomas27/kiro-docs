document.addEventListener('DOMContentLoaded', () => {
  let markdownContent = '';
  let tocLinks = [];
  let headings = [];

  const docsContent = document.getElementById('docs-content');
  const navToc = document.getElementById('nav-toc');
  const inputSearch = document.getElementById('input-search');
  const btnDownload = document.getElementById('btn-download');
  const statWords = document.getElementById('stat-words');
  const statUpdated = document.getElementById('stat-updated');

  // 1. Fetch Metadata and Stats
  fetch('metadata.json')
    .then(res => {
      if (!res.ok) throw new Error('Metadata not found');
      return res.json();
    })
    .then(meta => {
      if (statUpdated) {
        statUpdated.textContent = meta.last_updated || 'Unknown';
      }
      if (statWords) {
        // Format with commas
        const formattedWords = (meta.word_count || 0).toLocaleString();
        statWords.textContent = `${formattedWords} words`;
      }
    })
    .catch(err => {
      console.warn('Metadata load error:', err);
      if (statUpdated) statUpdated.textContent = 'Offline Mode';
    });

  // 2. Fetch and Render Markdown Document
  fetch('kiro_docs.md')
    .then(res => {
      if (!res.ok) throw new Error('Failed to load kiro_docs.md');
      return res.text();
    })
    .then(text => {
      markdownContent = text;
      renderMarkdown(text);
      buildTOC();
      setupCopyButtons();
      setupScrollSpy();
    })
    .catch(err => {
      console.error('Error loading documentation:', err);
      docsContent.innerHTML = `
        <div class="alert warning">
          <strong>Error Loading Documentation:</strong> ${err.message}. 
          Please make sure you have run the scraper script to compile the documentation file.
        </div>
      `;
    });

  // Render markdown to HTML
  function renderMarkdown(md) {
    // Configure marked options
    marked.setOptions({
      gfm: true,
      breaks: true,
      headerIds: false, // We'll manage heading IDs ourselves for complete control
      mangle: false
    });

    // Parse and sanitize markdown
    const rawHTML = marked.parse(md);
    const cleanHTML = DOMPurify.sanitize(rawHTML);
    docsContent.innerHTML = cleanHTML;
  }

  // Build the Table of Contents dynamically
  function buildTOC() {
    navToc.innerHTML = ''; // Clear skeleton loader
    
    // Select page titles (h1) and section titles (h3)
    headings = Array.from(docsContent.querySelectorAll('h1, h3'));
    
    headings.forEach((heading, idx) => {
      const text = heading.textContent.trim();
      
      // Generate a clean URL-friendly ID for the heading anchor
      const cleanId = text
        .toLowerCase()
        .replace(/[^\w\s-]/g, '') // remove special characters
        .replace(/\s+/g, '-')     // replace spaces with hyphens
        .replace(/-+/g, '-')      // remove duplicate hyphens
        + `-${idx}`;              // add index to ensure uniqueness
      
      heading.id = cleanId;

      const link = document.createElement('a');
      link.href = `#${cleanId}`;
      link.textContent = text;
      
      if (heading.tagName.toLowerCase() === 'h1') {
        link.className = 'toc-h1 font-semibold';
      } else {
        link.className = 'toc-h3 text-prey-400 pl-4 border-l border-white/5';
      }

      // Smooth scroll navigation
      link.addEventListener('click', (e) => {
        e.preventDefault();
        heading.scrollIntoView({ behavior: 'smooth' });
        // Set URL hash without jump
        history.pushState(null, null, `#${cleanId}`);
        setActiveLink(link);
      });

      navToc.appendChild(link);
      tocLinks.push({ link, heading, type: heading.tagName.toLowerCase() });
    });
  }

  function setActiveLink(activeLink) {
    tocLinks.forEach(({ link }) => {
      link.classList.remove('active');
    });
    activeLink.classList.add('active');
    
    // Scroll active link into view in the sidebar if needed
    const linkRect = activeLink.getBoundingClientRect();
    const sidebarRect = navToc.parentElement.getBoundingClientRect();
    if (linkRect.top < sidebarRect.top || linkRect.bottom > sidebarRect.bottom) {
      activeLink.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    }
  }

  // Setup Scroll Spy to track active header during reading
  function setupScrollSpy() {
    let ticking = false;

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          spyScroll();
          ticking = false;
        });
        ticking = true;
      }
    });
  }

  function spyScroll() {
    const scrollPos = window.scrollY || document.documentElement.scrollTop;
    
    // Find the heading that is closest to the top of the viewport
    let activeHeading = null;
    
    // If we're at the very top of the page, highlight the first link
    if (scrollPos < 100 && headings.length > 0) {
      const firstLink = tocLinks[0]?.link;
      if (firstLink) setActiveLink(firstLink);
      return;
    }

    for (let i = 0; i < headings.length; i++) {
      const heading = headings[i];
      const offsetTop = heading.offsetTop;
      
      // Highlight the heading if the scroll position has passed it (with an offset for sticky header)
      if (scrollPos >= offsetTop - 130) {
        activeHeading = heading;
      } else {
        break; // Headings are sorted by offsetTop, so we can stop searching
      }
    }

    if (activeHeading) {
      const match = tocLinks.find(item => item.heading === activeHeading);
      if (match) {
        setActiveLink(match.link);
      }
    }
  }

  // 3. Search functionality
  inputSearch.addEventListener('input', () => {
    const query = inputSearch.value.toLowerCase().trim();
    
    tocLinks.forEach(({ link, heading }) => {
      const linkText = link.textContent.toLowerCase();
      const headingText = heading.textContent.toLowerCase();
      
      if (linkText.includes(query) || headingText.includes(query)) {
        link.style.display = 'flex';
        // Highlight in content (soft highlight)
        heading.style.opacity = '1';
      } else {
        link.style.display = 'none';
        heading.style.opacity = '0.4';
      }
    });

    if (query === '') {
      tocLinks.forEach(({ heading }) => {
        heading.style.opacity = '1';
      });
    }
  });

  // 4. Download Markdown Action
  btnDownload.addEventListener('click', () => {
    if (!markdownContent) {
      alert('Documentation content is not loaded yet.');
      return;
    }
    
    const blob = new Blob([markdownContent], { type: 'text/markdown;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    
    link.href = url;
    link.download = 'kiro_docs.md';
    link.style.visibility = 'hidden';
    
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  });

  // 5. Code Copy Buttons Setup
  function setupCopyButtons() {
    const preBlocks = docsContent.querySelectorAll('pre');
    
    preBlocks.forEach(pre => {
      // Ensure the pre block is positioned relative for absolute button placement
      pre.style.position = 'relative';
      
      const copyBtn = document.createElement('button');
      copyBtn.className = 'copy-code-btn';
      copyBtn.textContent = 'Copy';
      
      copyBtn.addEventListener('click', () => {
        const codeElement = pre.querySelector('code');
        const textToCopy = codeElement ? codeElement.innerText : pre.innerText;
        
        navigator.clipboard.writeText(textToCopy).then(() => {
          copyBtn.textContent = 'Copied!';
          copyBtn.classList.add('success');
          
          setTimeout(() => {
            copyBtn.textContent = 'Copy';
            copyBtn.classList.remove('success');
          }, 2000);
        }).catch(err => {
          console.error('Failed to copy text:', err);
          copyBtn.textContent = 'Error';
        });
      });
      
      pre.appendChild(copyBtn);
    });
  }
});
