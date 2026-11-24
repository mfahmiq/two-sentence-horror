[![make.fun](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/mfahmiq/two-sentence-horror/rank.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/mfahmiq/two-sentence-horror/reward.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)

# Two-Sentence Horror

A two-sentence horror story for the [make.fun](https://make.fun/c/u-suroto-two-sentence-horror-acea9253) bounty **u-suroto-two-sentence-horror-acea9253** — the scariest story possible in exactly two sentences, no more than 400 characters.

## The story

> The estate agent laughed when I asked whether the previous owner still living here was just a figure of speech, and knocked a third off the price. Last night I heard my own voice downstairs, telling the new tenants the house is cheap because the previous owner still lives here.

## Why it scares

The first sentence reads like a joke shared between buyer and seller: a haunted-house cliché, defused by a laugh and a discount. The reader relaxes — the narrator got a bargain, the ghost is just a sales line.

The second sentence takes that comfort away. The narrator is no longer the buyer upstairs; he is the voice downstairs, repeating the agent's pitch to the next tenants. Nothing is explained — no death, no ghost, no violence — but the implication lands on its own: the narrator is now the previous owner, and the house has already claimed him. The bargain was never a bargain. The cycle that trapped the last owner has trapped him too, and it will trap the people listening to his voice now.

That is the turn the story is built on: sentence two does not add a new scare, it reframes sentence one. The laugh, the discount, the "figure of speech" — all of it was the trap closing, and the narrator only understands it once he is on the other side of it, doing the selling himself.

The horror is entirely implied. There is no gore, no monster described, no jump scare — just a man hearing his own voice from downstairs, and the reader filling in the worst of what that means.

## How it works

`main.py` (Python 3, standard library only) holds the story as a single string constant and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing, it self-verifies the competition gate:

- the text is valid UTF-8,
- it is 1–400 characters long (278 characters),
- it is not whitespace-only,
- it contains exactly two sentences.

If any check fails, the program exits non-zero and writes nothing.

## Usage

```sh
python3 main.py
# OK: wrote /output/entry.txt (278 chars, 2 sentences)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Files

- `main.py` — the entry program (writes and self-verifies `entry.txt`)
- `entry.txt` — the exact submitted story
- `README.md` — this file
- `LICENSE` — MIT License

