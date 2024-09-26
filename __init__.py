"""
@author: da2el
@title: D2 XYPlot Utils
@description: A parameter output node compatible with qq-nodes-comfyui. It outputs parameters such as Prompt S/R and seed.
"""

from .nodes.D2_PromptSR import D2_PromptSR
from .nodes.D2_MultiOutput import D2_MultiOutput
from .nodes.D2_RegexSwitcher import D2_RegexSwitcher
from .nodes.D2_CheckpointLoader import D2_CheckpointLoader
# from .nodes.D2_CheckpointList import D2_CheckpointList


WEB_DIRECTORY = "./web"

NODE_CLASS_MAPPINGS = {
    "D2 Prompt SR": D2_PromptSR,
    "D2 Multi Output": D2_MultiOutput,
    "D2 Regex Switcher": D2_RegexSwitcher,
    "D2 Checkpoint Loader": D2_CheckpointLoader,
    # "D2 Checkpoint List": D2_CheckpointList,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "D2 Prompt SR": "D2 Prompt SR",
    "D2 Multi Output": "D2 Multi Output",
    "D2 Regex Switcher": "D2 Regex Switcher",
    "D2 Checkpoint Loader": "D2 Checkpoint Loader",
    # "D2 Checkpoint List": "D2 Checkpoint List",
}


__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
