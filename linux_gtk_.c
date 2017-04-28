//gcc -Wall -o helloworld  hello.c `pkg-config --cflags --libs gtk+-2.0`


#include <gtk/gtk.h>  //gtk程序所需的头文件   
  
int  main(int argc,char *argv[])  
{  
    GtkWidget *window;  //定义一个构件指针   
  
    gtk_init(&argc,&argv);  //初始化GTK环境   
  
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);//新建一个标准的有框架窗口   
  
    gtk_widget_show(window); //显示window   
  
    gtk_main();//启动GTK   
  
    return 1;  
}  
