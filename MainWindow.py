#! /usr/bin/env python3

#******************************************************************************
# Insert licence here!



#******************************************************************************

from sys import exit #input一些包

from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter
from PySide2.QtWidgets import QMenuBar, QMenu, QAction
from PySide2.QtWidgets import QToolBar
from PySide2.QtWidgets import QStatusBar #这几行就是一些零部件用到GUI上面

from ItemTree import * #用到了这个 importItemTree 也行


from PySide2.QtWidgets import QFileDialog   #导入一下QFileDialog这个包 从PYSIDE2里挑出来
import os #系统导入一下
import ItemTree  #需要用到itemtree上面的方法
#******************************************************************************

class MainWindow(QMainWindow): #包里的Q。。。继承到mainwindow
    """
    Main application window
    :version:
    :author: pir
    """

   #--------------------------------------------------------------------------

    def __init__(self):       #设计UI界面 先运行init 初始化
        super().__init__()

        self.setWindowTitle("Organiser")
        self.mainLayout = QVBoxLayout()

        self.cwd = os.getcwd()                   # 获取当前程序文件位置 上面有import os

        
        # Create menu bar & menus
        self.fileMenu = self.menuBar().addMenu("&File") #建一个file菜单 menubar自带的 File是名字


        self.createNewNoteMenuAction = self.fileMenu.addAction("&Create New Note") #一般第一个字母小写 后面大写 驼峰法
        self.createNewNoteMenuAction.triggered.connect(self.on_create_new_note_action)        #这里命名方法用下划线

        self.openMenuAction = self.fileMenu.addAction("&Open") #在一级菜单file加上一个
        self.openMenuAction.triggered.connect(self.on_open_action)    # New-style connect! trigger 到后面的function
        
        self.saveMenuAction = self.fileMenu.addAction("&Save")
        self.saveMenuAction.triggered.connect(self.on_save_action)        #on 表示鼠标点在了按键上
        
        self.saveAsMenuAction = self.fileMenu.addAction("&Save as")
        self.saveAsMenuAction.triggered.connect(self.on_save_as_action)        #on 表示鼠标点在了按键上
        self.fileMenu.addSeparator()#open 和 设置之间的分割线
        
        #缺少设置打开以上功能的弹窗QFileDialog

        self.setPreferencesMenuAction = self.fileMenu.addAction("&Set Preferences")
        self.setPreferencesMenuAction.triggered.connect(self.on_set_preferences_action)        
        self.fileMenu.addSeparator()



        self.quitMenuAction = self.fileMenu.addAction("&Quit") #这些二级菜单都是加在filemenu里面的
        self.quitMenuAction.triggered.connect(self.on_quit_action)
        
        
        # Create main toolbar //加号什么的
        self.mainToolBar = QToolBar() #调用本来就有的
        self.mainToolBar.setMovable(False) #不能移动bar上面的东西
        
        self.addItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-add.svg"), "Insert new item")  # Icons from https://commons.wikimedia.org/wiki/GNOME_Desktop_icons
        self.addItemToolButton.triggered.connect(self.on_insert_item_action)      
        
        self.addChildItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-add-child.svg"), "Insert child item")
        self.addChildItemToolButton.triggered.connect(self.on_insert_child_item_action)      
        
        #TODO 删除的图标需要改一下！！！！！！！！！！！！！！！！！
        self.deleteItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-add.svg"), "Delete item")  
        self.deleteItemToolButton.triggered.connect(self.on_delete_item)
        
        #TODO 编辑的图标需要改一下！！！！！！！！！！！！！！！！！
        self.editItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-add.svg"), "Edit item")
        self.editItemToolButton.triggered.connect(self.on_edit_item)
        
        
        self.mainLayout.addWidget(self.mainToolBar) #按钮trigger到相应的function上
#上面这句话是打包到layout上

        # Configure window splitter
        self.splitter = QSplitter()
        self.splitter.setHandleWidth(2)

        # Configure item tree widget

        # TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!下面这句话可能还要改！

        self.itemTree = ItemTree.ItemTree()        #修改了 这样才能找得到itemtree
        self.splitter.addWidget(self.itemTree)      
        self.splitter.addWidget(self.itemTree.editBox)
        self.mainLayout.addWidget(self.splitter)  #这几行的splitter打包到layout上面

        # Is a status bar needed in this application?
        #self.statusBar = QStatusBar()
        #self.mainLayout.addWidget(self.statusBar)

        # Set layout as the central widget
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

        # TEST ONLY
        #self.uniqueCounter = 0 老师删掉了
        
        return
        
    #-------------------------------------------------------------------------- 这部分是给新增加的方法定义一下
    def on_create_new_note_action(self):
        return

    
    def on_save_action(self):
        return

    def on_save_as_action(self):
        return
