import os
import re

CONTENT_DIR = "content"
CONFIG_FILE = "admin/config.yml"

def generate_config():
    if not os.path.exists(CONTENT_DIR):
        print(f"Error: {CONTENT_DIR} not found.")
        return

    config_yaml = """backend:
  name: github
  repo: abdulahad-92/Course-Manual-System
  branch: main

media_folder: "_static/images"
public_folder: "/Course-Manual-System/_static/images"

collections:
"""
    
    folders = sorted([f for f in os.listdir(CONTENT_DIR) if os.path.isdir(os.path.join(CONTENT_DIR, f)) and f != "images"])
    
    for folder in folders:
        # e.g., 01_Computational_Thinking -> "Module 1 - Computational Thinking" or "Course Overview"
        folder_clean = re.sub(r"^\d+_", "", folder).replace("_", " ").title()
        if folder.startswith("00"):
            label = "Course Overview"
            name = "course_overview"
        else:
            mod_num = int(folder.split("_")[0])
            label = f"Module {mod_num}: {folder_clean}"
            name = f"module_{mod_num}"
            
        config_yaml += f"""
  - name: "{name}"
    label: "{label}"
    folder: "content/{folder}"
    extension: "md"
    create: true
    fields:
      - {{label: "Title", name: "title", widget: "string"}}
      - {{label: "Kernelspec (Optional)", name: "kernelspec", widget: "object", required: false, fields: [{{label: "Name", name: "name", widget: "string", default: "python3", required: false}}, {{label: "Display Name", name: "display_name", widget: "string", default: "Python 3", required: false}}]}}
      - {{label: "Body", name: "body", widget: "markdown"}}
"""
    
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        f.write(config_yaml)
        
    print(f"Generated Sveltia CMS config with {len(folders)} collections.")

if __name__ == "__main__":
    generate_config()
