import random

import numpy as np
import torch

DEFAULT_SEED = 1


def set_global_seed(seed):
    """
    Seed every source of randomness this project touches — Python's random,
    NumPy, and PyTorch (CPU + CUDA) — and force PyTorch onto its
    deterministic algorithm paths.

    This is what makes a run reproducible across machines/GPUs, not just
    across re-runs on the same one. Note: PyTorch's deterministic mode plus
    these seeds gets you as close to bit-identical as PyTorch allows, but
    exact bit-for-bit equality across different GPU architectures still
    isn't 100% guaranteed (floating-point reduction order can differ at the
    hardware level) — this is the practical ceiling, not an absolute one.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    return seed
