// page.js

const { ipcRenderer } = require('electron');

export async function page_1() {
    const contentDiv = document.getElementById('content');
    contentDiv.style.border = 'none';
    contentDiv.innerHTML = `<h1 style="text-align: center; width: 100%;">演示页面（page.js）</h1>`;
}