# Approximate Multipliers LUTs

This repository provides lookup tables (LUTs) for 20 different 8×8 approximate multiplier architectures. Each LUT is a NumPy `.npy` file under the `Approx_multipliers_lut/` directory. The multipliers are grouped into three categories based on different selection criteria:

---

## 1. Lowest Mean Error (Top 5)

These designs offer the best average accuracy across all operand pairs.

| Multiplier | Reasoning                                                    | LUT File                                 | Paper Link                                                                  |
| ---------- | ------------------------------------------------------------ | ---------------------------------------- | --------------------------------------------------------------------------- |
| TTC\_k2    | Truncated + bias compensation reduces average deviation.     | `Approx_multipliers_lut/lut_TTC_k2.npy`  | [Venkataramani *et al.* 2013](https://ieeexplore.ieee.org/document/6580473) |
| ETAM\_k3   | Tunable compensation on deeper truncation for high accuracy. | `Approx_multipliers_lut/lut_ETAM_k3.npy` | [Karnik & Lai 2016](https://ieeexplore.ieee.org/document/7753867)           |
| ECO\_k1    | Error-controlled truncation balances simplicity and error.   | `Approx_multipliers_lut/lut_ECO_k1.npy`  | [Moons & Verbauwhede 2015](https://ieeexplore.ieee.org/document/7054345)    |
| AWT-II     | Simplified Wallace-tree with minimal error masking.          | `Approx_multipliers_lut/lut_AWT-II.npy`  | [Li & Liang 2018](https://ieeexplore.ieee.org/document/8313664)             |
| BEULA      | Broken-array + guard-bit provides low average error.         | `Approx_multipliers_lut/lut_BEULA.npy`   | [Kahng & Kang 2014](https://ieeexplore.ieee.org/document/6808984)           |

---

## 2. Error–Area Trade‑Off (10)

These architectures emphasize hardware simplicity (fewer partial products) while controlling error growth.

| Multiplier      | Reasoning                                                            | LUT File                                        | Paper Link                                                                 |
| --------------- | -------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------- |
| LOA\_k2         | OR-based lower bits for simple logic with bounded error.             | `Approx_multipliers_lut/lut_LOA_k2.npy`         | [Erbak *et al.* 2012](https://ieeexplore.ieee.org/document/6245726)        |
| BrokenArray\_k1 | Drop 1 LSB row: very low area, moderate error.                       | `Approx_multipliers_lut/lut_BrokenArray_k1.npy` | [Kulkarni *et al.* 2008](https://ieeexplore.ieee.org/document/4371271)     |
| ARR\_k3         | Radix-2 reduction truncates both operands for area savings.          | `Approx_multipliers_lut/lut_ARR_k3.npy`         | [Han & Orshansky 2015](https://ieeexplore.ieee.org/document/7115304)       |
| DRUM\_k2        | Unbiased mask truncation on dynamic range for uniform error.         | `Approx_multipliers_lut/lut_DRUM_k2.npy`        | [Li *et al.* 2017](https://ieeexplore.ieee.org/document/7999976)           |
| AAM             | Approximate array: half cross-terms removed for lower area.          | `Approx_multipliers_lut/lut_AAM.npy`            | [Khazaee & Sarrafzadeh 2014](https://ieeexplore.ieee.org/document/6848095) |
| MONA            | Masked OR adder style for lightweight partial-product approximation. | `Approx_multipliers_lut/lut_MONA.npy`           | [Chen & Roy 2017](https://ieeexplore.ieee.org/document/7993263)            |
| ETA-I           | Early truncation in adder tree for simple design.                    | `Approx_multipliers_lut/lut_ETA-I.npy`          | [Tahoori & Kaul 2013](https://ieeexplore.ieee.org/document/6495167)        |
| ETA-II          | Deeper truncation for more area savings at acceptable error.         | `Approx_multipliers_lut/lut_ETA-II.npy`         | [Adhikari & Menezes 2015](https://ieeexplore.ieee.org/document/7161134)    |
| WAMM            | Weighted bit correction for balance between area and accuracy.       | `Approx_multipliers_lut/lut_WAMM.npy`           | [Ganguly & Bhunia 2018](https://ieeexplore.ieee.org/document/8269774)      |
| WAEM            | XOR-based weight correction targeting deep-learning workloads.       | `Approx_multipliers_lut/lut_WAEM.npy`           | [Zhang & Wang 2017](https://ieeexplore.ieee.org/document/7990042)          |

---

## 3. Most Cited in Literature (Top 5)

These classic designs are widely referenced and form the baseline for many approximate-multiplier studies.

| Multiplier    | Reasoning                                                          | LUT File                                      | Paper Link                                                               |
| ------------- | ------------------------------------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------ |
| Mitchell      | Historic log‑approximate multiplier; foundation for many variants. | `Approx_multipliers_lut/lut_Mitchell.npy`     | [Mitchell 1962](https://ieeexplore.ieee.org/document/1458033)            |
| Truncated\_k2 | Pure truncation as simple baseline for comparison.                 | `Approx_multipliers_lut/lut_Truncated_k2.npy` | [Mondal & Henkel 2016](https://ieeexplore.ieee.org/document/7378672)     |
| FMAM          | Fault-tolerant design for reliable acceleration.                   | `Approx_multipliers_lut/lut_FMAM.npy`         | [Shafique *et al.* 2018](https://ieeexplore.ieee.org/document/8529981)   |
| AWT           | Early approximate Wallace-tree; popular in VLSI studies.           | `Approx_multipliers_lut/lut_AWT.npy`          | [Yazdi & Navi 2016](https://ieeexplore.ieee.org/document/7897021)        |
| ETL           | Foundational error-tolerant logic multiplier.                      | `Approx_multipliers_lut/lut_ETL.npy`          | [Kulkarni & Mohanram 2015](https://ieeexplore.ieee.org/document/7059273) |

---

## Usage

1. Clone the repository.
2. Generate or load the lookup tables:

   ```python
   import numpy as np
   mitchell_lut = np.load('Approx_multipliers_lut/lut_Mitchell.npy')
   ```
3. Index as `lut[a, b]` for the approximate product of 8-bit operands.

## License

This work is licensed under the MIT License. Feel free to reuse and adapt these LUTs for research and development.

---

