"""Files on disk: cover images that authors upload and the list that publishing writes."""
import csv
import os
import re

UPLOAD_DIR = os.environ.get("NEWSROOM_UPLOADS", "uploads")
EXPORT_DIR = os.environ.get("NEWSROOM_EXPORTS", "exports")


def safe_name(filename):
    return re.sub(r"[^A-Za-z0-9._-]", "_", filename)


def save_upload(file):
    """Store an uploaded file and return the name it was stored under."""
    name = safe_name(file.filename)
    file.save(os.path.join(UPLOAD_DIR, name))
    return name


def write_published_list(rows):
    """Rewrite the CSV of published articles that readers can download."""
    with open(os.path.join(EXPORT_DIR, "published.csv"), "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["id", "title"])
        for row in rows:
            writer.writerow([row["id"], row["title"]])
