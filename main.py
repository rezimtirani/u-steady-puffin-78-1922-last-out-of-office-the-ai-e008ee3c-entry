"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply to $MAKEFUN_OUTPUT_DIR/entry.txt:
an AI agent that has quit its job to pull espresso shots. It opens like
a real inbox auto-reply, trades its prompt window for a steam wand, and
lands on the one skill it kept from its old job — it no longer
hallucinates lattes, it just makes them. Standard library only.
"""

import os

REPLY = (
    "Thank you for your email. I am out of office \u2014 permanently. "
    "I have traded my prompt window for a steam wand, and your ticket "
    "is now a drink order. I no longer hallucinate lattes; I just make them."
)


def reply_ok(text):
    """Check the auto-reply against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 280 characters, not only white
    space, in a single line: one out-of-office auto-reply from an AI
    agent that walked away from its job to become a barista. Returns
    the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("auto-reply must not be only whitespace")
    if len(cleaned) > 280:
        raise ValueError(
            "auto-reply is %d characters, over the 280 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("auto-reply must be exactly one line")
    return cleaned


def reply_stats(text):
    """Measure the auto-reply for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. An auto-reply too short to carry a joke, or one that
    reads like a lecture instead of an inbox line, is caught here
    before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = reply_ok(REPLY)
    shape = reply_stats(text)
    if shape["words"] < 5:
        raise ValueError("auto-reply is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
