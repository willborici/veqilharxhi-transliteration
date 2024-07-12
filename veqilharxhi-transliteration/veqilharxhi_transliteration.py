# Transliterate between official Albanian letters (Latin alphabet-based)
# and the Vithkuq or Veqilharxhi script characters.

# model a character object
class Character:
    def __init__(self, character_name=None, unicode_value=None):
        self.__character_name = character_name
        self.__unicode_value = unicode_value

        # if no character provided, but a Unicode value is given,
        # get character from Unicode
        if character_name is None and unicode_value is not None:
            # if digraph, return a digraph character via concatenation
            if tuple(unicode_value):
                self.__character_name = chr(unicode_value[0]) + chr(unicode_value[1])
            else:
                self.__character_name = chr(unicode_value)

    @property
    def unicode_value(self):
        return self.__unicode_value

    @property
    def character_name(self):
        return self.__character_name

    def display_info(self):
        info = f"Unicode value: {self.unicode_value}"
        info += f", Character name: {self.character_name}"
        print(info)

    def __str__(self):
        return f"Unicode: {hex(self.unicode_value)}, Name: {self.character_name}"


class AlbanianLetter(Character):
    # Define the dictionary mapping Albanian letters to their Unicode code points
    # as well as paris of Unicode points for the digraphs
    albanian_characters_unicode = {
        'a': ord('a'),
        'A': ord('A'),
        'b': ord('b'),
        'B': ord('B'),
        'c': ord('c'),
        'C': ord('C'),
        'ç': ord('ç'),
        'Ç': ord('Ç'),
        'd': ord('d'),
        'D': ord('D'),
        'dh': (ord('d'), ord('h')),
        'Dh': (ord('D'), ord('h')),
        'e': ord('e'),
        'E': ord('E'),
        'ë': ord('ë'),
        'Ë': ord('Ë'),
        'f': ord('f'),
        'F': ord('F'),
        'g': ord('g'),
        'G': ord('G'),
        'gj': (ord('g'), ord('j')),
        'Gj': (ord('G'), ord('j')),
        'h': ord('h'),
        'H': ord('H'),
        'i': ord('i'),
        'I': ord('I'),
        'j': ord('j'),
        'J': ord('J'),
        'k': ord('k'),
        'K': ord('K'),
        'l': ord('l'),
        'L': ord('L'),
        'll': (ord('l'), ord('l')),
        'Ll': (ord('L'), ord('l')),
        'm': ord('m'),
        'M': ord('M'),
        'n': ord('n'),
        'N': ord('N'),
        'nj': (ord('n'), ord('j')),
        'Nj': (ord('N'), ord('j')),
        'o': ord('o'),
        'O': ord('O'),
        'p': ord('p'),
        'P': ord('P'),
        'q': ord('q'),
        'Q': ord('Q'),
        'r': ord('r'),
        'R': ord('R'),
        'rr': (ord('r'), ord('r')),
        'Rr': (ord('R'), ord('r')),
        's': ord('s'),
        'S': ord('S'),
        'sh': (ord('s'), ord('h')),
        'Sh': (ord('S'), ord('h')),
        't': ord('t'),
        'T': ord('T'),
        'th': (ord('t'), ord('h')),
        'Th': (ord('T'), ord('h')),
        'u': ord('u'),
        'U': ord('U'),
        'v': ord('v'),
        'V': ord('V'),
        'x': ord('x'),
        'X': ord('X'),
        'xh': (ord('x'), ord('h')),
        'Xh': (ord('X'), ord('h')),
        'y': ord('y'),
        'Y': ord('Y'),
        'z': ord('z'),
        'Z': ord('Z'),
        'zh': (ord('z'), ord('h')),
        'Zh': (ord('Z'), ord('h'))
    }

    def __init__(self, character_name=None, unicode_value=None, is_uppercase=False, is_digraph=False):
        super().__init__(character_name, AlbanianLetter.albanian_letter_unicode(character_name))
        self.__language = "Albanian (official)"
        self.__is_uppercase = is_uppercase
        self.__is_digraph = is_digraph  # for the Albanian digraphs

    # fetch a unicode, given a letter
    @classmethod
    def albanian_letter_unicode(cls, letter):
        return cls.albanian_characters_unicode.get(letter)

    # given a unicode value or tuple, fetch the corresponding Albanian letter
    @classmethod
    def unicode_albanian_letter(cls, unicode_value):
        # reverse the equivalence in the albanian_characters_unicode dictionary:
        unicode_to_albanian_letter = {v: k for k, v in cls.albanian_characters_unicode.items()}
        return unicode_to_albanian_letter.get(unicode_value)

    # the letter to be provided includes digraphs
    @classmethod
    def is_albanian_letter(cls, letter):
        # Unicode range for Albanian letters (basic latin, latin1 supp, latin ext):
        return letter in cls.albanian_characters_unicode

    def __str__(self):
        info = super().__str__()
        info += f", Language: {self.__language}, Uppercase: {self.__is_uppercase}"
        return info


