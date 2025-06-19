import numpy as np
import os

N = 8
SIZE = 1 << N
OUTPUT_DIR = "Approx_multipliers_lut"

# Ensure output directory exists
def ensure_output_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# -----------------------------------------------------------------------------
# 1) Define each architecture as a function f(a, b) → approx product
# -----------------------------------------------------------------------------

def mitchell(a, b):
    if a == 0 or b == 0:
        return 0
    return 1 << int(round(np.log2(a) + np.log2(b)))


def loa(a, b, k=2):
    hi = ((a >> k) * (b >> k)) << k
    lo = ((a & ((1 << k) - 1)) | (b & ((1 << k) - 1)))
    return hi | lo


def broken_array(a, b, k=1):
    return (a * (b >> k)) << k


def truncated(a, b, k=2):
    return (a * (b >> k)) << k


def ttc(a, b, k=2):
    tr = (a * (b >> k)) << k
    bias = (1 << (k - 1)) * a
    return tr + bias


def drum(a, b, k=2):
    prod = a * b
    mask = ~((1 << k) - 1)
    return prod & mask


def aam(a, b):
    exact = a * b
    return exact - ((a & b) >> 1)


def moni(a, b):
    return loa(a, b, k=1)


def eta1(a, b):
    return loa(a, b, k=3)


def eta2(a, b):
    return loa(a, b, k=4)


def arr(a, b, k=3):
    return ((a >> k) * (b >> k)) << (2 * k)


def awt(a, b):
    return (a * b) & ~1


def eco(a, b):
    return truncated(a, b, k=1)


def beula(a, b):
    return broken_array(a, b, k=1) + ((a & 1) & (b & 1))


def etl(a, b):
    return truncated(a, b, k=3) + ((a & ((1 << 3) - 1)) >> (3 - 1))


def etam(a, b):
    return ttc(a, b, k=3)


def awt2(a, b):
    return (a * b) & ~3


def waem(a, b):
    return (a * b) + ((a ^ b) & 1)


def wamm(a, b):
    return (a * b) - ((a & b) & 1)


def fmam(a, b):
    return (a * b) >> 1

# Pack architectures\
ARCHS = [
    ("Mitchell", mitchell),
    ("LOA_k2", loa),
    ("BrokenArray_k1", broken_array),
    ("Truncated_k2", truncated),
    ("TTC_k2", ttc),
    ("DRUM_k2", drum),
    ("AAM", aam),
    ("MONA", moni),
    ("ETA-I", eta1),
    ("ETA-II", eta2),
    ("ARR_k3", arr),
    ("AWT", awt),
    ("ECO_k1", eco),
    ("BEULA", beula),
    ("ETL", etl),
    ("ETAM_k3", etam),
    ("AWT-II", awt2),
    ("WAEM", waem),
    ("WAMM", wamm),
    ("FMAM", fmam),
]

# -----------------------------------------------------------------------------
# 2) Build LUT for a given function
# -----------------------------------------------------------------------------

def build_lut(func):
    lut = np.zeros((SIZE, SIZE), dtype=np.uint16)
    for a in range(SIZE):
        for b in range(SIZE):
            lut[a, b] = np.uint16(func(a, b))
    return lut

# -----------------------------------------------------------------------------
# 3) Error metrics
# -----------------------------------------------------------------------------

def error_metrics(lut):
    i = np.arange(SIZE, dtype=int)
    j = np.arange(SIZE, dtype=int)
    exact = np.outer(i, j)
    err = np.abs(lut.astype(int) - exact)
    return float(err.mean()), int(err.max())

# -----------------------------------------------------------------------------
# 4) Main: build, compute, save
# -----------------------------------------------------------------------------

def main():
    ensure_output_dir(OUTPUT_DIR)
    results = []

    for name, fn in ARCHS:
        print(f"Building LUT for {name}...")
        lut = build_lut(fn)
        mae, maxae = error_metrics(lut)
        results.append((name, mae, maxae))

        # Save LUT
        filename = os.path.join(OUTPUT_DIR, f"lut_{name}.npy")
        np.save(filename, lut)
        print(f"Saved {filename}")

    # Print summary
    print(f"\n{'Arch':20s} {'MAE':>10s} {'MaxAE':>10s}")
    print("-"*42)
    for name, mae, maxae in results:
        print(f"{name:20s} {mae:10.2f} {maxae:10d}")

if __name__ == "__main__":
    main()
