import logging
import os

if not os.path.exists("log"):
    os.makedirs("log")

logging.basicConfig(
    filename="log/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
