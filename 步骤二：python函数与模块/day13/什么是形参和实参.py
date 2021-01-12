#什么是形参和实参
#定义一个函数
def print_verse(verse_name,is_show_title,is_show_dynasty):
    if verse_name == "静夜思":
        if is_show_title == True:
            print("静夜思")
        if is_show_dynasty == True:
            print("唐朝-李白")
        print("床前明月光")
        print("疑是地上霜")
        print("举头望明月")
        print("低头思故乡")

    elif verse_name == "枫桥夜泊":
        if is_show_title == False:
            print("枫桥夜泊")
        if is_show_dynasty == True:
            print("唐朝-张继")
        print("月落乌啼霜满天")
        print("江枫渔火对愁眠")
        print("姑苏城外寒山寺")
        print("夜半钟声到客船")

print_verse("枫桥夜泊",True,True)
print_verse("静夜思",True,True)

