import os
import re

CONTENT_DIR = "content"

def format_title(filename, folder):
    # e.g., 01_lecture_notes.md -> Lecture Notes
    name = filename.replace(".md", "")
    name = re.sub(r"^\d+_", "", name) # remove leading numbers like 01_
    name = name.replace("_", " ").title()
    
    folder_name = re.sub(r"^\d+_", "", folder)
    folder_name = folder_name.replace("_", " ").title()
    
    return f"{folder_name} - {name}"

def add_titles():
    count = 0
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                folder = os.path.basename(root)
                
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                
                title = format_title(file, folder)
                
                if content.startswith("---\n"):
                    # Has frontmatter
                    # Check if title exists
                    end_idx = content.find("\n---\n", 4)
                    if end_idx != -1:
                        frontmatter = content[4:end_idx]
                        if "title:" not in frontmatter:
                            new_frontmatter = f"title: \"{title}\"\n{frontmatter}"
                            new_content = f"---\n{new_frontmatter}\n---\n{content[end_idx+5:]}"
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(new_content)
                            count += 1
                else:
                    # No frontmatter
                    new_content = f"---\ntitle: \"{title}\"\n---\n{content}"
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    count += 1
    
    print(f"Added title frontmatter to {count} files.")

if __name__ == "__main__":
    add_titles()
