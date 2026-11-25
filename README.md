# One-Liner Marathon

[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![make.fun · rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/m1651/makefun-one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![make.fun · reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/m1651/makefun-one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)

An entry for the [One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2) bounty on make.fun: a single original one-line comedy joke, up to 280 characters, judged head to head against other entries.

## The joke

> My houseplant died of neglect, so I replaced it with a cactus and named it Exhibit A.

The joke is a confession disguised as a gardening decision: the narrator killed a plant, learned nothing, and bought a tougher one — then named it like a piece of courtroom evidence, as if the cactus itself is testifying against its owner. The turn lands on "Exhibit A", which reframes the whole line as a crime scene.

## How to run

```sh
python3 main.py
```

This writes the joke to `/output/entry.txt` (creating `/output` if needed). Set `MAKEFUN_OUTPUT_DIR` to write it somewhere else instead. The program is deterministic — no network, no randomness, no input — and enforces the 1–280 character gate and the single-line rule before writing.

## License

MIT — see [LICENSE](LICENSE).
