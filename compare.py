from typing import Any, Dict, List


class TypeWriter:

    def __init__(self, layout: Dict[str, List[str]], mapping: Dict[str, Any]) -> None:
        self.fingers = {}
        lookup: Dict[str, Any] = {
            "\n":       [{"y": 2, "x": 12, "c": "\n",    "f": mapping["nl"]}],
            "tab" :     [{"y": 1, "x": 0, "c": "\t",    "f": mapping["tab"]}],
            " ":        [{"y": 4, "x": 5, "c": " ",      "f": mapping["space"]}],
            "shift":    [{"y": 3, "x": 0, "c": "lshift", "f": mapping["shift"]}],
            "altgr":    [{"y": 4, "x": 7, "c": "altgr",  "f": mapping["altgr"]}]
        }
        for sub in layout:
            for y, row in enumerate(layout[sub]):
                for x, char in enumerate(row):
                    if char == " ":
                        continue
                    rx = x
                    if y > 0:
                        rx = rx + 1
                    main = mapping["_"][y][x]
                    commands = []
                    if sub != "_":
                        commands = [lookup[sub][0]]
                    commands.append({"y": y, "x": rx, "c": char, "f": main})
                    lookup[char] = commands
        self.lookup = lookup

    def put(self, letter: str) -> float:
        if letter == "\t":
            letter = "tab"
        if letter not in self.lookup:
            return [0.0, 0.0]
        commands = self.lookup[letter]
        lr = [0.0, 0.0]
        
        for command in commands:
            target = command["f"]
            if not target in self.fingers:
                self.fingers[target] = command
                continue
            state = self.fingers[target]
            dx = state["x"] - command["x"]
            dy = state["y"] - command["y"]
            self.fingers[target] = command
            idx = 0 if int(target) <= 5 else 1
            lr[idx] += (dx ** 2 + dy **  2) ** 0.5
        return lr

    def write(self, text: str) -> float:
        text = text.replace("    ", "\t")
        lr = [0, 0]
        for x in text:
            l, r = self.put(x)
            lr[0] += l
            lr[1] += r
        return lr

layouts = {
    "SK_QWERTZ" : {
        # keyboard rows top to bottom, left to right, without any other pressed keys
        "_" : [
            ";+ľščťžýáíé=´",
            "qwertzuiopúäň", 
            "asdfghjklô§", 
            "yxcvbnm,.-"
        ],
        # keyboard rows with pressed shift key
        "shift" : [
            "°1234567890%ˇ",
            "QWERTZUIOP/()",
            "ASDFGHJKL\"!",
            "YXCVBNM?:_"
        ],
        # keyboard rows with pressed altgr key (or ctrl+alt)
        "altgr" : [
            " ~ˇ^˘°˛`·´˝¨¸",
            "\\|€      '÷×¤",
            " đĐ[]  łŁ$ß",
            ">#&@{} <>*"
        ]
    },
    "SK_QWERTY" : {
        "_" : [
            ";+ľščťžýáíé=´",
            "qwertyuiopúäň", 
            "asdfghjklô§", 
            "zxcvbnm,.-"
        ],
        "shift" : [
            "°1234567890%ˇ",
            "QWERTYUIOP/()",
            "ASDFGHJKL\"!",
            "ZXCVBNM?:_"
        ],
        "altgr" : [
            " ~ˇ^˘°˛`·´˝¨¸",
            "\\|€      '÷×¤",
            " đĐ[]  łŁ$ß",
            ">#&@{} <>*"
        ]
    },
    "EN_QWERTZ" : {
        "_" : [
            "`1234567890-=",
            "qwertzuiop[]\\", 
            "asdfghjkl;'", 
            "yxcvbnm,./"
        ],
        "shift" : [
            "~!@#$%^&*()_+",
            "QWERTZUIOP{}|",
            "ASDFGHJKL:\"",
            "YXCVBNM<>?"
        ],
        "altgr" : [
            "             ",
            "             "
            "           ",
            "          "
        ]
    },
    "EN_QWERTY" : {
        "_" : [
            "`1234567890-=",
            "qwertyuiop[]\\", 
            "asdfghjkl;'", 
            "zxcvbnm,./"
        ],
        "shift" : [
            "~!@#$%^&*()_+",
            "QWERTYUIOP{}|",
            "ASDFGHJKL:\"",
            "ZXCVBNM<>?"
        ],
        "altgr" : [
            "             ",
            "             "
            "           ",
            "          "
        ]
    },
}

mapping = {
    # 1 = left thumb, 2 = left index, ..., 5 = left pinky
    # 6 = right thumb, 2 = right index, ..., 10 = right pinky
    "_" : [
        # keyboard rows from top to bottom (°1234, QWERT..., ASDF..., YXCV...)
        "5432111117777",
        "4432227778777",
        "54322277777",
        "2222277777"
    ],
    # mappings for special keys
    "shift" : "5",
    "altgr" : "6",
    "space": "1",
    "tab": "5",
    "nl": "9"
}

with open("example.txt", "r", encoding="utf-8") as f:
    text = f.read()
    for layout in layouts:
        tty = TypeWriter(layouts[layout], mapping)
        l, r = tty.write(text)
        print(f"layout: {layout}, left: {l:10.2f}, right: {r:10.2f}, sum: {l + r:10.2f}")