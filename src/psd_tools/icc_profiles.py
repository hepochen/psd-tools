# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os

GRAY_PATH = os.path.join(os.path.dirname(__file__), 'icc_profiles', 'Gray-CIE_L.icc')

if not os.path.isfile(GRAY_PATH) and 'ICC_GRAY_PATH' in os.environ:
    GRAY_PATH = os.environ.get('ICC_GRAY_PATH')

try:
    from PIL import ImageCms
    gray = ImageCms.ImageCmsProfile(GRAY_PATH)
    sRGB = ImageCms.createProfile('sRGB')
except ImportError:
    gray = None
    sRGB = None
