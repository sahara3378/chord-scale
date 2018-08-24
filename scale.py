# -*- coding: utf-8 -*-
musicNotes = ["C", "#C", "D", "bE", "E", "F", "#F", "G", "#G", "A", "bB", "B"]

tmp = []


# 音阶类
class Scale:

    # 获取自然音阶大调
    def get_natrual_major(self, root, pro):
        if root in musicNotes:
            # 获取当前元素的位置
            num = musicNotes.index(root)
            tmp.append(root)
            if pro.startswith("Ionian"):
                for i in range(1, 8):
                    if i == 3 or i == 7:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    tmp.append(musicNotes[(num + 2) % 12])
                    num = musicNotes.index(tmp[i])
            elif pro.startswith("Lydian"):
                for i in range(1, 8):
                    if i == 4 or i == 7:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    tmp.append(musicNotes[(num + 2) % 12])
                    num = musicNotes.index(tmp[i])
            elif pro.startswith("Mixolydian"):
                for i in range(1, 8):
                    if i == 3:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    if i == 6:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    tmp.append(musicNotes[(num + 2) % 12])
                    num = musicNotes.index(tmp[i])
            return tmp

    # 获取自然音阶小调
    def get_natrual_minor(self, root, pro):
        if root in musicNotes:
            # 获取当前元素的位置
            num = musicNotes.index(root)
            tmp.append(root)
            if pro.startswith("Aeolian"):
                for i in range(1, 8):
                    if i == 2 or i == 5:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    tmp.append(musicNotes[(num + 2) % 12])
                    num = musicNotes.index(tmp[i])
            elif pro.startswith("Dorian"):
                for i in range(1, 8):
                    if i == 2 or i == 6:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    tmp.append(musicNotes[(num + 2) % 12])
                    num = musicNotes.index(tmp[i])
            elif pro.startswith("Phrygian"):
                for i in range(1, 8):
                    if i == 1:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    if i == 5:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    tmp.append(musicNotes[(num + 2) % 12])
                    num = musicNotes.index(tmp[i])
            elif pro.startswith("Locrian"):
                for i in range(1, 8):
                    if i == 1:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    if i == 4:
                        tmp.append(musicNotes[(num + 1) % 12])
                        num = musicNotes.index(tmp[i])
                        continue
                    tmp.append(musicNotes[(num + 2) % 12])
                    num = musicNotes.index(tmp[i])
            return tmp

    # 获取五声音阶大调
    def get_pentatonic_major(self, tmp, pro, index):
        if tmp:
            if pro.startswith("Pentatonic-maj"):
                del tmp[index]
                return tmp

    # 获取五声音阶小调
    def get_pentatonic_minor(self, tmp, pro, index):
        if tmp:
            if pro.startswith("Pentatonic-min"):
                del tmp[index]
                return tmp

    # 获取布鲁斯音阶大调
    def get_blues_major(self, tmp, pro, index):
        if tmp:
            if pro.startswith("Blues-maj"):
                num = musicNotes.index(tmp[index])
                print(musicNotes[(num - 1) % 12])
                tmp.insert(num - 2, musicNotes[(num - 1) % 12])
                return tmp

    # 获取布鲁斯音阶小调
    def get_blues_minor(self, tmp, pro, index):
        if tmp:
            if pro.startswith("Blues-min"):
                num = musicNotes.index(tmp[index])
                print(musicNotes[(num + 1) % 12])
                tmp.insert(num - 2, musicNotes[(num + 1) % 12])
                return tmp


if __name__ == '__main__':
    s = Scale()

    # tmp = s.get_natrual_major('C', 'Ionian')
    # print(tmp)
    # tmp1 = s.get_pentatonic_major(s.get_pentatonic_major(tmp, 'Pentatonic-maj', 3), 'Pentatonic-maj', 5)
    # print(tmp1)
    # tmp2 = s.get_blues_major(tmp1, "Blues-maj", 2)
    # print(tmp2)

    # t = s.get_natrual_minor('C', 'Aeolian')
    # print(t)
    # t1 = s.get_pentatonic_minor(s.get_pentatonic_minor(t, 'Pentatonic-min', 1), 'Pentatonic-min', 4)
    # print(t1)
    # t2 = s.get_blues_minor(t1, "Blues-min", 2)
    # print(t2)
