# Approximate 8×8 Multipliers – Lookup Table Collection

This repository contains a collection of **20 approximate 8×8 multiplier architectures** implemented in Python. Each multiplier is used to build a LUT (`256×256`) and compute error metrics (MAE and MaxAE). The goal is to explore power/performance/accuracy tradeoffs in approximate arithmetic for low-power and error-tolerant applications.

---

## Directory Structure

* `Approx_multipliers_lut/` – Contains `.npy` files storing LUTs for each architecture.
* `approx_multipliers_lut.py` – Script to generate LUTs, compute error metrics, and save results.

---

## Multiplier Overview and References

| Multiplier Name       | Function Description / Technique                   | Source (Paper)                                                | DOI/URL                                                                        |
| --------------------- | -------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Underdesigned**     | Skips computation in high-error blocks (2×2 UDM)   | Kulkarni et al., VLSID 2011                                   | [DOI:10.1109/VLSID.2011.51](https://doi.org/10.1109/VLSID.2011.51)             |
| **BrokenArray**       | Prunes lower rows of partial products              | Mahdiani et al., TCAS-I 2010                                  | [DOI:10.1109/TCSI.2009.2034166](https://doi.org/10.1109/TCSI.2009.2034166)     |
| **InaccurateCounter** | Approximate adder/counter in PP tree               | Lin and Lin, ICCD 2013                                        | [DOI:10.1109/ICCD.2013.6657022](https://doi.org/10.1109/ICCD.2013.6657022)     |
| **ETM**               | High-order-only multiplication (error-tolerant)    | Kyaw et al., EDSSC 2010                                       | [DOI:10.1109/EDSSC.2010.5705560](https://doi.org/10.1109/EDSSC.2010.5705560)   |
| **SSM**               | Uses MSB for decisions, LSBs for fallback          | Narayanamoorthy et al., TVLSI 2015                            | [DOI:10.1109/TVLSI.2014.2333366](https://doi.org/10.1109/TVLSI.2014.2333366)   |
| **ApproxWallace**     | Approximate reduction in Wallace tree              | Bhardwaj et al., ISQED 2014                                   | [DOI:10.1109/ISQED.2014.6783335](https://doi.org/10.1109/ISQED.2014.6783335)   |
| **Mitchell**          | Log-based multiplication                           | Liu et al., Electronics 2022                                  | [DOI:10.3390/electronics11121913](https://doi.org/10.3390/electronics11121913) |
| **IterLog**           | Adds correction to Mitchell log result             | Babic et al., Electrotechnical Rev. 2010                      | No DOI; [paper](https://ev.fe.uni-lj.si)                                       |
| **DRUM**              | Range-preserving bias-free multiplication          | Hashemi et al., ICCAD 2015                                    | [DOI:10.1109/ICCAD.2015.7372600](https://doi.org/10.1109/ICCAD.2015.7372600)   |
| **AlteredPP**         | Zeroes LSBs of result (partial product truncation) | (Inspired by truncated/altered PP logic, no canonical source) | —                                                                              |
| **APP2**              | Partial product masking + LSB fusion               | (Similar to \[APPx] in ICACCI 2018, no exact source)          | —                                                                              |
| **TAM1**              | Truncates 1 LSB                                    | Jiang et al., TCAS-I 2018                                     | [DOI:10.1109/TCSI.2018.2851874](https://doi.org/10.1109/TCSI.2018.2851874)     |
| **TAM2**              | Truncates 2 LSBs                                   | Jiang et al., TCAS-I 2018                                     | [DOI:10.1109/TCSI.2018.2851874](https://doi.org/10.1109/TCSI.2018.2851874)     |
| **ALM\_SOA**          | Log-based multiplier, ORs result with 1            | Liu et al., TCAS-I 2018                                       | [DOI:10.1109/TCSI.2018.2792902](https://doi.org/10.1109/TCSI.2018.2792902)     |
| **IALM\_SL**          | Scaled-down variant of log multiplier              | Liu et al., TCAS-I 2018                                       | [DOI:10.1109/TCSI.2018.2792902](https://doi.org/10.1109/TCSI.2018.2792902)     |
| **PPP**               | Perforates partial product bits                    | Zervakis et al., GLSVLSI 2015                                 | [DOI:10.1145/2742060.2742109](https://doi.org/10.1145/2742060.2742109)         |
| **LOA**               | OR-based lower-part multiplication                 | Guo et al., TENCON 2018                                       | [DOI:10.1109/TENCON.2018.8650108](https://doi.org/10.1109/TENCON.2018.8650108) |
| **Linearized**        | Linear approximation via shifts                    | (Likely inspired by error modeling methods; no direct source) | —                                                                              |
| **EvoApprox**         | Masked LSBs (fixed) – generic EvoApprox8b model    | Mrázek et al., DATE 2017                                      | [DOI:10.23919/DATE.2017.7926993](https://doi.org/10.23919/DATE.2017.7926993)   |

---

## Metrics

For each multiplier, we compute:

* **MAE** – Mean Absolute Error across all 8×8 combinations
* **MaxAE** – Maximum Absolute Error observed
  
---

## Usage

To regenerate LUTs and evaluate metrics:

```bash
python approx_multipliers_lut.py
```

To load and use any LUT:

```python
import numpy as np
lut = np.load("Approx_multipliers_lut/DRUM_lut.npy")
product = lut[123, 87]
```

---

## Credits

This work compiles, implements, and reproduces key architectures in the field of approximate computing. All functions were cross-verified with academic references or conceptually aligned variants.
