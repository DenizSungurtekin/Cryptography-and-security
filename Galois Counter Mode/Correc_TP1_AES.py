# Here's the S-boxes as tuples. You can change their form if you prefer to
# work with lists or other structures.

S_box = (
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
            )
S_box_inv = (
            0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
            )

MixColMatrix = [[0x02,0x03,0x01,0x01],
                [0x01,0x02,0x03,0x01],
                [0x01,0x01,0x02,0x03],
                [0x03,0x01,0x01,0x02]]

MixColInverse = [[0x0e,0x0b,0x0d,0x09],
                [0x09,0x0e,0x0b,0x0d],
                [0x0d,0x09,0x0e,0x0b],
                [0x0b,0x0d,0x09,0x0e]]


# Applies the S-Box on 32 bit blocks (lists of 4 bytes)
def Sbox(lst,box):
    result = [box[lst[0]],box[lst[1]],box[lst[2]],box[lst[3]]]
    return result



# xor on two lists of 4 bytes
def xor_lst(lst1,lst2):
    result = []
    for i in range(4):
        result.append(lst1[i] ^ lst2[i])
    return result

# Polynomial product in GF(2^8), with irreductible polynomial x^8+x^4+x^3+x+1
def poly_multiplication(p1,p2):
    liste_p1 = list(str(bin(p1))[2:])
    res = 0
    degrep1 = len(liste_p1)-1
    for i in range(degrep1+1):
        if liste_p1[i] == '1':
            temp = p2 * pow(2,degrep1-i)
            res = res ^ temp
    while res > 255:
        bigger_byte = res // 256
        lesser_byte = res % 256
        poly = 0b11011
        res = lesser_byte ^ poly_multiplication(bigger_byte,poly)
    return res


# Key expansion step, returns a list of keys (each key will be composed of four
# lists of 4 bytes). The given key is either 4x4, 6x4 or 8x4 bytes.

def key_expansion(key,box):
    N = len(key)
    if len(key) == 4:
        steps = 10
    elif len(key) == 6:
        steps = 12
    elif len(key) == 8:
        steps = 14
    else:
        raise ValueError("Invalid Key Length")
        
    
    rc_table = [0b00000001, 0b00000010 , 0b00000100 ,
                  0b00001000, 0b00010000 , 0b00100000 ,
                  0b01000000, 0b10000000 , 0b00011011 ,
                  0b00110110]
    rcon_table = []

    for i in range(10):
        rcon_table.append([rc_table[i], 0b0, 0b0, 0b0])
    Expanded_Key = []

    for i in range(N):
        Expanded_Key.append(key[i])

    for i in range(N,4*(steps+1)):
        if i % N == 0:
            rotated = Expanded_Key[i-1][1:] + [Expanded_Key[i-1][0]]
            Expanded_Key.append(xor_lst(xor_lst(Expanded_Key[i-N],
                                           Sbox(rotated,box)),rcon_table[int(i/N)-1]))
        elif N > 6 and i % N == 4:
            Expanded_Key.append(xor_lst(Expanded_Key[i-N],Sbox(Expanded_Key[i-1],box)))
        else:
            Expanded_Key.append(xor_lst(Expanded_Key[i-N],Expanded_Key[i-1]))

    return Expanded_Key


# ByteSub operation on a 4x4 matrix of bytes.
def ByteSub(matrix,sub_box):
    result = []
    for i in range(4):
        result.append(Sbox(matrix[i],sub_box))
    return result

# ShiftRow operation on a 4x4 matrix of bytes.
def ShiftRow(matrix, encrypt):
    if encrypt == True :
        row1 = [matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3]]
        row2 = [matrix[1][0],matrix[2][1],matrix[3][2],matrix[0][3]]
        row3 = [matrix[2][0],matrix[3][1],matrix[0][2],matrix[1][3]]
        row4 = [matrix[3][0],matrix[0][1],matrix[1][2],matrix[2][3]]
    else:
        row1 = [matrix[0][0],matrix[3][1],matrix[2][2],matrix[1][3]]
        row2 = [matrix[1][0],matrix[0][1],matrix[3][2],matrix[2][3]]
        row3 = [matrix[2][0],matrix[1][1],matrix[0][2],matrix[3][3]]
        row4 = [matrix[3][0],matrix[2][1],matrix[1][2],matrix[0][3]]
        
    result = [row1,row2,row3,row4]
    return result



