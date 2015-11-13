#魔方类
class magicCube(object):
    def __init__(self, text):
        if len(text) < 50:
            self.setVal('rrrrrrrrrooooooooowwwwwwwwwyyyyyyyyybbbbbbbbbggggggggg')
        else:
            self.setVal(text)
    def __str__(self):
        return self.seq
    def getVal(self):
        return self.seq
    def setVal(self, text):
        #目前仅判断长度是否正确,以后可以添加其他条件判断
        if len(text) != 54:
            print("Invalue Cube!")
            return False
        self.seq = text
        return True
    def gethRotate(self, level):
        #获取水平顺时针旋转，level=1上层旋转，level=2下层旋转
        if level != 1 and level != 2 :
            print("Please Input 1 or 2")
            return self.seq
        if level == 1 :
            s = [6,3,0,7,4,1,8,5,2,9,10,11,12,13,14,15,16,17,45,46,47,21,22,23,24,25,26,36,37,38,30,31,32,33,34,35,18,19,20,39,40,41,42,43,44,27,28,29,48,49,50,51,52,53]
        else:
            s = [0,1,2,3,4,5,6,7,8,15,12,9,16,13,10,17,14,11,18,19,20,21,22,23,42,43,44,27,28,29,30,31,32,51,52,53,36,37,38,39,40,41,33,34,35,45,46,47,48,49,50,24,25,26]
        text = ''
        for i in s:
            text += self.seq[i]
        #self.setVal(text)
        return text
    def getvRotate(self, level):
        #获取垂直顺时针旋转，level=1-4 对应四个面旋转
        if level != 1 and level != 2 and level !=3 and level !=4:
            print("Please Input 1-4")
            return self.seq
        if level == 1 :
            s = [0,1,2,3,4,5,44,41,38,51,48,45,12,13,14,15,16,17,24,21,18,25,22,19,26,23,20,27,28,29,30,31,32,33,34,35,36,37,9,39,40,10,42,43,11,6,46,47,7,49,50,8,52,53]
        if level == 2 :
            s = [0,1,20,3,4,23,6,7,26,9,10,33,12,13,30,15,16,27,18,19,11,21,22,14,24,25,17,8,28,29,5,31,32,2,34,35,36,37,38,39,40,41,42,43,44,51,48,45,52,49,46,53,50,47]
        if level == 3 :
            s = [47,50,53,3,4,5,6,7,8,9,10,11,12,13,14,36,39,42,18,19,20,21,22,23,24,25,26,33,30,27,34,31,28,35,32,29,2,37,38,1,40,41,0,43,44,45,46,17,48,49,16,51,52,15]
        if level == 4 :
            s = [35,1,2,32,4,5,29,7,8,18,10,11,21,13,14,24,16,17,0,19,20,3,22,23,6,25,26,27,28,15,30,31,12,33,34,9,42,39,36,43,40,37,44,41,38,45,46,47,48,49,50,51,52,53]
        text = ''
        for i in s:
            text += self.seq[i]
        #self.setVal(text)
        return text
    def hRotate(self, level):
        self.setVal(self.gethRotate(level))
    def vRotate(self, level):
        self.setVal(self.getvRotate(level))
        
        