#---------------------------------------------------------- 下面这两个都写好了
    
    def on_delete_item(self):
        """   """
        self.itemTree.delete_task_item()
        return

   
    def on_edit_item(self):
        """Handler for 'Open' menu item"""
        self.itemTree.edit_task_item()
        return


#----------------------------------------------------------
    def on_insert_item_action(self):
        """Handler for 'add item' action"""

        """
        # Test code
        title = str(self.uniqueCounter)
        self.uniqueCounter += 1

        # TODO Get parameters of new task
        iconIndex = 0
        #title = ""
        deadline = 0
        
        self.itemTree.insert_task_item(iconIndex, title, deadline, True, False)      
        print("adding an item")
        """
        """
        title, ok = QInputDialog.getText(self, 'Title', 'Enter Title')
        if (not ok or not title):   #用户取消了 就退回到刚才界面了
            return
        
        iconIndex, ok = QInputDialog.getInt(self, 'Icon Index', 'Choose Icon index')
        if (not ok):            #问图标的样式 需要用户输入0，1，2，3
            return
        
        deadline, ok = QInputDialog.getText(self, 'Deadline', 'Enter Deadline (YYYYMMDDHHMM)')
        if (not ok):           #按格式输入deadline #Int撑不住这么大的数 所以改成了Text,处理成字符串再转成数
            return

        self.itemTree.insert_task_item(iconIndex, title, deadline, True, False)  
        
        """
        self.itemTree.insert_task_item(True, False) 
        print("adding an item")          

        return
        
   #--------------------------------------------------------------------------
   
    def on_insert_child_item_action(self):
        """Handler for 'add child item' action"""

        """

        # Test code
        title = str(self.uniqueCounter)
        self.uniqueCounter += 1

        # TODO Get parameters of new task
        iconIndex = 0
        #title = ""
        deadline = 0

        self.itemTree.insert_task_item(iconIndex, title, deadline, True, True)      
        print("add a child item")
        
        return
        
        """

        """
        title, ok = QInputDialog.getText(self, 'Title', 'Enter Title')
        if (not ok or not title):
            return

        iconIndex, ok = QInputDialog.getInt(self, 'Icon Index', 'Choose Icon index')
        if (not ok):
            return

        deadline, ok = QInputDialog.getInt(self, 'Deadline', 'Enter Deadline (YYYYMMDDHHMM)')
        if (not ok):
            return
        
        self.itemTree.insert_task_item(iconIndex, title, deadline, True, True) 
        
        """    
        self.itemTree.insert_task_item(True, True) 
        print("add a child item")

        return


        
   #--------------------------------------------------------------------------
    
    def on_open_action(self):
        """Handler for 'open' action"""
        
        fileName_choose,filetype = QFileDialog.getOpenFileName(self,
                                    "Open",                            #弹出窗口后的标题显示open
                                    "C:\\Users\\", # 从起始路径打开文件
                                    "All Files (*);;Text Files (*.txt);;Word Files (*.docx)" )  # 设置文件扩展名过滤,用双分号间隔 增加了一个word文件

        print("open file item")  #提示找错的 

        if fileName_choose == "":
            print("\nDeslect the choose") #用户犹豫不决 关掉之后显示的话
            return

        print("\nThe file you choosed:") #选择文件之后显示的
        print(fileName_choose)
        print("File type: ",filetype)

        
        f = open(fileName_choose) #这四行代表 读取文件出来
        lines = f.read()
        #add_task_item(lines)      # add_task_item 
        print(lines)    #方便查错print
        f.close()

        
        fn=fileName_choose.split("/")[-1]  #把文件名从地址中提取出来 只显示文件名和格式 -1表示选取最后一项

        self.itemTree.add_task_item(0, fn, lines, 0, False, 0)   #调用这个方法，把东西投屏到右边 做出相应的事情 右边设置成了默认值
        #ItemTree.add_task_item(self,iconIndex, title, note, deadline, expanded, indentLevel)


        return

    #--------------------------------------------------------------------------
   
    def on_set_preferences_action(self):
        """Handler for 'set preferences' action"""

        self.itemTree.set_item_tree_preferences()
        
        return
    
    #--------------------------------------------------------------------------   
    
    def on_quit_action(self):
        """Handler for 'quit' action"""
        
        print("quitting application")
        self.close()
        
        return     

#******************************************************************************

# Main program
if __name__ == "__main__":
    application = QApplication([])

    mainWindow = MainWindow()
    mainWindow.show()

    # test
    #mainWindow.itemTree.add_task_item(0, "hello", "note", 0, True, 0)
    #mainWindow.itemTree.add_task_item(0, "hello2", "note", 0, True, 0)
    #mainWindow.itemTree.add_task_item(0, "first child", "note", 0, True, 0)
    
    
    exit(application.exec_())   # Not sure why this still has to be `exec_` with a trailing underscore?

#******************************************************************************















