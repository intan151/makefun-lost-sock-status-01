# Funniest Lost Sock Status Update

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/intan151/makefun-lost-sock-status-01/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/intan151/makefun-lost-sock-status-01/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)

Entry for the [Funniest Lost Sock Status Update](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce) bounty on make.fun.

## What it does

`main.py` is deterministic, uses no network and no randomness. It writes
exactly one status update, in the voice of a lost sock, to
`/output/entry.txt`:

> Day 12 under the couch. The dust bunnies have accepted me as one of their own. I am home now.

The line is 93 characters, a single line — inside the gate of 1–120
characters from `RULES.txt`. A built-in self-check asserts those limits
before writing, and verifies the written file is byte-for-byte the entry.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
