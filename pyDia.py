#coding=utf-8
import  xml.dom.minidom
#打开xml文档
dom = xml.dom.minidom.parse('file.xml')

#得到文档元素对象
root = dom.documentElement

cc=dom.getElementsByTagName('rawtext')
c1=cc[0]
print c1.firstChild.data
##out 打电话

##file.xml

<?xml version='1.0' encoding='utf-8' standalone='yes' ?><nlp>
  <version>1.1</version>
  <rawtext>打电话</rawtext>
  <confidence>76</confidence>
  <engine>local</engine>
  <result>
    <focus>打电话</focus>
    <confidence>84</confidence>
    <object>
      <打电话 id="10001">打电话</打电话>
    </object>
  </result>
</nlp>
