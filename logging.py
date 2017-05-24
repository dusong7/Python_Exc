一、通过向日志记录函数传递一个extra参数引入上下文信息
前面我们提到过，可以通过向日志记录函数传递一个extra参数来实现向日志输出中添加额外的上下文信息，如：

import logging
import sys

fmt = logging.Formatter("%(asctime)s - %(name)s - %(ip)s - %(username)s - %(message)s")
h_console = logging.StreamHandler(sys.stdout)
h_console.setFormatter(fmt)
logger = logging.getLogger("myPro")
logger.setLevel(logging.DEBUG)
logger.addHandler(h_console)

extra_dict = {"ip": "113.208.78.29", "username": "Petter"}
logger.debug("User Login!", extra=extra_dict)

extra_dict = {"ip": "223.190.65.139", "username": "Jerry"}
logger.info("User Access!", extra=extra_dict)
输出：

2017-05-14 15:47:25,562 - myPro - 113.208.78.29 - Petter - User Login!
2017-05-14 15:47:25,562 - myPro - 223.190.65.139 - Jerry - User Access!
但是用这种方式来传递信息并不是那么方便，因为每次调用日志记录方法都要传递一个extra关键词参数。即便没有需要插入的上下文信息也是如此，因为该logger设置的formatter格式中指定的字段必须要存在。所以，我们推荐使用下面两种方式来实现上下文信息的引入。

也许可以尝试在每次创建连接时都创建一个Logger实例来解决上面存在的问题，但是这显然不是一个好的解决方案，因为这些Logger实例并不会进行垃圾回收。尽管这在实践中不是个问题，但是当Logger数量变得不可控将会非常难以管理。

二、使用LoggerAdapters引入上下文信息
使用LoggerAdapter类来传递上下文信息到日志事件的信息中是一个非常简单的方式，可以把它看做第一种实现方式的优化版--因为它为extra提供了一个默认值。这个类设计的类似于Logger，因此我们可以像使用Logger类的实例那样来调用debug(), info(), warning(),error(), exception(), critical()和log()方法。当创建一个LoggerAdapter的实例时，我们需要传递一个Logger实例和一个包含上下文信息的类字典对象给该类的实例构建方法。当调用LoggerAdapter实例的一个日志记录方法时，该方法会在对日志日志消息和字典对象进行处理后，调用构建该实例时传递给该实例的logger对象的同名的日志记录方法。下面是LoggerAdapter类中几个方法的定义：

class LoggerAdapter(object):
    """
    An adapter for loggers which makes it easier to specify contextual
    information in logging output.
    """

    def __init__(self, logger, extra):
        """
        Initialize the adapter with a logger and a dict-like object which
        provides contextual information. This constructor signature allows
        easy stacking of LoggerAdapters, if so desired.

        You can effectively pass keyword arguments as shown in the
        following example:

        adapter = LoggerAdapter(someLogger, dict(p1=v1, p2="v2"))
        """
        self.logger = logger
        self.extra = extra
    
    def process(self, msg, kwargs):
        """
        Process the logging message and keyword arguments passed in to
        a logging call to insert contextual information. You can either
        manipulate the message itself, the keyword args or both. Return
        the message and kwargs modified (or not) to suit your needs.

        Normally, you'll only need to override this one method in a
        LoggerAdapter subclass for your specific needs.
        """
        kwargs["extra"] = self.extra
        return msg, kwargs
        
    def debug(self, msg, *args, **kwargs):
        """
        Delegate a debug call to the underlying logger, after adding
        contextual information from this adapter instance.
        """
        msg, kwargs = self.process(msg, kwargs)
        self.logger.debug(msg, *args, **kwargs)
通过分析上面的代码可以得出以下结论：

上下文信息是在LoggerAdapter类的process()方法中被添加到日志记录的输出消息中的，如果要实现自定义需求只需要实现LoggerAdapter的子类并重写process()方法即可；
process()方法的默认实现中，没有修改msg的值，只是为关键词参数插入了一个名为extra的 key，这个extra的值为传递给LoggerAdapter类构造方法的参数值；
LoggerAdapter类构建方法所接收的extra参数，实际上就是为了满足logger的formatter格式要求所提供的默认上下文信息。
关于上面提到的第3个结论，我们来看个例子：

import logging
import sys


# 初始化一个要传递给LoggerAdapter构造方法的logger实例
fmt = logging.Formatter("%(asctime)s - %(name)s - %(ip)s - %(username)s - %(message)s")
h_console = logging.StreamHandler(sys.stdout)
h_console.setFormatter(fmt)
init_logger = logging.getLogger("myPro")
init_logger.setLevel(logging.DEBUG)
init_logger.addHandler(h_console)

# 初始化一个要传递给LoggerAdapter构造方法的上下文字典对象
extra_dict = {"ip": "IP", "username": "USERNAME"}

# 获取一个LoggerAdapter类的实例
logger = logging.LoggerAdapter(init_logger, extra_dict)

# 应用中的日志记录方法调用
logger.info("User Login!")
logger.info("User Login!", extra={"ip": "113.208.78.29", "username": "Petter"})
logger.extra = {"ip": "113.208.78.29", "username": "Petter"}
logger.info("User Login!")
logger.info("User Login!")
输出结果：

# 使用extra默认值：{"ip": "IP", "username": "USERNAME"}
2017-05-14 17:23:15,148 - myPro - IP - USERNAME - User Login!

# info(msg, extra)方法中传递的extra方法没有覆盖默认值
2017-05-14 17:23:15,148 - myPro - IP - USERNAME - User Login!

