#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <qmessagebox.h>
#include <stdlib.h>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_ShellRun_clicked()
{
    QMessageBox::about(NULL,"","runCommand");
    system("gnome-terminal -e runCommand");
}

void MainWindow::on_keyBoardRun_clicked()
{
    QString showMsg = "299";

    QMessageBox::about(NULL,"About",showMsg);
}

void MainWindow::on_AMClRun_clicked()
{
    QMessageBox::aboutQt(NULL,"AboutMessage");
}
//  system("gnome-terminal -x bash -c \'ls -la;exec bash\'");
//system("gnome-terminal -x bash -c \'./listDir.sh;exec bash\'");
