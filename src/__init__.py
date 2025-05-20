"""
Meta Ads Analytics - Um projeto para análise de anúncios do Facebook
"""

__version__ = '1.0.0'
__author__ = 'Seu Nome'
__email__ = 'seu.email@exemplo.com'

from . import api
from . import processor
from . import visualizer
from . import config

__all__ = ['api', 'processor', 'visualizer', 'config'] 