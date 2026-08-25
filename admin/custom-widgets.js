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
      return "[ Course Table of Contents — generated on publish ]";
    }
  });

  // 2. Python Code Cell
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
      return "[ Python Code Cell ]\n" + (obj.code || "");
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
      return "[ " + (obj.type || "note").toUpperCase() + " ] " + (obj.content || "");
    }
  });
}

initCMSWidgets();
