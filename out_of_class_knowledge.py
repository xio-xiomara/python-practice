#学习sorted、map、filter常用函数
# 为了记得更牢，我将分别解释它们的意义：
# 1、sorted：排序，若没写key=。。。时，他会默认按照“字母顺序”来排,如果加了key=lambda x： len（x)则意味着按单词的长度来排列,reverse=True意味着逆转
# 2、map：把一个函数作用到可迭代对象的每个元素上（例如数列--通讯录）
# 3、filter：筛选作用（例如筛选出数列里大于5的数字）

#题目一：用lambda函数算一个数的平方
square=lambda x:x**2
print(square(3))

#题目二：用map和lambda将列表【1，2，3，4】每个元素都加五，列出新列表
num_list=[1,2,3,4]
num_list_plus_five=map (lambda num:num+5, num_list)#map()返回的是一种“懒加载”的迭代器对象，他不会直接变成列表，所以要用list（）把他转为真实的数据
print(list(num_list_plus_five))

#用filter筛选出大于五的数
num_list=[1,2,3,4,23,22,44,10,43]
num_list_plus_filter=filter(lambda x: x>5,num_list)
print(list(num_list_plus_filter))

#用sorted给单词排序 从短到长
word_list=['banana','apple','orange','soup']
word_list_sorted=sorted(word_list,key=lambda x:len(x),reverse=True)
print(word_list_sorted)

#忽略大小写排序
x=['alice','anna','BOB','Tom']
x_sorted=sorted(x,key=lambda x:x.lower())
print(x_sorted)

# 测试方法
# assertEqual(a, b)                  判断 a == b        self.assertEqual(add(2, 3), 5)
# assertNotEqual(a, b)               判断 a != b        self.assertNotEqual(add(2, 2), 5)
# assertTrue(x)                      判断 x 是真         self.assertTrue(is_valid(7))
# assertFalse(x)                     判断 x 是假         self.assertFalse(is_valid(-1))
# assertIs(a, b)                     判断 a is b        self.assertIs(obj1, obj2)
# assertIsNone(x)                    判断 x 是 None      self.assertIsNone(find_user(0))
# assertIn(a, b)                     判断 a in b         self.assertIn("a", "abc")
# assertRaises(Error, func, *args)   判断是否抛出指定异常   self.assertRaises(ValueError, int, "abc")

# __str__()方法 类里的魔术方法 用法和__init__类似，我觉得跟总结差不多
class ShoppingList:
    def __init__(self,shopping_list):
        self.shopping_list=shopping_list

    def shopping_list_count(self):
        return len(self.shopping_list)    #对公式极度不熟悉,return不记得，len（）也快不记得了

    def shopping_list_total_price(self):
        total = 0
        for price in self.shopping_list.values():
            total +=price
        return  total
    # 还有个最简单的方法就是 return sum(self.shopping_list.values)


    def __str__(self):
        lines=[f'{item}:{price}元'for item,price in self.shopping_list.items()]
        total_line=f'总价：{self.shopping_list_total_price()}元'
        return '\n'.join(lines + [total_line])

    # join（）是一个非常常用的字符串方法，它的作用是：用某个字符把多个字符串“连接”成一个新的字符串。
    # '连接符'.join(可迭代对象)
    # 例子：
    # items=['苹果','香蕉','橘子']
    # result=','.join(items)
    # print(result)
    # 输出结果：苹果,香蕉,橘子

    # 添加商品和移除商品的方法
    def add_item(self,item,price):
        self.shopping_list[item]=price
        print(f'已添加商品：{item}-{price}元')

    def remove_item(self,item):
        # if item in self.shopping_list[item]:  注意self.shopping_list[item]代表的是值
        if item in self.shopping_list:
            del self.shopping_list [item]
            print(f'已删除：{item}')
        else:
            print(f"{item}不在购物清单里")



num_1 = {'洗衣机': 123, '洗发水': 34, '牙刷': 76}
sl = ShoppingList(num_1)
print(sl)
# f-string写法：
# f"{item}:{price}元"
#
# .format()写法
# "{}:{}元".format(item,price)

#又多了个新知识 可恶 我都还没复习完！！！！！
# {:}冒号后面可以指定格式，比如小数点位数、对齐方式、宽度等
# '{:.2}'.format(3.14159)   保留两位小数      3.14
# '{:>10}'.format('hi')    右对齐，占10宽度   '          hi'
# '{:<10}'.format('hi')    左对齐，占10宽度   'hi          '
# '{:^10}'.format('hi')    居中，占10宽度     '     hi     '
# '{:0>5}'.format(42)      补零到5位         '00042'