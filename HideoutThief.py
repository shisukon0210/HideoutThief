class Hideout:
    def __init__(self):
        self.sysword = ['version', 'language', 'hideout_name', 'hideout_hash']
        self.whitelist = ['倉庫', '公會倉庫', '傳送點', '工藝台', '黃金地球儀', '娜瓦莉', '埃哈', '艾瓦', '赫蓮娜', '尼科', '瓊恩', '札那', '修女卡西亞', '塔恩．奧克塔維斯', '基拉克', '戰鬥詩人．丹尼格', '賭徒．關南', '討價還價．圖貞', '商人．羅格']
        self.decorations = []
        self.newDecorations = []

    def hideoutInput(self, file):
        self.decorations = file.readlines()

    def moveHideout(self, x, y, file):
        for i in range(6):
            tmp = file.readline()
            self.newDecorations.append(tmp)

        for line in range(6, len(self.decorations)):
            if self.decorations[line] == "{":
                continue
            flag = 0
            for item in self.whitelist:
                if item in self.decorations[line]:
                    flag = 1
                    break
            counter = 0
            if flag == 1:
                self.newDecorations.append(self.decorations[line])
                counter += 2
                continue
            if "\"x\"" in self.decorations[line] and counter==0:
                xs = self.decorations[line].split(":")
                xss = xs[-1].split(",")
                xline = xs[0] + ":" + str(int(xss[0])+x) + ",\n"
                self.newDecorations.append(xline)
                continue
            if "\"x\"" in self.decorations[line] and counter>0:
                self.newDecorations.append(self.decorations[line])
                counter -= 1
                continue
            if "\"y\"" in self.decorations[line] and counter==0:
                ys = self.decorations[line].split(":")
                yss = ys[-1].split(",")
                yline = ys[0] + ":" + str(int(yss[0])+y) + ",\n"
                self.newDecorations.append(yline)
                continue
            if "\"y\"" in self.decorations[line] and counter>0:
                self.newDecorations.append(self.decorations[line])
                counter -= 1
                continue
            self.newDecorations.append(self.decorations[line])

    def printHideout(self):
        for line in self.decorations:
            print(line, end='')

    def printNewHideout(self):
        for line in self.newDecorations:
            print(line, end='')

    def outputNewHideout(self, file):
        for line in self.newDecorations:
            file.write(line)

def hideoutMoving(fname, fname2, x, y):
    file = open(fname, 'r', encoding='utf-8')
    file2 = open(fname2, 'r', encoding='utf-8')
    obj = Hideout()
    obj.hideoutInput(file)
    file.close()
    obj.moveHideout(x, y, file2)
    file2.close()
    file2 = open(fname2, "w", encoding='utf-8')
    obj.outputNewHideout(file2)

if __name__ == "__main__":
    fname = "pekora.hideout"
    file = open(fname, 'r', encoding='utf-8')
    names = fname.split(".")
    fname2 = names[0] + "_new." + names[1]
    file2 = open(fname2, "r", encoding='utf-8')
    obj = Hideout()
    obj.hideoutInput(file)
    file.close()
    # obj.printHideout()
    obj.moveHideout(43, -43, file2)
    file2.close()
    file2 = open(fname2, "w", encoding='utf-8')
    # obj.printNewHideout()
    obj.outputNewHideout(file2)
