function initCMSWidgets() {
  if (typeof window.CMS === 'undefined') {
    setTimeout(initCMSWidgets, 100);
    return;
  }

  // 1. Table of Contents
  CMS.registerEditorComponent({
    id: "myst-toc",
    label: "Table of Contents",
    fields: [],
    pattern: /^```\{tableofcontents\}\r?\n```$/m,
    fromBlock: function(match) {
      return {};
    },
    toBlock: function(obj) {
      return "```{tableofcontents}\n```";
    },
    toPreview: function(obj) {
      var el = document.createElement('div');
      el.style.cssText = "padding:20px;background:#2d3748;border:1px solid #4a5568;text-align:center;border-radius:8px;color:#e2e8f0;font-family:sans-serif;margin:10px 0;";
      el.innerHTML = "<strong style='font-size:16px'>📚 Course Table of Contents</strong><br><em style='font-size:12px;color:#a0aec0'>(Generated automatically upon publish)</em>";
      return el;
    }
  });

  // 2. Python Code Cell — uses plain "text" widget to avoid Immutable.js issues
  CMS.registerEditorComponent({
    id: "myst-code-cell",
    label: "Python Code Cell",
    fields: [
      {
        name: "code",
        label: "Python Code (type your code here)",
        widget: "text"
      }
    ],
    pattern: /^```\{code-cell\} python3\r?\n([\s\S]*?)\r?\n```$/m,
    fromBlock: function(match) {
      return { code: match[1] };
    },
    toBlock: function(obj) {
      return "```{code-cell} python3\n" + (obj.code || "") + "\n```";
    },
    toPreview: function(obj) {
      var code = obj.code || "";
      var wrapper = document.createElement('div');
      wrapper.style.cssText = "padding:15px;background:#1e1e1e;color:#d4d4d4;border-radius:8px;border-left:4px solid #3776ab;margin:10px 0;";
      var label = document.createElement('div');
      label.style.cssText = "font-family:sans-serif;font-size:12px;font-weight:bold;margin-bottom:8px;color:#3776ab;letter-spacing:1px;";
      label.textContent = "PYTHON CODE CELL";
      var pre = document.createElement('pre');
      pre.style.cssText = "margin:0;font-family:monospace;white-space:pre-wrap;font-size:14px;";
      pre.textContent = code;
      wrapper.appendChild(label);
      wrapper.appendChild(pre);
      return wrapper;
    }
  });

  // 3. Alert / Admonition — uses "string" widget for content to stay simple
  CMS.registerEditorComponent({
    id: "myst-admonition",
    label: "Alert / Admonition",
    fields: [
      {
        name: "type",
        label: "Alert Type",
        widget: "select",
        options: ["note", "warning", "tip", "important"]
      },
      {
        name: "content",
        label: "Message",
        widget: "text"
      }
    ],
    pattern: /^:::\{(note|warning|tip|important)\}\r?\n([\s\S]*?)\r?\n:::$/m,
    fromBlock: function(match) {
      return { type: match[1], content: match[2] };
    },
    toBlock: function(obj) {
      return ":::{"+(obj.type || "note")+"}\n" + (obj.content || "") + "\n:::";
    },
    toPreview: function(obj) {
      var type = obj.type || "note";
      var colorMap = {
        note:      { color:"#31708f", bg:"#ebf8ff", border:"#90cdf4" },
        warning:   { color:"#975a16", bg:"#fffff0", border:"#f6e05e" },
        important: { color:"#9b2c2c", bg:"#fff5f5", border:"#fc8181" },
        tip:       { color:"#276749", bg:"#f0fff4", border:"#68d391" }
      };
      var c = colorMap[type] || colorMap.note;
      var wrapper = document.createElement('div');
      wrapper.style.cssText = "padding:15px;background:"+c.bg+";color:"+c.color+";border-left:4px solid "+c.border+";border-radius:4px;margin:10px 0;font-family:sans-serif;";
      var title = document.createElement('strong');
      title.style.cssText = "text-transform:uppercase;font-size:12px;letter-spacing:1px;";
      title.textContent = type;
      var body = document.createElement('div');
      body.style.cssText = "margin-top:6px;";
      body.textContent = obj.content || "";
      wrapper.appendChild(title);
      wrapper.appendChild(body);
      return wrapper;
    }
  });
}

initCMSWidgets();
