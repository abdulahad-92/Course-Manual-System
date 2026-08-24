import os
import yaml

CONTENT_DIR = "content"
MYST_YML = "myst.yml"

def generate_myst_config():
    if not os.path.exists(CONTENT_DIR):
        print(f"Error: {CONTENT_DIR} directory not found.")
        return

    # Basic structure for myst.yml
    config = {
        "version": 1,
        "project": {
            "title": "MIS 103: Introduction to Computer Applications",
            "authors": [{"name": "Engr Dr Syed Irfan Nabi"}],
            "jupyter": True,
            "thebe": True,
            "thebe_config": {
                "kernel_name": "python3"
            },
            "static_files": ["admin"],
            "toc": []
        },
        "site": {
            "template": "book-theme",
            "head": [
                {
                    "tag": "script",
                    "attributes": {
                        "type": "text/x-thebe-config"
                    },
                    "value": '{"useBinder": false, "useJupyterLite": true}'
                }
            ],
            "options": {
                "launch_buttons": {
                    "thebe": True
                },
                "actions": [
                    {
                        "title": "Open in Google Colab",
                        "url": "https://colab.research.google.com"
                    }
                ]
            }
        }
    }

    folders = sorted([f for f in os.listdir(CONTENT_DIR) if os.path.isdir(os.path.join(CONTENT_DIR, f))])
    
    toc = []
    
    for index, folder in enumerate(folders):
        folder_path = os.path.join(CONTENT_DIR, folder)
        md_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
        
        if not md_files:
            continue
            
        main_file = md_files[0]
        chapter_title = folder.replace("_", " ")
        parts = chapter_title.split(" ")
        if parts[0].isdigit():
            chapter_title = " ".join(parts[1:])
            
        if index == 0:
            # MyST requires the first TOC item (home page) to have no children
            toc.append({
                "title": chapter_title,
                "file": f"{CONTENT_DIR}/{folder}/{main_file}"
            })
            if len(md_files) > 1:
                toc.append({
                    "title": "Syllabus & Pedagogy",
                    "children": [{"file": f"{CONTENT_DIR}/{folder}/{child}"} for child in md_files[1:]]
                })
        else:
            chapter_entry = {
                "title": chapter_title,
                "file": f"{CONTENT_DIR}/{folder}/{main_file}"
            }
            if len(md_files) > 1:
                chapter_entry["children"] = [{"file": f"{CONTENT_DIR}/{folder}/{child}"} for child in md_files[1:]]
            toc.append(chapter_entry)

    config["project"]["toc"] = toc
    
    with open(MYST_YML, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, sort_keys=False, default_flow_style=False, allow_unicode=True)
        
    print("SUCCESS: myst.yml has been updated successfully based on the content folder.")

if __name__ == "__main__":
    generate_myst_config()
