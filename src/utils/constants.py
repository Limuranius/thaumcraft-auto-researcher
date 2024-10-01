import logging
import os
from os.path import join

# ------------------------
# UI and visual part
MARGIN = 20
FPS = 60

# ------------------------
# Files paths

BASE_DIR = join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

SRC_DIR = join(BASE_DIR, "src")
IMAGES_DIR = join(BASE_DIR, "images")
ASPECTS_CONFIGS_DIR = join(BASE_DIR, "aspects_configs")
USER_CONFIGS_DIR = join(SRC_DIR, "user_configs")

THAUM_VERSION_CONFIG_PATH = join(USER_CONFIGS_DIR, 'thaumVersionConfig.json')
THAUM_CONTROLS_CONFIG_PATH = join(USER_CONFIGS_DIR, 'thaumControlsConfig.json')
THAUM_ASPECT_RECIPES_CONFIG_PATH = join(ASPECTS_CONFIGS_DIR, 'aspectsRecipes.json')
THAUM_ADDONS_ASPECT_RECIPES_CONFIG_PATH = join(ASPECTS_CONFIGS_DIR, 'addonsAspectsRecipes.json')
THAUM_ASPECTS_ORDER_CONFIG_PATH = join(ASPECTS_CONFIGS_DIR, 'aspectsOrder.json')


def getAspectImagePath(aspectName, colored=True):
    return join(IMAGES_DIR, f"{'color' if colored else 'mono'}/{aspectName}.png")


def getImagePathByNumber(number):
    return join(IMAGES_DIR, f"numbers/{number}.png")


UNKNOWN_ASPECT_IMAGE_PATH = join(IMAGES_DIR, "unknownAspect.png")

EMPTY_ASPECT_SLOT_IMAGE_PATH = join(IMAGES_DIR, 'emptyAspectPlace.png')
HEXAGON_MASK_IMAGE_PATH = join(IMAGES_DIR, 'hexagons/hexagonMask.png')
HEXAGON_BORDER_MASK_IMAGE_PATH = join(IMAGES_DIR, 'hexagons/hexagonBorderMask.png')
MASK_WITHOUT_NUMBER_IMAGE_PATH = join(IMAGES_DIR, 'maskWithoutNumbers.png')
MASK_ONLY_NUMBER_IMAGE_PATH = join(IMAGES_DIR, 'maskOnlyNumbers.png')
NONE_HEXAGON_SLOT_IMAGE_PATH = join(IMAGES_DIR, 'hexagons/noneHexagon.png')
FREE_HEXAGON_SLOT_IMAGES_PATHS = [
    join(IMAGES_DIR, 'hexagons/freeHexagons/1.png'),
    join(IMAGES_DIR, 'hexagons/freeHexagons/2.png'),
    join(IMAGES_DIR, 'hexagons/freeHexagons/3.png'),
    join(IMAGES_DIR, 'hexagons/freeHexagons/4.png'),
    join(IMAGES_DIR, 'hexagons/freeHexagons/5.png'),
    join(IMAGES_DIR, 'hexagons/freeHexagons/6.png'),
    join(IMAGES_DIR, 'hexagons/freeHexagons/7.png'),
]
ASPECTS_IMAGES_SIZE = 32  # px

# ------------------------
# In-game inventory
# !!! Don't touch if you not sure !!!
INVENTORY_SLOTS_X = 9
INVENTORY_SLOTS_Y = 3

THAUM_ASPECTS_INVENTORY_SLOTS_X = 5
THAUM_ASPECTS_INVENTORY_SLOTS_Y = 5

THAUM_HEXAGONS_SLOTS_COUNT = 9  # must be odd

DELAY_BETWEEN_EVENTS = 0.15  # seconds
DELAY_BETWEEN_RENDER = 0.5  # seconds

# ------------------------
# Neurolink constants
MODEL_ONNX_PATH = r"D:\Git Projects\thaumcraft-auto-researcher\tmp\weights.onnx"
FREE_HEXAGON_PREDICTION_NAME = "free_hex"
SCRIPT_IMAGE_PREDICTION_NAME = "script"

# ------------------------
# Other constants
EMPTY_TOLERANCE_PERCENT = 0.02
IMAGE_TMP_PATH = join(BASE_DIR, ".tmp/tmp.png")
LOG_FILE_PATH = join(BASE_DIR, "logs/logs.log")
MAX_LOG_FILE_SIZE_BYTES = 1024 * 1024  # 1 Mb

# ------------------------
LOG_LEVEL = logging.DEBUG
# DEBUG = True
DEBUG = False
