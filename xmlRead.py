<?xml version="1.0" encoding="utf-8"?>
<catalog>
    <maxid>4</maxid>
    <login username="pytest" passwd='123456'>
        <caption>Python</caption>
        <item id="4">
            <caption>测试</caption>
        </item>
    </login>
    <item id="2">
        <caption>Zope</caption>
    </item>
</catalog>

#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('file1.xml')

#得到文档元素对象
root = dom.documentElement

itemlist = root.getElementsByTagName('login')
item = itemlist[0]
un=item.getAttribute("username")
print un
pd=item.getAttribute("passwd")
print pd

ii = root.getElementsByTagName('item')
i1 = ii[0]
i=i1.getAttribute("id")
print i

i2 = ii[1]
i=i2.getAttribute("id")
print i

# pytest
# 123456
# 4
# 2


#coding=utf-8
import  xml.dom.minidom
#打开xml文档
dom = xml.dom.minidom.parse('file1.xml')

#得到文档元素对象
root = dom.documentElement

cc=dom.getElementsByTagName('caption')
c1=cc[0]
print c1.firstChild.data

c2=cc[1]
print c2.firstChild.data

c3=cc[2]
print c3.firstChild.data
##Python
##测试
##Zope





 
　　关于python读取xml文章很多，但大多文章都是贴一个xml文件，然后再贴个处理文件的代码。这样并不利于初学者的学习，希望这篇文章可以更通俗易懂的教如何使用python 来读取xml 文件。

 

什么是xml？

xml即可扩展标记语言，它可以用来标记数据、定义数据类型，是一种允许用户对自己的标记语言进行定义的源语言。

abc.xml

复制代码
<?xml version="1.0" encoding="utf-8"?>
<catalog>
    <maxid>4</maxid>
    <login username="pytest" passwd='123456'>
        <caption>Python</caption>
        <item id="4">
            <caption>测试</caption>
        </item>
    </login>
    <item id="2">
        <caption>Zope</caption>
    </item>
</catalog>
复制代码
Ok ,从结构上，它很像我们常见的HTML超文本标记语言。但他们被设计的目的是不同的，超文本标记语言被设计用来显示数据，其焦点是数据的外观。它被设计用来传输和存储数据，其焦点是数据的内容。

那么它有如下特征：

首先，它是有标签对组成，<aa></aa>

标签可以有属性：<aa id=’123’></aa>

标签对可以嵌入数据：<aa>abc</aa>

标签可以嵌入子标签（具有层级关系）：

<aa>

     <bb></bb>

</aa>

 

获得标签属性

 

那么，下面来介绍如何用python来读取这种类型的文件。

复制代码
#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE
复制代码
mxl.dom.minidom 模块被用来处理xml文件，所以要先引入。

xml.dom.minidom.parse() 用于打开一个xml文件，并将这个文件对象dom变量。

documentElement 用于得到dom对象的文档元素，并把获得的对象给root

每一个结点都有它的nodeName，nodeValue，nodeType属性。

nodeName为结点名字。

nodeValue是结点的值，只对文本结点有效。

nodeType是结点的类型。catalog是ELEMENT_NODE类型

现在有以下几种：

'ATTRIBUTE_NODE'
'CDATA_SECTION_NODE'
'COMMENT_NODE'
'DOCUMENT_FRAGMENT_NODE'
'DOCUMENT_NODE'
'DOCUMENT_TYPE_NODE'
'ELEMENT_NODE'
'ENTITY_NODE'
'ENTITY_REFERENCE_NODE'
'NOTATION_NODE'
'PROCESSING_INSTRUCTION_NODE'
'TEXT_NODE'

NodeTypes - 有名常数

http://www.w3school.com.cn/xmldom/dom_nodetype.asp

 

 

获得子标签

 

现在要获得catalog的子标签以的标签name

复制代码
<?xml version="1.0" encoding="utf-8"?>
<catalog>
       <maxid>4</maxid>
       <login username="pytest" passwd='123456'>
            　　<caption>Python</caption>
             <item id="4">
                    <caption>测试</caption>
            </item>
    </login>
    <item id="2">
            <caption>Zope</caption>
    </item>
</catalog>
复制代码
对于知道元素名字的子元素，可以使用getElementsByTagName方法获取：

复制代码
#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement

bb = root.getElementsByTagName('maxid')
b= bb[0]
print b.nodeName

bb = root.getElementsByTagName('login')
b= bb[0]
print b.nodeName
复制代码
如何区分相同标签名字的标签：

复制代码
<?xml version="1.0" encoding="utf-8"?>
<catalog>
       <maxid>4</maxid>
       <login username="pytest" passwd='123456'>
            　　<caption>Python</caption>
             <item id="4">
                    <caption>测试</caption>
            </item>
    </login>
    <item id="2">
            <caption>Zope</caption>
    </item>
</catalog>
复制代码
<caption>和<item>标签不止一个如何区分？

复制代码
#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement

bb = root.getElementsByTagName('caption')
b= bb[2]
print b.nodeName

bb = root.getElementsByTagName('item')
b= bb[1]
print b.nodeName
复制代码
root.getElementsByTagName('caption') 获得的是标签为caption 一组标签，b[0]表示一组标签中的第一个；b[2] ，表示这一组标签中的第三个。

 

 

获得标签属性值

 

复制代码
<?xml version="1.0" encoding="utf-8"?>
<catalog>
       <maxid>4</maxid>
       <login username="pytest" passwd='123456'>
            　　<caption>Python</caption>
             <item id="4">
                    <caption>测试</caption>
            </item>
    </login>
    <item id="2">
            <caption>Zope</caption>
    </item>
</catalog>
复制代码
<login>和<item>标签是有属性的，如何获得他们的属性？

复制代码
#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement

itemlist = root.getElementsByTagName('login')
item = itemlist[0]
un=item.getAttribute("username")
print un
pd=item.getAttribute("passwd")
print pd

ii = root.getElementsByTagName('item')
i1 = ii[0]
i=i1.getAttribute("id")
print i

i2 = ii[1]
i=i2.getAttribute("id")
print i
复制代码
getAttribute方法可以获得元素的属性所对应的值。

 

 

获得标签对之间的数据

 

复制代码
<?xml version="1.0" encoding="utf-8"?>
<catalog>
       <maxid>4</maxid>
       <login username="pytest" passwd='123456'>
            　　<caption>Python</caption>
             <item id="4">
                    <caption>测试</caption>
            </item>
    </login>
    <item id="2">
            <caption>Zope</caption>
    </item>
</catalog>
复制代码
<caption>标签对之间是有数据的，如何获得这些数据？

获得标签对之间的数据有多种方法，

方法一

复制代码
#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abc.xml')

#得到文档元素对象
root = dom.documentElement

cc=dom.getElementsByTagName('caption')
c1=cc[0]
print c1.firstChild.data

c2=cc[1]
print c2.firstChild.data

c3=cc[2]
print c3.firstChild.data
复制代码
firstChild 属性返回被选节点的第一个子节点，.data表示获取该节点人数据。

 

 

方法二

复制代码
#coding=utf-8
from xml.etree import ElementTree as ET
per=ET.parse('abc.xml')
p=per.findall('./login/item')

for oneper in p:
    for child in oneper.getchildren():
        print child.tag,':',child.text


p=per.findall('./item')

for oneper in p:
    for child in oneper.getchildren():
        print child.tag,':',child.text
复制代码
方法二有点复杂，所引用模块也与前面的不一样，findall用于指定在哪一级标签下开始遍历。

getchildren方法按照文档顺序返回所有子标签。并输出标签名（child.tag）和标签的数据（child.text）


