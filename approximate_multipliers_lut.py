import numpy as np

# -------------------- 1. Multiplier Architectures --------------------

def underdesigned_multiplier(a, b):
    prod = a * b
    if (a & 0b11) == 0b11 and (b & 0b11) == 0b11:
        prod -= 2
    return prod

def broken_array_multiplier(a, b):
    prod = a * (b & 0xF0)
    return prod & ~0b11

def inaccurate_counter_multiplier(a, b):
    prod = a * b
    if (prod & 0b111) == 0b100:
        prod = (prod & ~0b111) | 0b010
    return prod

def error_tolerant_multiplier(a, b):
    ah, al = a >> 4, a & 0xF
    bh, bl = b >> 4, b & 0xF
    return (ah * bh) << 8 if (ah * bh) != 0 else al * bl

def static_segment_multiplier(a, b):
    ah, al = a >> 4, a & 0xF
    bh, bl = b >> 4, b & 0xF
    return (ah * bh) << 8 if (ah != 0 or bh != 0) else al * bl

def approx_wallace_multiplier(a, b):
    a0, a1 = a & 0xF, a >> 4
    b0, b1 = b & 0xF, b >> 4
    return (a0 * b0) + ((a1 * b1) << 8)

def logarithmic_multiplier(a, b):
    if a == 0 or b == 0:
        return 0
    i, j = a.bit_length() - 1, b.bit_length() - 1
    m, n = a - (1 << i), b - (1 << j)
    return (1 << (i + j)) + (m << j) + (n << i)

def improved_log_multiplier(a, b):
    return logarithmic_multiplier(a, b) + ((a & b) >> 1)

def drum_multiplier(a, b):
    if a == 0 or b == 0:
        return 0
    la, lb, k = a.bit_length() - 1, b.bit_length() - 1, 4
    if la < k-1 or lb < k-1:
        return a * b
    a_core = (1 << la) | (1 << (la - (k - 1)))
    b_core = (1 << lb) | (1 << (lb - (k - 1)))
    return (a_core * b_core) << (la + lb - 2*(k - 1))

def altered_pp_multiplier(a, b):
    return (a * b) & ~0xF

def app2_multiplier(a, b):
    prod = a * b
    return (prod & ~0x3FF) | (prod & 0x3)

def tam1_multiplier(a, b):
    return (a * b) & ~0b1

def tam2_multiplier(a, b):
    return (a * b) & ~0b11

def alms1_multiplier(a, b):
    return logarithmic_multiplier(a, b) | 0x1

def ialm_sl_multiplier(a, b):
    return (logarithmic_multiplier(a, b) >> 2) << 2

def ppp_multiplier(a, b):
    return ((a >> 2) * (b >> 2)) << 4

def loa_multiplier(a, b):
    res = 0
    for i in range(8):
        if (a >> i) & 1:
            for j in range(8):
                if (b >> j) & 1:
                    res |= (1 << (i + j))
    return res

def linearized_multiplier(a, b):
    prod = a * b
    return (prod >> 1) + (prod >> 2)

def evolvable_multiplier(a, b):
    return (a * b) & 0xFFFF

# -------------------- 2. Metadata --------------------

ARCHS = [
    ("Underdesigned", underdesigned_multiplier),
    ("BrokenArray", broken_array_multiplier),
    ("InaccurateCounter", inaccurate_counter_multiplier),
    ("ETM", error_tolerant_multiplier),
    ("SSM", static_segment_multiplier),
    ("ApproxWallace", approx_wallace_multiplier),
    ("Mitchell", logarithmic_multiplier),
    ("IterLog", improved_log_multiplier),
    ("DRUM", drum_multiplier),
    ("AlteredPP", altered_pp_multiplier),
    ("APP2", app2_multiplier),
    ("TAM1", tam1_multiplier),
    ("TAM2", tam2_multiplier),
    ("ALM_SOA", alms1_multiplier),
    ("IALM_SL", ialm_sl_multiplier),
    ("PPP", ppp_multiplier),
    ("LOA", loa_multiplier),
    ("Linearized", linearized_multiplier),
    ("EvoApprox", evolvable_multiplier),
]

# -------------------- 3. LUT + Metrics --------------------

SIZE = 256

def build_lut(fn):
    lut = np.zeros((SIZE, SIZE), dtype=np.uint16)
    for i in range(SIZE):
        for j in range(SIZE):
            lut[i, j] = fn(i, j)
    return lut

def compute_error_metrics(lut):
    exact = np.outer(np.arange(SIZE), np.arange(SIZE))
    err = np.abs(lut.astype(int) - exact)
    return err.mean(), err.max()

# -------------------- 4. Run --------------------

def main():
    print(f"{'Architecture':20s} {'MAE':>10} {'MaxAE':>10}")
    print("-" * 42)
    for name, fn in ARCHS:
        lut = build_lut(fn)
        mae, maxae = compute_error_metrics(lut)
        print(f"{name:20s} {mae:10.2f} {maxae:10d}")
import os

OUTPUT_DIR = "Approx_multipliers_lut"

def ensure_output_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_luts():
    ensure_output_dir(OUTPUT_DIR)
    print("\nSaving LUTs:")
    for name, fn in ARCHS:
        lut = build_lut(fn)
        filename = os.path.join(OUTPUT_DIR, f"{name}_lut.npy")
        np.save(filename, lut)
        print(f"✔ Saved {filename}")

# Call this function if you want to save the LUTs after evaluating metrics
if __name__ == "__main__":
    main()
    save_luts()