class VeqilharxhiLetter(Character):
    def __init__(self, character_name=None, unicode_value=None, is_uppercase=False):
        super().__init__(character_name, unicode_value)
        self.__language = "Albanian (Vithkuqi Script)"
        self.__is_uppercase = is_uppercase

    @classmethod
    def is_vithkuqi_letter(cls, letter):
        # Unicode range for Vithkuqi letters: https://www.unicode.org/charts/PDF/U10570.pdf
        return ord(letter) in range(0x10570, 0x105BD + 1)

    def __str__(self):
        info = super().__str__()
        info += f", Language: {self.__language}, Uppercase: {self.__is_uppercase}"
        return info


# initialize the lookups:
# NB: spaces are needed to distinguish between double letters
ALBANIAN_LOWERCASE = 'a b c ç d dh e ë f g gj h i j k l ll m n nj o p q r rr s sh t th u v x xh y z zh'
ALBANIAN_UPPERCASE = 'A B C Ç D Dh E Ë F G Gj H I J K L Ll M N Nj O P Q R Rr S Sh T Th U V X Xh Y Z Zh'

# get the Vithkuqi script per the 2021 official Unicode range
# note: you need to have the Vithkuqi font installed to render the letters
# Enclosed in this git repo is a font I designed in 2019.
VITHKUQI_UPPERCASE = ' '.join(chr(code) for code in range(0x10570, 0x10596 + 1))
VITHKUQI_LOWERCASE = ' '.join(chr(code) for code in range(0x10597, 0x105BD + 1))

# Combine lowercase and uppercase letters
albanian_letters = ALBANIAN_LOWERCASE + ' ' + ALBANIAN_UPPERCASE
vithkuqi_letters = VITHKUQI_LOWERCASE + ' ' + VITHKUQI_UPPERCASE


# Function to instantiate characters
def store_letters(letters, is_alb_script):
    upper_case_letters = ALBANIAN_UPPERCASE if is_alb_script else VITHKUQI_UPPERCASE

    # strip spaces and store in a list
    characters = letters.strip(' ')

    # store letters in a list:
    script = []
    for character in characters:
        is_uppercase = True if character in upper_case_letters else False
        if is_alb_script:
            is_digraph = len(character) == 2
            letter = AlbanianLetter(character_name=character,
                                    unicode_value=AlbanianLetter.albanian_letter_unicode(letter=character),
                                    is_uppercase=is_uppercase, is_digraph=is_digraph)
        else:
            letter = VeqilharxhiLetter(character_name=character, is_uppercase=is_uppercase)

        script.append(letter)

    return script


# initialize the two lists:
alb_script = store_letters(albanian_letters, True)
vith_script = store_letters(vithkuqi_letters, False)

# print the letters in the run console to facilitate manual script equivalence construction:
alb_letter_index = 0
vith_letter_index = 0
albanian_letters = albanian_letters.split(' ')
vithkuqi_letters = vithkuqi_letters.split(' ')
print(albanian_letters)
while alb_letter_index < len(albanian_letters) and vith_letter_index < len(vithkuqi_letters):
    alb_letter = albanian_letters[alb_letter_index]
    vith_letter = vithkuqi_letters[vith_letter_index]
    no_alb_equivalent = False

    if ord(vith_letter) in (66969, 66980, 66982, 66930, 66941, 66943):
        no_alb_equivalent = True
        alb_letter = None

    if alb_letter is not None:
        alb_letter = albanian_letters[alb_letter_index]

    vith_letter = vithkuqi_letters[vith_letter_index]

    if no_alb_equivalent:
        print(f" {-vith_letter_index}: {ord(vith_letter)}, # {alb_letter} --> {vith_letter}")
    else:
        print(
            f" {AlbanianLetter.albanian_letter_unicode(alb_letter)}: {ord(vith_letter)}, # {alb_letter} --> {vith_letter}")

    if alb_letter is not None:
        alb_letter_index += 1
    vith_letter_index += 1