# Vector Multiplication with polynomial multiplication for lists of 4 bytes,
# Returns an integer value (Addition is also polynomial).
def Vector_poly_multi(polylst,polylst2):
    result = 0
    for i in range(4):
        temp = poly_multiplication(polylst[i],polylst2[i])
        result = result ^ temp
    return result


# MixColumn operation on a 4x4 matrix of bytes.
# We have to work with column instead of rows here, so we have to build the
# columns first
def MixColumn(matrix, mixcol):
    result = [[],[],[],[]]
    # Recuperation of the adequate column
    for i in range(4):
        col = matrix[i]
        # Matrix multiplication, multiplies each time the corresponding row of
        # MixCol with the column of values.
        for j in range(4):
            result[i].append(Vector_poly_multi(mixcol[j],col))
    return result


# AddRoundKey operation on a 4x4 matrix of bytes.
def AddRoundKey(matrix,sub_key):
    result = []
    for i in range(4):
        result.append(xor_lst(matrix[i],sub_key[i]))
    return result

# Changes any message in a vector of 32-bit words, i.e. a matrix of bytes 4xN.
# In particular, this means a key will already be organised as words,
# And a 128 bit message will already we a 4x4 matrix of bytes.
# A byte is here just an integer value between 0 and 255.
def MessageToMatrix(string):
    longueur = len(string)
    matrice = []
    for i in range(longueur):
        byte = ord(string[i])
        if i % 4 == 0:
            matrice.append([byte])
        else:
            matrice[-1].append(byte)
    return matrice

# Vice-versa : transforms a matrix 4xN of bytes into a string.
def MatrixToMessage(matrice):
    string = ""
    for word in matrice:
        for j in range(4):
            string += chr(word[j])
    return string


# FINAL AES FUNCTION :
def AES(message,key,S_box, mixcol):
    message = MessageToMatrix(message)
    key = MessageToMatrix(key)
    All_Keys = key_expansion(key,S_box)
    Init_Key = All_Keys[0:4]

    # First xor
    message = AddRoundKey(message,Init_Key)
    
    N = len(key)
    if N == 4:
        steps = 10
    elif N == 6:
        steps = 12
    elif N == 8 :
        steps = 14
    else:
        raise ValueError("Invalid Key Length")
        
    for i in range(1,steps+1):
        next_key = All_Keys[4*i:4*(i+1)]
        message = ByteSub(message,S_box)
        message = ShiftRow(message, True)
        if i < steps:
            message = MixColumn(message, mixcol)
        message = AddRoundKey(message, next_key)


    message = MatrixToMessage(message)
    return message


# AES Decryption :
def AES_Inv(message,key,S_box, S_box_Inv, mixcol):
    message = MessageToMatrix(message)
    key = MessageToMatrix(key)
    All_Keys = key_expansion(key,S_box)
    Init_Key = All_Keys[0:4]

    
    
    N = len(key)
    if N == 4:
        steps = 10
    elif N == 6:
        steps = 12
    elif N == 8 :
        steps = 14
    else:
        raise ValueError("Invalid Key Length")
        
    for i in range(steps,0,-1):
        next_key = All_Keys[4*i:4*(i+1)]
        message = AddRoundKey(message, next_key)
        if i < steps:
            message = MixColumn(message, mixcol)
        message = ShiftRow(message, False)
        message = ByteSub(message,S_box_Inv)

    # Reverse the First xor
    message = AddRoundKey(message,Init_Key)

    message = MatrixToMessage(message)
    return message



message = "Two One Nine Two"
key = "Thats my Kung Fu"
#print(MessageToMatrix(message))

#ciphertext = AES(message,key,S_box,MixColMatrix)


#plaintext = AES_Inv(ciphertext, key, S_box, S_box_inv, MixColInverse)
#print(message)
#print(ciphertext)
#print(plaintext)

# This only does the minimum needed for TP2 : an AES_Box which uses blocks of
# 16 characters (i.e. 128 bits). To do exactly what was asked for TP1, it
# misses the part where you need to cut the message into 128 bits blocks.


