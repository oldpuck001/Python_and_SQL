// main.js

const { app, BrowserWindow } = require('electron');

function createWindow() {
  // 創建瀏覽器窗口
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  // 加載應用的 index.html
  win.loadFile('index.html');
}

// 當 Electron 完成初始化並準備創建瀏覽器窗口時調用
app.whenReady().then(createWindow);

// 當所有窗口都關閉時退出應用
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});