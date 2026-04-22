# 🚌 BusUCR — Rutas externas de la UCR
 
> Plataforma web para estudiantes de la Universidad de Costa Rica que usan el transporte público externo. Horarios en tiempo real, estimación de posición del bus, reportes colaborativos y detección de parada más cercana por GPS.
 
[![Estado](https://img.shields.io/badge/estado-activo-brightgreen)](https://bus-ucr-externo.netlify.app)
[![Licencia](https://img.shields.io/badge/licencia-personalizada-orange)](#licencia)
[![Hecho con](https://img.shields.io/badge/hecho%20con-HTML%20%2B%20CSS%20%2B%20JS%20%2B%20Firebase-purple)](#)
 
---
 
## ✨ Funcionalidades

- 🕐 **Próximo bus según el horario del día** — muestra la próxima salida disponible según la ruta y el día actual
- 📍 **GPS inteligente** — detecta automáticamente la parada más cercana al usuario
- 🚌 **Posición estimada del bus** — calculada con horarios, reportes de usuarios y offsets entre paradas
- 📊 **Reportes colaborativos** — permite reportar si el bus ya pasó, dónde va o si viene con atraso
- 📋 **Horarios por día** — horarios diferenciados de lunes a domingo según cada ruta
- 💬 **Grupos de WhatsApp** — acceso directo a los grupos de cada ruta
- 🔔 **Notificaciones** — avisos importantes sobre cancelaciones, cambios o información relevante
- 🏪 **Emprendimientos estudiantiles** — espacio para apoyar y visualizar emprendimientos de la comunidad UCR
- 📍 **Ferias de emprendedores** — desde `/emprendimientos` se pueden ver las ferias disponibles, su ubicación en el mapa y los detalles del evento
- ☕ **Donaciones opcionales** — permite apoyar el mantenimiento del proyecto sin afectar el uso gratuito de la app
- 📱 **Diseño responsive y PWA** — funciona desde celular, computadora y puede instalarse como app
- ⚙️ **Panel de administración** — protegido con Firebase Authentication para gestionar horarios, avisos, emprendimientos y ferias
 
---
 
## 🗺️ Rutas disponibles
 
| Ruta | URL |
|------|-----|
| Coronado ↔ UCR | `/coronado` |
| Tibás ↔ UCR | `/tibas` |
| Heredia ↔ UCR | `/heredia` |
| Acosta / Aserrí ↔ UCR | `/acosta` |
| San Ramón ↔ UCR | `/san_ramon` |
| Santa Ana / Escazú ↔ UCR | `/santa_ana_escazu` |
| Alajuela ↔ UCR | `/alajuela` |
| San Rafael ↔ UCR | `/san_rafael` |
| Desamparados ↔ UCR | `/desamparados` |
| La Periférica ↔ UCR | `/periferica` |
| Pavas ↔ UCR | `/pavas` |
| Interlinea ↔ UCR | `/interlinea` |
| Emprendimientos| `/emprendimientos` |
 
---
 
## 🛠️ Tecnologías
 
- **Frontend** — HTML, CSS, JavaScript vanilla
- **Base de datos** — Firebase Firestore
- **Autenticación** — Firebase Authentication
- **Hosting** — Netlify
- **PWA** — Service Worker + Web App Manifest
 
---
 
## 📁 Estructura del proyecto
 
```
busucr/
├── index.html              # Página principal con todas las rutas
├── coronado.html           # Ruta Coronado ↔ UCR
├── tibas.html              # Ruta Tibás ↔ UCR
├── heredia.html            # Ruta Heredia ↔ UCR
├── acosta.html             # Ruta Acosta / Aserrí ↔ UCR
├── san_ramon.html          # Ruta San Ramón ↔ UCR
├── santa_ana_escazu.html   # Ruta Santa Ana / Escazú ↔ UCR
├── alajuela.html           # Ruta Alajuela ↔ UCR
├── san_rafael.html         # Ruta San Rafael ↔ UCR
├── desamparados.html       # Ruta Desamparados ↔ UCR
├── periferica.html         # Ruta La Periférica ↔ UCR
├── interlinea.html         # Ruta Interlinea↔ UCR
├── emprendimientos.html    # Emprendimientos
├── pavas.html              # Ruta Pavas ↔ UCR
├── creditos.html           # Easter egg — créditos del proyecto
├── manifest.json           # PWA manifest
├── sw.js                   # Service Worker
├── netlify.toml            # Configuración de Netlify (redirects)
└── icons/                  # Íconos de la PWA
    ├── icon-192.png
    └── icon-512.png
```
 
---
 
## 🚀 Correr localmente
 
No necesitás instalar dependencias. Solo necesitás Python:
 
```bash
# Clonar el repo
git clone https://github.com/Desmond16170/busucr.git
cd busucr
 
# Iniciar servidor local
python server.py
```
 
Luego abrís `http://localhost:8080` en tu navegador.
 
> El `server.py` simula los redirects de Netlify para que las rutas `/coronado`, `/tibas`, etc. funcionen igual que en producción.
 
---
 
## 🤝 Colaborar
 
¿Usás alguna de estas rutas y querés ayudar? Hay varias formas de contribuir:
 
### Datos y horarios
Si notás que un horario está desactualizado o falta una parada, podés:
- Abrir un **Issue** en este repo describiendo el cambio
- O escribirnos por Instagram [@bus_u.c.r](https://www.instagram.com/bus_u.c.r)
 
### Nuevas rutas
Si querés que se agregue una ruta que no está, abrí un Issue con:
- Nombre de la ruta
- Horarios UCR → destino y destino → UCR por día
- Paradas principales con nombre y tiempo aproximado desde UCR
 
### Código
Si querés contribuir con código:
1. Hacé un fork del repo
2. Creá una rama con tu cambio (`git checkout -b mejora/nombre`)
3. Hacé commit de tus cambios
4. Abrí un Pull Request describiendo qué cambiaste y por qué
 
> Por favor revisá la [licencia](#licencia) antes de contribuir. Cualquier contribución se hace bajo los mismos términos.
 
---
 
## ☕ Apoyar el proyecto
 
BusUCR es completamente gratuito y sin anuncios. Si te ha sido útil y querés ayudar a mantenerlo vivo, podés invitarme un café:
 
[![Ko-fi](https://img.shields.io/badge/Donar-Ko--fi-ff5e5b?logo=ko-fi)](https://ko-fi.com/Q5Q2187D5I)
 
Cada aporte, por pequeño que sea, ayuda a costear el hosting y el tiempo dedicado al proyecto. 🙏
 
---
 
## 📄 Licencia
 
Este proyecto usa una **licencia personalizada**. En resumen:
 
- ✅ Podés usarlo y estudiarlo libremente con fines personales o educativos
- ✅ Debés dar crédito visible al autor original (BusUCR / L. Fernando Herrera Vargas)
- ❌ No podés usarlo con fines comerciales sin autorización escrita
- ❌ No podés redistribuirlo como trabajo propio
 
Consultá el archivo [`LICENSE`](./LICENSE) para los términos completos en español, inglés y portugués.
 
---
 
## 📬 Contacto
 
- Instagram: [@bus_u.c.r](https://www.instagram.com/bus_u.c.r)
- GitHub: [@Desmond16170](https://github.com/Desmond16170)
 
---
 
<p align="center">Hecho por Luis Fernando Herrera Vargas🎓</p>
