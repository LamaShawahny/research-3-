# checks if email valid or not
def check_valid_mail(str):
    # we make sure that @ is not repeating and available
    number_of_sh = str.count('@')
    if number_of_sh != 1:
        return False

    # checking the string before @
    prefix = ""
    index = 0
    for ch in str:
        if ch == '@':
            break
        index = index + 1
        prefix += ch

    number_of_sol = prefix.count('#')
    if number_of_sol != 0:
        return False

    asci_ch = ord(prefix[0])
    if not ((48 <= asci_ch <= 57) or (65 <= asci_ch <= 90) or (97 <= asci_ch <= 122)):
        return False

    asci_ch = ord(prefix[len(prefix) - 1])
    if not ((48 <= asci_ch <= 57) or (65 <= asci_ch <= 90) or (97 <= asci_ch <= 122)):
        return False

    for i in range(len(prefix) - 1):
        ch = ord(prefix[i])
        ch1 = ord(prefix[i + 1])
        if not ((48 <= ch <= 57) or (65 <= ch <= 90) or (97 <= ch <= 122)) and (not ((48 <= ch1 <= 57) or (
                65 <= ch1 <= 90) or (97 <= ch1 <= 122))):
            return False

    # checking the string after @
    domain = ""
    num_of_ente = str.count('\n')
    index = index + 1
    while index < len(str) - num_of_ente:
        domain += str[index]
        index = index + 1

    if len(domain) - num_of_ente < 4:
        return False

    for i in range(len(domain) - 1 - num_of_ente):
        ch = ord(domain[i])
        ch1 = ord(domain[i + 1])
        if not ((48 <= ch <= 57) or (65 <= ch <= 90) or (97 <= ch <= 122)) and (not ((48 <= ch1 <= 57) or (
                65 <= ch1 <= 90) or (97 <= ch1 <= 122))):
            return False

    number_of_sol = domain.count('.')
    if number_of_sol != 1:
        return False

    number_of_sol = domain.count('#')
    if number_of_sol != 0:
        return False

    ind2 = 0
    for ch in domain:
        if ch == '.':
            break
        ind2 = ind2 + 1

    dom = ""
    ind2 = ind2 + 1
    while ind2 < len(domain):
        dom += domain[ind2]
        ind2 = ind2 + 1

    if len(dom) < 2:
        return False

    for index2 in range(len(dom) - num_of_ente):
        ch3 = dom[index2]
        asci_ch3 = ord(ch3)
        if not ((65 <= asci_ch3 <= 90) or (97 <= asci_ch3 <= 122)):
            return False

    return True

    # reading the file and classifying into to  lists (valid anf invalid )

def read_file(File_name):
    filepath = File_name
    Vaild = []
    Invalid = []
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if check_valid_mail(line) is True:
                Vaild.append(line.replace("\n", ""))
            else:
                Invalid.append(line.replace("\n", ""))
            line = fp.readline()
            cnt += 1

    print("                                                 Valid mails                ")
    print(Vaild)
    print()
    print("                                                 InValid mails                ")
    print(Invalid)


###

if __name__ == '__main__':
    read_file("ReadFile")
