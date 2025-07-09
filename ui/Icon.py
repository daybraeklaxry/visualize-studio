# /ui/Icon.py
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QByteArray, QBuffer
import os

# 注意：为了让代码能跑起来，需要一个 qrc 文件和对应的资源。
# 假设我们已经通过 pyrcc5 生成了 icons_rc.py
# import newYear.resources.icons_rc  # 实际项目中需要这一行

class Icon:
    """图标资源管理类"""
    
    # 默认头像
    Default_avatar_path = ':/icons/default_avatar.svg'
    # 远优于：QPixmap(':/icons/default_avatar.svg')
    _default_avatar = None
    
    # 其他图标路径
    Logo_path = ':/icons/logo.svg'
    Logo = QIcon(Logo_path)
    
    @classmethod
    def get_default_avatar(cls):
        """获取默认头像"""
        if cls._default_avatar is None:
            # 懒加载：第一次需要时才创建 QPixmap 对象
            cls._default_avatar = QPixmap(cls.Default_avatar_path)
        return cls._default_avatar
        
    @classmethod
    def get_default_avatar_bytes(cls):
        """获取默认头像的二进制数据"""
        if cls._default_avatar is None:
            cls._default_avatar = QPixmap(cls.Default_avatar_path)
        ba = QByteArray()
        buffer = QBuffer(ba)
        buffer.open(QBuffer.WriteOnly)
        cls._default_avatar.save(buffer, 'PNG')
        return ba.data()
