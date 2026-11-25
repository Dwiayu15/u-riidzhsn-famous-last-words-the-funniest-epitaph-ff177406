"""Famous Last Words: The Funniest Epitaph — one-line tombstone entry."""

EPITAPH = 'HERE LIES A MAN WHO ASKED, "WHAT\'S THE WORST THAT COULD HAPPEN?" — NOW HE KNOWS.'

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the epitaph is a valid single-line entry of 1-150 chars."""
    if not isinstance(text, str):
        raise ValueError("epitaph must be a string")
    if not text.strip():
        raise ValueError("epitaph must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("epitaph must be a single line")
    if len(text) > 150:
        raise ValueError(f"epitaph is {len(text)} chars, over the 150 limit")
    if len(text) < 1:
        raise ValueError("epitaph must be at least 1 char")
    return True


def self_test():
    validate(EPITAPH)
    print(f"epitaph: {EPITAPH}")
    print(f"characters: {len(EPITAPH)}")
    print("self_test: OK")


def main(output_path=OUTPUT_PATH):
    validate(EPITAPH)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(EPITAPH)
    self_test()


if __name__ == "__main__":
    import sys

    chosen = sys.argv[1] if len(sys.argv) > 1 else OUTPUT_PATH
    main(chosen)
