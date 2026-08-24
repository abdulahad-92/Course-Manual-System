// Register Custom Editor Components for MyST Markdown

// 1. Table of Contents
CMS.registerEditorComponent({
  id: "myst-toc",
  label: "Table of Contents",
  fields: [],
  pattern: /^{tableofcontents}$/m,
  fromBlock: function(match) {
    return {};
  },
  toBlock: function(obj) {
    return "{tableofcontents}";
  },
  toPreview: function(obj) {
    return '<div style="padding: 20px; background: #2d3748; border: 1px solid #4a5568; text-align: center; border-radius: 8px; color: #e2e8f0; font-family: sans-serif; margin: 10px 0;">' +
           '<strong style="font-size: 16px;">📚 Course Table of Contents</strong><br>' +
           '<em style="font-size: 12px; color: #a0aec0;">(Generated automatically upon publish)</em>' +
           '</div>';
  }
});

// 2. Python Code Cell
CMS.registerEditorComponent({
  id: "myst-code-cell",
  label: "Python Code Cell",
  fields: [
    {
      name: "code",
      label: "Python Code",
      widget: "code",
      default_language: "python"
    }
  ],
  pattern: /^```{code-cell} python3\n([\s\S]*?)\n```$/m,
  fromBlock: function(match) {
    return {
      code: match[1]
    };
  },
  toBlock: function(obj) {
    return "```{code-cell} python3\n" + (obj.code || "") + "\n```";
  },
  toPreview: function(obj) {
    return '<div style="padding: 15px; background: #1e1e1e; color: #d4d4d4; border-radius: 8px; border-left: 4px solid #3776ab; margin: 10px 0;">' +
           '<div style="font-family: sans-serif; font-size: 12px; font-weight: bold; margin-bottom: 8px; color: #3776ab;">PYTHON CODE CELL</div>' +
           '<pre style="margin: 0; font-family: monospace; white-space: pre-wrap; font-size: 14px;">' + (obj.code || "") + '</pre>' +
           '</div>';
  }
});

// 3. Alert / Admonition
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
      label: "Message Content",
      widget: "markdown"
    }
  ],
  pattern: /^:::{(note|warning|tip|important)}\n([\s\S]*?)\n:::$/m,
  fromBlock: function(match) {
    return {
      type: match[1],
      content: match[2]
    };
  },
  toBlock: function(obj) {
    return ":::{"+(obj.type || "note")+"}\n" + (obj.content || "") + "\n:::";
  },
  toPreview: function(obj) {
    let type = obj.type || "note";
    let color = "#31708f";
    let bg = "#ebf8ff";
    let border = "#90cdf4";
    
    if (type === "warning") { 
        color = "#975a16"; bg = "#fffff0"; border = "#f6e05e";
    } else if (type === "important") { 
        color = "#9b2c2c"; bg = "#fff5f5"; border = "#fc8181";
    } else if (type === "tip") { 
        color = "#276749"; bg = "#f0fff4"; border = "#68d391";
    }
    
    return '<div style="padding: 15px; background: '+bg+'; color: '+color+'; border-left: 4px solid '+border+'; border-radius: 4px; margin: 10px 0; font-family: sans-serif;">' +
           '<strong style="text-transform: uppercase; font-size: 12px;">'+type+'</strong><br>' +
           '<div style="margin-top: 5px;">' + (obj.content || "") + '</div>' +
           '</div>';
  }
});
