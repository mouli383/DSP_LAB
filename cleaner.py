%%writefile cleaner.py
import re

def remove_chat_metadata(chat_export_file):
    pattern = r"\d+\/\d+\/\d+,\s\d+:\d+\s-\s(?:[\w\s]+:\s)?"

    with open(chat_export_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    cleaned = re.sub(pattern, "", content)

    lines = []
    for line in cleaned.split("\n"):
        line = line.strip()
        if not line:
            continue
        if "end-to-end encrypted" in line.lower():
            continue
        lines.append(line)

    return tuple(lines)


def remove_non_message_text(export_text_lines):
    filter_out_msgs = ("<Media omitted>",)
    return tuple(
        msg for msg in export_text_lines
        if msg not in filter_out_msgs
    )


def clean_corpus(chat_export_file):
    messages = remove_chat_metadata(chat_export_file)
    return remove_non_message_text(messages)
