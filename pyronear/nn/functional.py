#!usr/bin/python
# -*- coding: utf-8 -*-

# Based on https://github.com/fastai/fastai/blob/master/fastai/layers.py

import torch
import torch.nn.functional as F


def adaptive_concat_pool2d(x, output_size):
    """Concatenates a 2D adaptive max pooling and a 2D adaptive average pooling
    over an input signal composed of several input planes.
    See :class:`~torch.nn.AdaptiveConcatPool2d` for details and output shape.
    Args:
        output_size: the target output size (single integer or
            double-integer tuple)
    """

    return torch.cat([F.adaptive_max_pool2d(x, output_size),
                      F.adaptive_avg_pool2d(x, output_size)], dim=1)
