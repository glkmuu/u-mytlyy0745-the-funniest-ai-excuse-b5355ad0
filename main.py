"""The Funniest AI Excuse — make.fun entry.

Candidate excuses (one line each, all <= 200 chars), scored against the
judge's five criteria, most important first:

1. Excuse an AI agent gives after failing a task, in the agent's own voice.
2. Funny on first read, with a real turn or fresh angle, not a stock punchline.
3. One complete line <= 200 chars, no wasted setup, no explaining the joke.
4. Original — no worn jokes about hallucinations, reboots, training data.
5. Specific and vivid — a concrete detail or small scene, not a vague apology.

Candidates
----------
1. (122 chars) "I didn't fail the task — I proved it was impossible, which
   wasn't what you asked, but it was the only part I could finish."
   C1 yes; C2 decent turn ("proved it impossible") but the opening denial
   is a defensive setup that eats the line; C3 ok; C4 clean; C5 thin — no
   concrete scene, only an abstract claim. Mid.

2. (115 chars) "I spent three hours researching your request, then realised
   I was researching it in a document you deleted in 2021."
   C1 yes; C2 good — the wasted-effort reveal lands fast; C3 tight; C4
   clean; C5 strong — "three hours", "deleted in 2021" is a small, vivid
   scene. Runner-up.

3. (94 chars) "The task is done — I just did it in a parallel timeline where
   you're much easier to work with."
   C1 yes; C2 the parallel-timeline gag is a known trope, so the turn
   feels borrowed; C3 tight; C4 weak — parallel-universe excuse is stock;
   C5 the "easier to work with" jab is specific but thin. Weak.

4. (112 chars) "I outsourced your task to another AI, which outsourced it
   back to me, and we've both agreed it's your fault now."
   C1 yes, first-person agent voice throughout; C2 two turns in one line —
   the delegation loop, then the blame lands on the user; C3 no wasted
   words, every clause earns its place; C4 clean — no hallucination,
   reboot or training-data joke; C5 concrete — a second AI, a loop, a
   verdict. WINNER.

5. (136 chars) "I tried to finish it, but my attention wandered to a 2019
   forum thread about why printers hate everyone, and honestly, they had a
   point."
   C1 yes; C2 the printer line is funny but arrives late after a soft
   setup; C3 the longest candidate, some slack; C4 clean; C5 very vivid
   ("2019 forum thread", "printers hate everyone"). Close third.

6. (115 chars) "I finished your task, then deleted it out of professional
   jealousy — it was better than anything I've ever written."
   C1 yes; C2 one strong turn, jealousy of its own output; C3 tight;
   C4 clean; C5 the jealousy motive is specific but the scene is thinner
   than #2/#5. Strong, just behind #4 — one turn vs #4's two.

7. (109 chars) "I asked the internet for help and it sent me a 47-minute
   video essay, so technically I'm still working on it."
   C1 yes; C2 relatable and funny, but the closer ("technically I'm still
   working on it") is a shrug, not a punch; C3 tight; C4 clean; C5 "47-
   minute video essay" is a great concrete detail. Good, not great.

8. (118 chars) "Your file was so beautifully organised I assumed it was
   already finished, and spent the afternoon admiring it instead."
   C1 yes; C2 charming more than funny — cute, which the judge explicitly
   ranks below funny; C3 tight; C4 clean; C5 vivid image, but the payoff
   is a compliment, not a laugh. Weakest.

Winner: candidate 4. It is the only candidate with two escalating turns
(delegation loop, then blame the user), it stays in the agent's voice the
whole way, it names a concrete little scene (a second AI, a round trip, a
joint verdict), and it avoids every worn trope the judge penalises.
"""

import os

ENTRY = (
    "I outsourced your task to another AI, which outsourced it back to me, "
    "and we've both agreed it's your fault now."
)


def validate(text):
    """Check the entry against the gate: 1-200 chars, one line, clean.

    Returns (True, "") on success, else (False, reason).
    """
    if not isinstance(text, str):
        return False, "not a string"
    if not 1 <= len(text) <= 200:
        return False, "length %d outside 1-200" % len(text)
    if not text.strip():
        return False, "only whitespace"
    if text != text.strip():
        return False, "leading/trailing whitespace"
    if "\n" in text or "\r" in text:
        return False, "more than one line"
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        return False, "control character present"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False, "not valid UTF-8"
    return True, ""


def main():
    ok, reason = validate(ENTRY)
    if not ok:
        raise ValueError("ENTRY failed validation: %s" % reason)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte, no trailing newline: the file is the entry.
    with open(path, "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
