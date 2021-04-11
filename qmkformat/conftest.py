from qmkformat.keyboard import Keyboard
import pytest


@pytest.fixture
def iris():
    return Keyboard.from_kb_info(path='keyboards/iris_rev4.json')