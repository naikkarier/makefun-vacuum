import os

LINE = "I did not miss that spot. My sensors logged it as a permanent resident, and I respect its tenancy."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1 to 200 characters, got %d" % len(text)
    assert "\n" not in text, "line must be a single line"
    assert "\r" not in text, "line must not contain a carriage return"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
