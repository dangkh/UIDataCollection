# Authors: Clemens Brunner <clemens.brunner@gmail.com>
#
# License: BSD (3-clause)
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from mnelab.mnelab.mainwindow import OtherMainWindow, __version__  # noqa: F401
from mnelab.mnelab.model import Model


__all__ = [OtherMainWindow, Model]
