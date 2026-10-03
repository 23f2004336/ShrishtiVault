import json, os

notes = {}
if os.path.isdir("notes"):
    for subject in sorted(os.listdir("notes")):
        folder = os.path.join("notes", subject)
        if not os.path.isdir(folder):
            continue
        files = [f for f in sorted(os.listdir(folder)) if f.endswith((".html", ".pdf"))]
        name = subject.replace("-", " ")
        notes[name.upper() if len(name) <= 4 else name.title()] = [
            {"title": os.path.splitext(f)[0].replace("_", " ").replace("-", " "),
             "path": f"{folder}/{f}"}
            for f in files
        ]

with open("notes.json", "w") as f:
    json.dump(notes, f, indent=2)
