Ah! The error you’re seeing is because of the **`---` at the top** in combination with Markdown. In YAML or some parsers, `---` is interpreted as a YAML document separator, and if you mix it with Markdown list formatting immediately after, it can cause the “did not find expected alphabetic or numeric character” error.

To fix it:

1. **Remove the top `---`**, unless you specifically need it for YAML front matter.
2. Keep your Markdown as-is.

Here’s the corrected version:

````markdown
# Python Exceptions

## Overview

This folder contains Python exercises demonstrating **exception handling**. Each file shows different ways to manage errors, raise exceptions, and safely work with lists and numbers.

## Files

* `0-safe_print_list.py` – Safely prints x elements of a list
* `1-safe_print_integer.py` – Safely prints an integer
* `2-safe_print_list_integers.py` – Prints first x integers of a list
* `3-safe_print_division.py` – Safely divides two integers
* `4-list_division.py` – Divides elements of two lists safely
* `5-raise_exception.py` – Raises a `TypeError`
* `6-raise_exception_msg.py` – Raises a `NameError` with a message

## How to Run

--- bash
python3 0-main.py
python3 3-main.py
---

## Learning Outcomes

* Handle errors with `try/except/finally`
* Safely print and divide numbers and list elements
* Raise and manage exceptions in Python

---


If you want, I can **also rewrite it fully as a one-page, YAML-compatible Markdown** so it won’t trigger any errors. Do you want me to do that?
```
