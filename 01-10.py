print('Вы находитесь в комнате на развилке. Вы можете пойти "налево", "направо" или "прямо". Введите одно из слов\
 в кавычках для выбора.')
x = input()
print('Вы направились '+x+'. Через некоторое время вы дошли до двух дверей. Вы выберете "левую" или "правую"?')
y = input()
print('Вы смело открыли '+y+' дверь. ')
if y == 'левую':
    print('Но за ней вас подстерегала гигантская подземная жаба, которая проглотила вас целиком!')
elif y == 'правую':
    print('За ней находится мешок с золотом!')

