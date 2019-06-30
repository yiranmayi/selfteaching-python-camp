text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#统计单词出现的次数
textlist1=text.split()
textlist2 = []             #表示定义一个列表，列表推导用方括号（“[]”）括起来
for i in textlist1:              #对textlist1中的每个i都进行检测
    if i.isalpha():               #如果i是字母，则添加i到原来列表textlist2的最后。
        textlist2.append(i)      #去除非单词
print(textlist2)
