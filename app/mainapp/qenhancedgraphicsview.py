from PyQt5.QtWidgets import QGraphicsView


class QEnhancedGraphicsView(QGraphicsView):
    def __init__(self, widget):
        super(QEnhancedGraphicsView, self).__init__(parent=None)
