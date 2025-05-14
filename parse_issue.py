import yaml

with open('notebook_gallery.yaml') as f:
    gallery = yaml.safe_load(f)

with open('issue_body.txt') as f:
    body = f.read()

print("Full Issue Body:")
print(body)

fields = {
    "Repository URL": "",
    "Cookbook Title": "",
    "Short Description": "",
    "Thumbnail Image URL": "",
    "Root Path Name": ""
}

lines = body.splitlines()

current_label = None
for line in lines:
    line = line.strip().lstrip("#").strip()  
    if line in fields:
        current_label = line
    elif current_label and line:
        fields[current_label] = line
        current_label = None

repo_url = fields["Repository URL"]
title = fields["Cookbook Title"]
description = fields["Short Description"]
thumbnail = fields["Thumbnail Image URL"]
root_path = fields["Root Path Name"]

print(f"Repo URL: {repo_url}")
print(f"Title: {title}")
print(f"Description: {description}")
print(f"Thumbnail: {thumbnail}")
print(f"Root Path: {root_path}")

if not root_path:
    raise ValueError("Root Path konnte nicht extrahiert werden – Abbruch.")

gallery['domains'][root_path] = {
    'title': title,
    'branch': 'main',
    'root_path': root_path,
    'description': description,
    'thumbnail': thumbnail,
    'url': f"https://katharinastarzer21.github.io/dest/{root_path}/index.html"
}

with open('notebook_gallery.yaml', 'w') as f:
    yaml.dump(gallery, f, sort_keys=False)

import os
with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    env_file.write(f"REPO_URL={repo_url}\n")
    env_file.write(f"ROOT_PATH={root_path}\n")
