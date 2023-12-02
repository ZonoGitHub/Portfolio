const socket = io('http://your-server-address');

socket.on('notification', (data) => {
    const notification = document.createElement('div');
    notification.classList.add('notification');
    notification.innerHTML = `
        <span class="message">${data.message}</span>
        <span class="timestamp">${data.timestamp}</span>
        <button class="mark-as-read" data-notification-id="${data.id}">Marquer comme lu</button>
    `;
    document.getElementById('notifications').appendChild(notification);
});