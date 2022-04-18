from enum import Enum
from pathlib import Path
from typing import Callable
from typing import Union

from freesurfer_stats.cortical_stats.format import SpecialHeaders
from freesurfer_stats.freesurfer_stats import FreesurferStats


class CorticalStats(FreesurferStats):
    #: Headers structure
    HEADERS_END = "Measure"

    #: Special headers
    SPECIAL_HEADERS = SpecialHeaders

    def __init__(self, stats_file: Union[Path, str]) -> None:
        super().__init__(stats_file)
