import os
import yaml

input_dir = "contributors"
output_file = "_includes/contributors.html"

# Ensure _includes exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

contributors = []

# Read and collect contributor data from .md files, excluding index.qmd
for file in os.listdir(input_dir):
    # Skip index.qmd and ensure only .md files are processed
    if (file.endswith(".md") or file.endswith(".qmd")) and file != "index.qmd":
        with open(os.path.join(input_dir, file), "r", encoding="utf-8") as f:
            content = f.read().strip()
            
            # Skip empty files
            if not content:
                continue
            
            parts = content.split("---")
            if len(parts) >= 3:
                try:
                    data = yaml.safe_load(parts[1])  # Extract YAML front matter
                    if data:  # Skip empty data
                        # Ensure all required fields are present (excluding contribution)
                        if all(field in data for field in ["name", "affiliation", "email", "url"]):
                            print(f"Processing {file}: {data}")  # Debug: print loaded data
                            contributors.append(data)
                        else:
                            print(f"Skipping {file} due to missing fields")  # Debug: print skipped files
                    else:
                        print(f"Skipping {file} due to empty YAML")  # Debug: print skipped files
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML in {file}: {e}")

# Sort contributors by last name (safely)
contributors.sort(key=lambda c: c.get("name", "").split()[-1].lower() if len(c.get("name", "").split()) > 1 else "")

# Generate HTML boxes
boxes = []
for data in contributors:
    print(f"Generating box for {data.get('name', '')}")  # Debug: print name being used
    
    # Check if email and URL are present and not empty
    email_icon = f'<a href="mailto:{data.get("email", "")}" title="Email"><i class="bi bi-envelope-fill"></i></a>' if data.get("email") not in [None, ""] else ""
    url_icon = f'<a href="{data.get("url", "")}" title="Website" target="_blank"><i class="bi bi-globe2"></i></a>' if data.get("url") not in [None, ""] else ""
    
    box = f"""
<div class="contrib-box">
  <strong>Name:</strong> {data.get("name", "")}<br>
  <strong>Affiliation:</strong> {data.get("affiliation", "")}<br>
  {email_icon}
  {url_icon}<br>
</div>
"""
    boxes.append(box)

# Write all the boxes to the HTML file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("<div class='contrib-row'>\n")
    f.write("\n".join(boxes))  # Insert all the contributor boxes
    f.write("\n</div>")
