# 🛠️ Itertools of the Trade

Just a small collection of scripts I use to poke at Python's `itertools` (and sometimes `functools`) whenever I'm messing with iterators or want a quick reference.

## 🧠 What's Inside

Each file is basically a tiny demo of one idea — nothing wild, just practical stuff I keep reaching for.

| Script                  | What It Shows                                                         |
| :---------------------- | :-------------------------------------------------------------------- |
| `pairs_without_self.py` | Simple nested-loop pair generation.                                   |
| `efficient_pairs.py`    | Same idea, but using `product()` for cleaner/faster results.          |
| `merge_lists.py`        | Stitch a bunch of lists together with `chain()`.                      |
| `infinite_sequences.py` | Playing with infinite iterators without accidentally nuking your CPU. |
| `group_data.py`         | Quick examples of grouping values using `groupby()`.                  |
| `team_combinations.py`  | Mixing and matching with `permutations()` and `combinations()`.       |
| `chain_react.py`        | A tiny functional pipeline using chains, filters, and reduces.        |
| `infinite_looping.py`   | Some grouped/accumulated transforms for when you want to get fancy.   |

## ⚙️ Why It Exists

I just like having small, readable examples around when I need to remember a pattern or test an idea without spinning up a whole project.

## 💡 Tip

Most of these make more sense if you run them in a REPL and poke around — watching the iterators do their thing hits different.

## 🧵 Tags

`python` · `itertools` · `functional-programming` · `lazy-evaluation` · `data-pipelines`

<br>
