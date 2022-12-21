def answers_from(answers):
    ANS_COUNT = 11

    data = [0]*ANS_COUNT
    for i, ans in enumerate(answers):
        if ans.lower() == "да":
            data[(i%ANS_COUNT)-1] += 1
    
    skills = [
            "Cпособность управлять собой",
            "Чёткие ценности",
            "Чёткие личные цели", "Продолжающееся саморазвитие",
            "Хорошие навыки решения проблем",
            "Творческий подход",
            "Умение влиять на окружающих",
            "Понимание особенностей управленческого труда",
            "Способность руководить",
            "Умение обучать",
            "Cпособность управлять собой",
    ]

    indexs = list(range(ANS_COUNT))
    for i in range(1, ANS_COUNT):
        c = 0
        j = i
        while j > 0 and data[j-1] > data[j]:
            c += 1
            tmp = data[j]
            data[j] = data[j-1]
            data[j-1] = tmp
            j -= 1
        indexs.pop(i)
        indexs.insert(i-c,  i)

    otvet = "Сильные стороны: "
    for i in indexs[-3:]:
        otvet += skills[i].lower() + ', '
    otvet = otvet[:len(otvet)-2] + '.\n'
    otvet += "\nСлабые стороны: "
    for i in indexs[:3]:
        otvet += skills[i].lower() + ', '
    otvet = otvet[:len(otvet)-2] + '.'

    return otvet


if __name__ == "__main__":
    print(answers_from(['да']))
