import numpy as np


def hist2array(h, flow=False, copy=True, include_sumw2=False):
    nx = h.GetNbinsX() + 2
    dtype = 0
    if isinstance(h, ROOT.TH1D):
        dtype = np.double
    elif isinstance(h, ROOT.TH1F):
        dtype = np.float
    elif isinstance(h, ROOT.TH1I):
        dtype = np.int
    else:
        print("Histogram of type", h, "is not supperted", file=sys.stderr)
        sys.exit(1)

    vals = np.ndarray((nx,), dtype=dtype, buffer=h.GetArray())
    sumw2 = np.ndarray((nx,), dtype=dtype, buffer=h.GetSumw2().GetArray())

    shift = 0
    if flow:
        shift = 1
    vals = vals[shift : nx - shift]
    sumw2 = sumw2[shift : nx - shift]

    if copy:
        vals = vals.copy()
        sumw2 = sumw2.copy()
    if include_sumw2:
        return vals, sumw2
    else:
        return vals
