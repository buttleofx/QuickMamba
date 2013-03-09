from PySide import QtCore, QtGui
from PySide import QtDeclarative


class ColorExtended(QtDeclarative.QDeclarativeItem):

    _color = QtGui.QColor()
	
    def __init__(self, parent=None):
        QtDeclarative.QDeclarativeItem.__init__(self, parent)


    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color
        self.colorChanged.emit()

    def getRed(self):
        return self._color.red()

    def setRed(self, red):
        self._color.setRed(red)
        self.colorChanged.emit()

    def getGreen(self):
        return self._color.green()

    def setGreen(self, green):
        self._color.setGreen(green)
        self.colorChanged.emit()

    def getBlue(self):
        return self._color.blue()

    def setBlue(self, blue):
        self._color.setBlue(blue)
        self.colorChanged.emit()

    def getHue(self):
        return self._color.hue()

    def setHue(self, hue):
        self._color.setHue(hue)
        self.colorChanged.emit()

    def getSaturation(self):
        return self._color.saturation()

    def setSaturation(self, saturation):
        self._color.setSaturation(saturation)
        self.colorChanged.emit()

    def getBrightness(self):
        return self._color.brightness()

    def setBrightness(self, brightness):
        self._color.setBrightness(brightness)
        self.colorChanged.emit()

    def getAlpha(self):
        # alpha returns the value of alpha between 0 and 255 and alphaF between 0 and 1
        return self._color.alphaF()

    def setAlpha(self, alpha):
        self._color.setAlphaF(alpha)
        self.colorChanged.emit()

    colorChanged = QtCore.Signal()
    value = QtCore.Property(QtGui.QColor, getColor, setColor, notify=colorChanged)
    red = QtCore.Property(float, getRed, setRed, notify=colorChanged)
    green = QtCore.Property(float, getGreen, setGreen, notify=colorChanged)
    blue = QtCore.Property(float, getBlue, setBlue, notify=colorChanged)
    hue = QtCore.Property(float, getHue, setHue, notify=colorChanged)
    saturation = QtCore.Property(float, getSaturation, setSaturation, notify=colorChanged)
    brightness = QtCore.Property(float, getBrightness, setBrightness, notify=colorChanged)
    alpha = QtCore.Property(float, getAlpha, setAlpha, notify=colorChanged)


