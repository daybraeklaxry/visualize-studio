# /ui/result_display.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class ResultDisplay(QWidget):
    """结果展示组件 (占位符)"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        """初始化UI"""
        layout = QVBoxLayout(self)
        label = QLabel("右侧结果展示区域\n(由 ResultDisplay 组件负责)")
        label.setStyleSheet("border: 2px dashed #ccc; font-size: 16px;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
