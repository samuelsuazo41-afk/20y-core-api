self.addEventListener('install', e => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(clients.claim()));
self.addEventListener('fetch', e => e.respondWith(fetch(e.request)));

self.addEventListener('message', e => {
  if (e.data.type === 'SCHEDULE_SPITH') {
    scheduleSpith(e.data.freq);
  }
});

function scheduleSpith(freq) {
  const now = new Date();
  let next = new Date();
  next.setHours(9, 0, 0, 0);
  if (now > next) next.setDate(next.getDate() + 1);
  if (freq === 'semanal') {
    const day = next.getDay();
    const diff = day === 1? 0 : (day === 0? 1 : 8 - day);
    next.setDate(next.getDate() + diff);
  }
  const delay = next.getTime() - now.getTime();
  setTimeout(() => {
    self.registration.showNotification('20Y SPITH', {
      body: 'Abre 20Y para leer tu Spith de hoy. Nivel 4/4 te espera.',
      icon: 'icon-192.png',
      badge: 'icon-192.png',
      tag: '20y-spith',
      renotify: true
    });
    scheduleSpith(freq);
  }, delay);
}

self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(clients.openWindow('/'));
});