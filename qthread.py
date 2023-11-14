import sys
from contextlib import redirect_stdout

import brightway2 as bw
from bw2data import config
from PySide2.QtCore import QThread
from PySide2 import QtWidgets


proj = 'segfault310'
if proj in bw.projects:
    bw.projects.delete_project(proj, delete_dir=True)
bw.projects.set_current(proj)

class DefaultBiosphereThread(QThread):
    def run(self):
        config.is_test = True  # disables tqdm progress bar
        with open('out.log', 'a') as f:
            with redirect_stdout(f):  # make sure nothing is printed to stdout
                bw.create_default_biosphere3()

app = QtWidgets.QApplication(sys.argv)
thread = DefaultBiosphereThread()
thread.finished.connect(app.exit)
thread.start()
sys.exit(app.exec_())