# extra默认值被修改了
2017-05-14 17:23:15,148 - myPro - 113.208.78.29 - Petter - User Login!
2017-05-14 17:23:15,148 - myPro - 113.208.78.29 - Petter - User Login!
根据上面的程序输出结果，我们会发现一个问题：传递给LoggerAdapter类构造方法的extra参数值不能被LoggerAdapter实例的日志记录函数（如上面调用的info()方法）中的extra参数覆盖，只能通过修改LoggerAdapter实例的extra属性来修改默认值（如上面使用的logger.extra=xxx），但是这也就意味着默认值被修改了。

解决这个问题的思路应该是：实现一个LoggerAdapter的子类，重写process()方法。其中对于kwargs参数的操作应该是先判断其本身是否包含extra关键字，如果包含则不使用默认值进行替换；如果kwargs参数中不包含extra关键字则取默认值。来看具体实现：

import logging
import sys

class MyLoggerAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        if 'extra' not in kwargs:
            kwargs["extra"] = self.extra
        return msg, kwargs

if __name__ == '__main__':
    # 初始化一个要传递给LoggerAdapter构造方法的logger实例
    fmt = logging.Formatter("%(asctime)s - %(name)s - %(ip)s - %(username)s - %(message)s")
    h_console = logging.StreamHandler(sys.stdout)
    h_console.setFormatter(fmt)
    init_logger = logging.getLogger("myPro")
    init_logger.setLevel(logging.DEBUG)
    init_logger.addHandler(h_console)
    
    # 初始化一个要传递给LoggerAdapter构造方法的上下文字典对象
    extra_dict = {"ip": "IP", "username": "USERNAME"}
    
    # 获取一个自定义LoggerAdapter类的实例
    logger = MyLoggerAdapter(init_logger, extra_dict)
    
    # 应用中的日志记录方法调用
    logger.info("User Login!")
    logger.info("User Login!", extra={"ip": "113.208.78.29", "username": "Petter"})
    logger.info("User Login!")
    logger.info("User Login!")
输出结果：

# 使用extra默认值：{"ip": "IP", "username": "USERNAME"}
2017-05-22 17:35:38,499 - myPro - IP - USERNAME - User Login!

# info(msg, extra)方法中传递的extra方法已覆盖默认值
2017-05-22 17:35:38,499 - myPro - 113.208.78.29 - Petter - User Login!

# extra默认值保持不变
2017-05-22 17:35:38,499 - myPro - IP - USERNAME - User Login!
2017-05-22 17:35:38,499 - myPro - IP - USERNAME - User Login!
OK！ 问题解决了。

其实，如果我们想不受formatter的限制，在日志输出中实现自由的字段插入，可以通过在自定义LoggerAdapter的子类的process()方法中将字典参数中的关键字信息拼接到日志事件的消息中。很明显，这些上下文中的字段信息在日志输出中的位置是有限制的。而使用'extra'的优势在于，这个类字典对象的值将被合并到这个LogRecord实例的__dict__中，这样就允许我们通过Formatter实例自定义日志输出的格式字符串。这虽然使得上下文信息中的字段信息在日志输出中的位置变得与内置字段一样灵活，但是前提是传递给构造器方法的这个类字典对象中的key必须是确定且明了的。

三、使用Filters引入上下文信息
另外，我们还可以使用自定义的Filter.Filter实例的方式，在filter(record)方法中修改传递过来的LogRecord实例，把要加入的上下文信息作为新的属性赋值给该实例，这样就可以通过指定formatter的字符串格式来输出这些上下文信息了。

我们模仿上面的实现，在传递个filter(record)方法的LogRecord实例中添加两个与当前网络请求相关的信息：ip和username。

import logging
from random import choice


class ContextFilter(logging.Filter):

        ip = 'IP'
        username = 'USER'

        def filter(self, record):
            record.ip = self.ip
            record.username = self.username
            return True

if __name__ == '__main__':
    levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    users = ['Tom', 'Jerry', 'Peter']
    ips = ['113.108.98.34', '219.238.78.91', '43.123.99.68']

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(name)-5s %(levelname)-8s %(ip)-15s %(username)-8s %(message)s')
    logger = logging.getLogger('myLogger')
    f = ContextFilter()
    logger.addFilter(f)
    logger.debug('A debug message')
    logger.info('An info message with %s', 'some parameters')

    for x in range(5):
        lvl = choice(levels)
        lvlname = logging.getLevelName(lvl)
        filter.ip = choice(ips)
        filter.username = choice(users)
        logger.log(lvl, 'A message at %s level with %d %s', lvlname, 2, 'parameters')
输出结果：

2017-05-15 10:21:49,401 myLogger DEBUG    IP              USER     A debug message
2017-05-15 10:21:49,401 myLogger INFO     IP              USER     An info message with some parameters
2017-05-15 10:21:49,401 myLogger INFO     219.238.78.91   Tom      A message at INFO level with 2 parameters
2017-05-15 10:21:49,401 myLogger INFO     219.238.78.91   Peter    A message at INFO level with 2 parameters
2017-05-15 10:21:49,401 myLogger DEBUG    113.108.98.34   Jerry    A message at DEBUG level with 2 parameters
2017-05-15 10:21:49,401 myLogger CRITICAL 43.123.99.68    Tom      A message at CRITICAL level with 2 parameters
2017-05-15 10:21:49,401 myLogger INFO     43.123.99.68    Jerry    A message at INFO level with 2 parameters
