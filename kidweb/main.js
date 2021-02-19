{
    
    
    const {app,Menu,globalShortcut,net, BrowserWindow ,ipcMain} = require('electron')
    Menu.setApplicationMenu(null)
//进行监控，如果有new-window 发送过来，则重新创建一个窗口，文件是list.html
    
//进行监控，如果有new-window 发送过来，则重新创建一个窗口，文件是list.html

    // Keep a global reference of the window object, if you don't, the window will
    // be closed automatically when the JavaScript object is garbage collected.
    let win
    function hide() {
      const js = require("fs").readFileSync(__dirname+'/insert/js.js').toString();
      win.webContents.executeJavaScript(js)
    }
    function createWindow () {
      // 创建浏览器窗口。
      win = new BrowserWindow({width: 1920, height: 1080})
      
      win.loadFile(__dirname+"/index.html")
      globalShortcut.register('ESC', function () {
          win.webContents.goBack()
      })
      globalShortcut.register('F4', function () {
        //  编写你的代码
        // ...

        let request=net.request('http://localhost:8080/state0')
        request.on('response',(response)=>{
            
          response.on('data',(chunk)=>{
              
          })

          response.on('end',()=>{
            app.quit()
            
          })
          
      })
      request.end();
     
      
        
      })
      const {session} = require('electron')
      const ses = session.defaultSession
      
      var valid=require('./block')
    win.webContents.on('new-window', (event, url) => {
      event.preventDefault()
      console.log(url)
      if(valid.validate(url)==true){
        win.loadURL(url)
        
      }
        
  })
  win.webContents.on('did-finish-load', function() {
    hide()
  });

  win.webContents.on('will-navigate', ( url)=>{
    console.log("re : "+url)
  });
  
      
      // 然后加载应用的 index.html。
      
      
      
      // 打开开发者工具
      //win.webContents.openDevTools()
  
      // 当 window 被关闭，这个事件会被触发。
      win.on('closed', () => {
        // 取消引用 window 对象，如果你的应用支持多窗口的话，
        // 通常会把多个 window 对象存放在一个数组里面，
        // 与此同时，你应该删除相应的元素。
        win = null
      })
      
      
    }
  
    
    app.on('ready', createWindow)
  
    // 当全部窗口关闭时退出。
    app.on('window-all-closed', () => {
      // 在 macOS 上，除非用户用 Cmd + Q 确定地退出，
      // 否则绝大部分应用及其菜单栏会保持激活。
      if (process.platform !== 'darwin') {
        app.quit()
      }
    })
  
    app.on('activate', () => {
      // 在macOS上，当单击dock图标并且没有其他窗口打开时，
      // 通常在应用程序中重新创建一个窗口。
      if (win === null) {
        createWindow()
      }
    })
    
    
}

  