# https://www.hidglobal.com/sites/default/files/resource_files/6090-905-f_0_1-pivclass-fips-201-reader-operation-and-output-selections.pdf

def convert_hex_to_binary(hex_string):
    #convert hexidecimal to respective 4 bits
    bit_group_list = []
    for c in reversed("0" + hex_string):
        formatted_bits = "{0:04b}".format(int(c,16))
        bit_group_list.append(formatted_bits)

    print("hex bit list") 
    print(bit_group_list)
    #convert 4-bit list to bytes
    byte_list = []
    for i, j in zip(*[bit_group_list[n::2] for n in [1,0]]):
        byte_list.append(i+j)
    
    print("bytes list")
    print(byte_list)

    return "".join(reversed(byte_list))


def convert_hid_bcd_to_digit(bcd):
    cluster_switch = {
        "00001": 0,
        "10000": 1,
        "01000": 2,
        "11001": 3,
        "00100": 4,
        "10101": 5,
        "01101": 6,
        "11100": 7,
        "00010": 8,
        "10011": 9,
        "11010": "SS",
        "10110": "FS",
        "11111": "ES"
    }
    return cluster_switch.get(bcd, "Invalid")

def convert_binary_to_bcd_clusters(binary_string):
    bcd_list = []
    for startIndex in range(0, len(binary_string), 5):
        bcd_cluster = binary_string[startIndex:(startIndex+5)]
        bcd_list.append(bcd_cluster)
    return bcd_list

def convert_hid_bcd_clusters_to_characters(bcd_list):
    char_list = []
    for bcd in bcd_list:
        hid_char = convert_hid_bcd_to_digit(bcd)
        char_list.append(hid_char)
    return char_list

def validate_bcd_cluster(data, expected):
    if(data != expected):
        raise ValueError("Expected " + expected)

def get_fascn_data(hex_value):
    print("\nHex value:\n" + hex_value)

    binary_string = convert_hex_to_binary(hex_value)
    print("\nBinary value:\n" + binary_string)

    bcd_list = convert_binary_to_bcd_clusters(binary_string)
    print("\nHID Binary cluster list:\n")
    print(bcd_list)

    hid_char_list = convert_hid_bcd_clusters_to_characters(bcd_list)
    print("\nHID data character list:\n")
    print(hid_char_list)

    validate_bcd_cluster(hid_char_list[0], 'SS') # data should start with an HID Start Sentinel

    agency_code = "".join(str(x) for x in hid_char_list[1:5])
    print("\nFASCN Agency Code:\n")
    print(agency_code)

    validate_bcd_cluster(hid_char_list[5], 'FS') # expect HID field separator

    system_code = "".join(str(x) for x in hid_char_list[6:10])
    print("\nFASCN System Code:\n")
    print(system_code)

    validate_bcd_cluster(hid_char_list[10], 'FS') # expect HID field separator    

    credential = "".join(str(x) for x in hid_char_list[11:17])
    print("\nFASCN Credential Number:\n")
    print(credential)

    return agency_code + system_code + credential


value1 = "D70339DA15256C10843C45A16858210D5B3CCC90870339A3FF"
result1 = get_fascn_data(value1)
print("\n Input 1: " + value1)
print("Output 1: " + result1)
print("Expected: 70991545000072")

# value2 = "D70339DAA108AC120790CDA16858210D5B3CCC90870339A3F9"
# result2 = get_fascn_data(value2)
# print("\n Input 2: " + value2)
# print("Output 2: " + result2)
# print("Expected: 70995008040713")

# value3 = "D70339DAA108AC18343C45A16458210C262986A2870339A3E8"
# result3 = get_fascn_data(value3)
# print("\n Input 3: " + value3)
# print("Output 3: " + result3)
# print("Expected: 70995008016072")