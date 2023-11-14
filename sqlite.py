import sys

from peewee import SqliteDatabase
from PySide2.QtCore import QThread
from PySide2 import QtWidgets


db = SqliteDatabase('my_database.db')

class DefaultBiosphereThread(QThread):
    def run(self):
        db.connect()

app = QtWidgets.QApplication(sys.argv)
thread = DefaultBiosphereThread()
thread.finished.connect(app.exit)
thread.start()
sys.exit(app.exec_())
