const CACHE_NAME = '20y-pulse-v9';
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json',
  '/icon-192.png',
  '/icon-512.png'
];

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(
    caches.open(CACHE_NAME)
    .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.map(key => {
        if (key!== CACHE_NAME) return caches.delete(key);
      })
    )).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request)
    .then(response => response || fetch(e.request))
  );
});

self.addEventListener('message', e => {
  if (e.data.type === 'SCHEDULE_SPITH') {
    scheduleSpith(e.data.freq);
  }
});

self.addEventListener('notificationclick', e => {
  e.notification.close();
  const targetTab = e.notification.data?.tab || 'spith';
  e.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then(clientList => {
      for (const client of clientList) {
        if (client.url.includes(self.location.origin) && 'focus' in client) {
          client.focus();
          client.postMessage({ type: 'OPEN_TAB', tab: targetTab });
          return;
        }
      }
      if (clients.openWindow) {
        return clients.openWindow('./#' + targetTab);
      }
    })
  );
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
    showSpithNotification();
    scheduleSpith(freq);
  }, delay);
}

async function showSpithNotification() {
  const clients = await self.clients.matchAll();
  if (clients.length > 0) {
    const msgChannel = new MessageChannel();
    clients[0].postMessage({ type: 'GET_SPITH' }, [msgChannel.port2]);
    const spith = await new Promise(resolve => {
      msgChannel.port1.onmessage = e => resolve(e.data);
    });
    self.registration.showNotification('20Y SPITH DIARIO', {
      body: spith,
      icon: 'icon-192.png',
      badge: 'icon-192.png',
      tag: '20y-spith',
      renotify: true,
      requireInteraction: true,
      data: { tab: 'spith' }
    });
  } else {
    self.registration.showNotification('20Y SPITH DIARIO', {
      body: 'Nivel 4/4 activo. Abre 20Y para tu Spith de hoy.',
      icon: 'icon-192.png',
      badge: 'icon-192.png',
      tag: '20y-spith',
      requireInteraction: true,
      data: { tab: 'spith' }
    });
  }
}