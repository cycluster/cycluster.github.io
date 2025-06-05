import os
import yaml

input_dir = "contributors"
output_file = "_includes/contributors.html"

# Ensure _includes exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

contributors = []

# Read and collect contributor data from .md or .qmd files, excluding index.qmd
for file in os.listdir(input_dir):
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
                    if data:
                        # Ensure required fields are present
                        if all(field in data for field in ["name", "affiliation", "email", "url"]):
                            print(f"Processing {file}: {data}")
                            contributors.append(data)
                        else:
                            print(f"Skipping {file} due to missing fields")
                    else:
                        print(f"Skipping {file} due to empty YAML")
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML in {file}: {e}")

# Sort contributors by last name
contributors.sort(key=lambda c: c.get("name", "").split()[-1].lower() if len(c.get("name", "").split()) > 1 else "")

# Generate HTML boxes
boxes = []
for data in contributors:
    print(f"Generating box for {data.get('name', '')}")

    email = data.get("email", "")
    url = data.get("url", "")

    email_icon = f'<a href="mailto:{email}" title="Email"><i class="bi bi-envelope-fill"></i></a>' if email else ""
    url_icon = f'<a href="{url}" title="Website" target="_blank"><i class="bi bi-globe2"></i></a>' if url else ""

    # Combine icons smartly
    icons = ""
    if email_icon and url_icon:
        icons = f"{email_icon} {url_icon}<br>"
    elif email_icon:
        icons = f"{email_icon}<br>"
    elif url_icon:
        icons = f"{url_icon}<br>"

    box = f"""
<div class="contrib-box">
  <strong>Name:</strong> {data.get("name", "")}<br>
  <strong>Affiliation:</strong> {data.get("affiliation", "")}<br>
  {icons}
</div>
"""
    boxes.append(box)

# Write all the boxes to the output HTML file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("<div class='contrib-row'>\n")
    f.write("\n".join(boxes))
    f.write("\n</div>")
