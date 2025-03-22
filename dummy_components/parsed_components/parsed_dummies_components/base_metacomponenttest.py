# flake8: noqa: F403, F405, B006
from typing import *

from kfp.dsl import *


def metacomponenttest():
    from dummy_components.dummy_components_v2 import MetaComponentTest

    comp = MetaComponentTest()
    comp.execute()