# create the script equivalence with the help of the "while" loop above:
# the negative-valued keys are dummy values I assigned to indicate that
# there is no Albanian letter equivalent to the corresponding Veqilharxhi letter
# The digraphs have a tuple of Unicode points.
script_equivalence = {
    97: 66967,  # a --> 𐖗
    98: 66968,  # b --> 𐖘
    -2: 66969,  # None --> 𐖙
    99: 66970,  # c --> 𐖚
    231: 66971,  # ç --> 𐖛
    100: 66972,  # d --> 𐖜
    (100, 104): 66973,  # dh --> 𐖝
    101: 66974,  # e --> 𐖞
    235: 66975,  # ë --> 𐖟
    102: 66976,  # f --> 𐖠
    103: 66977,  # g --> 𐖡
    (103, 106): 66978,  # gj --> 𐖢
    104: 66979,  # h --> 𐖣
    -13: 66980,  # None --> 𐖤
    105: 66981,  # i --> 𐖥
    -15: 66982,  # None --> 𐖦
    106: 66983,  # j --> 𐖧
    107: 66984,  # k --> 𐖨
    108: 66985,  # l --> 𐖩
    (108, 108): 66986,  # ll --> 𐖪
    109: 66987,  # m --> 𐖫
    110: 66988,  # n --> 𐖬
    (110, 106): 66989,  # nj --> 𐖭
    111: 66990,  # o --> 𐖮
    112: 66991,  # p --> 𐖯
    113: 66992,  # q --> 𐖰
    114: 66993,  # r --> 𐖱
    (114, 114): 66994,  # rr --> 𐖲
    115: 66995,  # s --> 𐖳
    (115, 104): 66996,  # sh --> 𐖴
    116: 66997,  # t --> 𐖵
    (116, 104): 66998,  # th --> 𐖶
    117: 66999,  # u --> 𐖷
    118: 67000,  # v --> 𐖸
    120: 67001,  # x --> 𐖹
    (120, 104): 67002,  # xh --> 𐖺
    121: 67003,  # y --> 𐖻
    122: 67004,  # z --> 𐖼
    (122, 104): 67005,  # zh --> 𐖽
    65: 66928,  # A --> 𐕰
    66: 66929,  # B --> 𐕱
    -41: 66930,  # None --> 𐕲
    67: 66931,  # C --> 𐕳
    199: 66932,  # Ç --> 𐕴
    68: 66933,  # D --> 𐕵
    (68, 104): 66934,  # Dh --> 𐕶
    69: 66935,  # E --> 𐕷
    203: 66936,  # Ë --> 𐕸
    70: 66937,  # F --> 𐕹
    71: 66938,  # G --> 𐕺
    (71, 106): 66939,  # Gj --> 𐕻
    72: 66940,  # H --> 𐕼
    -52: 66941,  # None --> 𐕽
    73: 66942,  # I --> 𐕾
    -54: 66943,  # None --> 𐕿
    74: 66944,  # J --> 𐖀
    75: 66945,  # K --> 𐖁
    76: 66946,  # L --> 𐖂
    (76, 108): 66947,  # Ll --> 𐖃
    77: 66948,  # M --> 𐖄
    78: 66949,  # N --> 𐖅
    (78, 106): 66950,  # Nj --> 𐖆
    79: 66951,  # O --> 𐖇
    80: 66952,  # P --> 𐖈
    81: 66953,  # Q --> 𐖉
    82: 66954,  # R --> 𐖊
    (82, 114): 66955,  # Rr --> 𐖋
    83: 66956,  # S --> 𐖌
    (83, 104): 66957,  # Sh --> 𐖍
    84: 66958,  # T --> 𐖎
    (84, 104): 66959,  # Th --> 𐖏
    85: 66960,  # U --> 𐖐
    86: 66961,  # V --> 𐖑
    88: 66962,  # X --> 𐖒
    (88, 104): 66963,  # Xh --> 𐖓
    89: 66964,  # Y --> 𐖔
    90: 66965,  # Z --> 𐖕
    (90, 104): 66966  # Zh --> 𐖖
}
# Reverse the mapping (Vithkuqi to Albanian) into a different dictionary
reverse_equivalence = {v: k for k, v in script_equivalence.items()}


# Transliterate a string
def transliterate(input_string):
    output_string = ""
    i = 0
    while i < len(input_string):
        current_char = input_string[i]
        if AlbanianLetter.is_albanian_letter(current_char):
            # check if the current character forms a digraph with the next;
            # if so, fetch the Unicode point from the tuple key, and convert it to chr:
            if (i + 1 < len(input_string) and
                    isinstance(AlbanianLetter.albanian_letter_unicode(current_char + input_string[i + 1]), tuple)):
                output_string += chr(script_equivalence.get((ord(current_char), ord(input_string[i + 1]))))
                i += 1  # skip next character as it's part of the digraph
            else:
                output_string += chr(script_equivalence.get(ord(current_char)))
        elif VeqilharxhiLetter.is_vithkuqi_letter(current_char):
            output_string += AlbanianLetter.unicode_albanian_letter(reverse_equivalence.get(ord(current_char)))
        else:
            output_string += current_char  # leave unrecognized characters unchanged

        i += 1

    return output_string


print(transliterate('Xhorxh W. Bush dhe Bill Klinton shtrënguan duart në mirënjohje.'))
print(transliterate('𐖓𐖮𐖱𐖺 W. 𐕱𐖷𐖴 𐖝𐖞 𐕱𐖥𐖪 𐖁𐖩𐖥𐖬𐖵𐖮𐖬 𐖴𐖵𐖱𐖟𐖬𐖡𐖷𐖗𐖬 𐖜𐖷𐖗𐖱𐖵 𐖬𐖟 𐖫𐖥𐖱𐖟𐖭𐖮𐖣𐖧𐖞.'))
