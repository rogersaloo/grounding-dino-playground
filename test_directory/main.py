from pathlib import Path
from GroundingDINO.groundingdino.util.inference import load_model, predict, annotate

ROOT = Path.cwd()
WEIGHTS_NAME = "groundingdino_swint_ogc.pth"

CONFIG_PATH = ROOT.joinpath(WEIGHTS_NAME)
# print(CONFIG_PATH)
# print(ROOT)

model = load_model(CONFIG_PATH, WEIGHTS_NAME)