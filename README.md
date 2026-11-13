# Open Science Code Test

A small Python project for practicing code sharing and archiving. All example values are synthetic; this repository contains no research data.

## Crash rate

The function calculates crashes per million vehicle miles traveled (VMT):

```
crash rate = crashes / vehicle miles traveled × 1,000,000
```

For example, 12 crashes over 4,000,000 vehicle miles gives 3 crashes per million VMT.

```python
from crash_rate import crash_rate_per_million_vmt

rate = crash_rate_per_million_vmt(12, 4_000_000)
print(rate)  # 3.0
```

The crash count must be a nonnegative integer and VMT must be positive and finite. This is an arithmetic demonstration, not a complete safety analysis.

## Run the tests

Python 3 is required; no third-party packages are needed.

```sh
python3 -m unittest -v
```

## License

MIT; see [LICENSE](LICENSE).
