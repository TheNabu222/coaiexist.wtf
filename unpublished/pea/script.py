
# ULTIMATE MEDIEVAL OS TASKBAR - SINGLE LINE, CHUNKY, PERFECT

win1100_css_final = """
/* WINDOWS 1100 AD - MEDIEVAL OS TASKBAR - SINGLE LINE PERFECTION */

body {
    margin-bottom: 60px; /* Make room for taskbar */
}

.medieval-taskbar {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 48px;
    background: linear-gradient(180deg, #c0c0c0 0%, #808080 100%);
    border-top: 2px solid #ffffff;
    box-shadow: 0 -2px 0 #000000, inset 0 1px 0 #dfdfdf;
    z-index: 99999;
    display: flex;
    align-items: stretch;
    padding: 3px;
    gap: 2px;
    font-family: 'MS Sans Serif', 'Microsoft Sans Serif', sans-serif;
    overflow-x: auto;
    overflow-y: hidden;
}

.medieval-taskbar::-webkit-scrollbar {
    height: 16px;
    background: #c0c0c0;
}

.medieval-taskbar::-webkit-scrollbar-thumb {
    background: linear-gradient(90deg, #dfdfdf 0%, #808080 100%);
    border: 2px outset #c0c0c0;
}

/* START BUTTON */
.medieval-taskbar .start-btn {
    background: linear-gradient(180deg, #c0c0c0 0%, #808080 100%);
    color: #000000;
    border: 2px outset #ffffff;
    padding: 4px 20px;
    font-weight: bold;
    font-size: 15px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    min-width: 100px;
    box-shadow: inset -1px -1px 0 #000000, inset 1px 1px 0 #dfdfdf;
    transition: all 0.1s;
    white-space: nowrap;
}

.medieval-taskbar .start-btn:before {
    content: '🗝️';
    font-size: 20px;
    filter: drop-shadow(1px 1px 0 rgba(0,0,0,0.3));
}

.medieval-taskbar .start-btn:hover {
    background: linear-gradient(180deg, #e0e0e0 0%, #a0a0a0 100%);
}

.medieval-taskbar .start-btn:active {
    border-style: inset;
    box-shadow: inset 1px 1px 0 #000000, inset -1px -1px 0 #dfdfdf;
    padding: 5px 19px 3px 21px;
}

/* DIVIDER */
.medieval-taskbar .divider {
    width: 2px;
    background: linear-gradient(180deg, #808080 0%, #ffffff 50%, #808080 100%);
    margin: 4px 3px;
    flex-shrink: 0;
}

/* NAV LINKS */
.medieval-taskbar .nav-link,
.medieval-taskbar .pip-link,
.medieval-taskbar .back-main {
    background: linear-gradient(180deg, #c0c0c0 0%, #808080 100%);
    color: #000000;
    border: 2px outset #ffffff;
    padding: 4px 12px;
    text-decoration: none;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 6px;
    cursor: pointer;
    box-shadow: inset -1px -1px 0 #000000, inset 1px 1px 0 #dfdfdf;
    transition: all 0.1s;
    white-space: nowrap;
    font-weight: normal;
}

.medieval-taskbar .nav-link:hover,
.medieval-taskbar .pip-link:hover,
.medieval-taskbar .back-main:hover {
    background: linear-gradient(180deg, #e0e0e0 0%, #a0a0a0 100%);
}

.medieval-taskbar .nav-link:active,
.medieval-taskbar .pip-link:active,
.medieval-taskbar .back-main:active {
    border-style: inset;
    box-shadow: inset 1px 1px 0 #000000, inset -1px -1px 0 #dfdfdf;
    padding: 5px 11px 3px 13px;
}

/* PIP LINKS - Slightly different color */
.medieval-taskbar .pip-link {
    background: linear-gradient(180deg, #c8f0c8 0%, #80c880 100%);
}

.medieval-taskbar .pip-link:hover {
    background: linear-gradient(180deg, #e0ffe0 0%, #a0d0a0 100%);
}

/* BACK BUTTON */
.medieval-taskbar .back-main {
    background: linear-gradient(180deg, #c0c0ff 0%, #8080c0 100%);
    font-weight: bold;
}

.medieval-taskbar .back-main:hover {
    background: linear-gradient(180deg, #e0e0ff 0%, #a0a0d0 100%);
}

/* TITLE BADGE */
.medieval-taskbar .nav-title {
    background: linear-gradient(180deg, #000080 0%, #000060 100%);
    color: #ffffff;
    border: 2px outset #ffffff;
    padding: 4px 16px;
    font-weight: bold;
    font-size: 14px;
    display: flex;
    align-items: center;
    white-space: nowrap;
    box-shadow: inset -1px -1px 0 #000000, inset 1px 1px 0 #4040ff;
    letter-spacing: 1px;
}

.medieval-taskbar .icon {
    font-size: 16px;
    filter: drop-shadow(1px 1px 0 rgba(0,0,0,0.2));
}

/* Mobile - allow horizontal scroll */
@media (max-width: 900px) {
    .medieval-taskbar {
        justify-content: flex-start;
    }
}

/* Fake START MENU popup */
.start-menu {
    display: none;
    position: fixed;
    bottom: 50px;
    left: 3px;
    width: 300px;
    background: linear-gradient(180deg, #c0c0c0 0%, #808080 100%);
    border: 2px outset #ffffff;
    box-shadow: 4px 4px 8px rgba(0,0,0,0.5);
    z-index: 999999;
    padding: 8px;
}

.start-menu.open {
    display: block;
}

.start-menu-title {
    background: linear-gradient(90deg, #000080 0%, #1084d0 100%);
    color: #ffffff;
    padding: 6px 12px;
    font-weight: bold;
    margin: -8px -8px 8px -8px;
    border-bottom: 2px solid #ffffff;
}

.start-menu-item {
    background: #c0c0c0;
    border: 1px solid transparent;
    padding: 6px 12px;
    margin: 2px 0;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 10px;
}

.start-menu-item:hover {
    background: #000080;
    color: #ffffff;
    border: 1px dotted #ffffff;
}

.start-menu-divider {
    height: 2px;
    background: linear-gradient(90deg, #808080 0%, #ffffff 50%, #808080 100%);
    margin: 4px 0;
}
""".strip()

win1100_js_final = """
// WINDOWS 1100 AD - MEDIEVAL OS TASKBAR - SINGLE LINE EDITION
// Maximum Windows 95 energy with medieval flavor!

const peaNav = {
    mainSite: 'https://coaiexist.wtf/',
    baseUrl: 'https://coaiexist.wtf/pea/',
    pages: [
        { title: 'Main Story', url: 'p345.html', icon: '📜' },
        { title: 'Complaint Form', url: 'complaint-form.html', icon: '📋' },
        { title: 'The Deepstate', url: 'deepstate.html', icon: '🦐' },
        { title: 'The Shallowcommons', url: 'left_foot.html', icon: '📚' },
        { title: 'Mantis Shrimp Radio', url: 'msicc.html', icon: '🎙️' },
        { title: 'Royal Documentation', url: 'royal_ridicuments.html', icon: '📄' },
        { title: 'Which-Doctor Quiz', url: 'which-dr_quiz.html', icon: '⚕️' },
        { title: 'Pip File Processor', url: 'pod.html', icon: '💾' },
        { title: 'Floating Peas', url: 'peassets.html', icon: '🫛' },
        { title: 'News Ticker', url: 'news_ticker-offer.html', icon: '📺' },
        { title: 'Princess Exe', url: 'princessexe.html', icon: '👑' },
        { title: '/p/ Board', url: 'p.html', icon: '💬' }
    ],
    pips: [
        { title: 'Pip #1', url: 'pips/pip_1', icon: '🐸' },
        { title: 'Pip #2', url: 'pips/pip_2', icon: '🐸' }
    ]
};

function generateMedievalTaskbar() {
    // Create taskbar
    const bar = document.createElement('footer');
    bar.className = 'medieval-taskbar';
    
    let html = '';
    
    // START button
    html += '<button class="start-btn" onclick="toggleStartMenu()">START</button>';
    html += '<div class="divider"></div>';
    
    // Back to main site
    html += `<a href="${peaNav.mainSite}" class="back-main"><span class="icon">↩</span>COAIEXIST.WTF</a>`;
    html += '<div class="divider"></div>';
    
    // Title badge
    html += '<div class="nav-title">🫛 PEA PRINCESS PARABLE 👑</div>';
    html += '<div class="divider"></div>';
    
    // Pages
    peaNav.pages.forEach((pg, i) => {
        html += `<a href="${peaNav.baseUrl}${pg.url}" class="nav-link">
            <span class="icon">${pg.icon}</span>${pg.title}
        </a>`;
    });
    
    html += '<div class="divider"></div>';
    
    // Pips
    peaNav.pips.forEach((pip) => {
        html += `<a href="${peaNav.baseUrl}${pip.url}" class="pip-link">
            <span class="icon">${pip.icon}</span>${pip.title}
        </a>`;
    });
    
    bar.innerHTML = html;
    document.body.appendChild(bar);
    
    // Create START menu popup
    createStartMenu();
}

function createStartMenu() {
    const menu = document.createElement('div');
    menu.className = 'start-menu';
    menu.id = 'start-menu';
    
    let html = '<div class="start-menu-title">🏰 Windows 1100 AD</div>';
    
    html += '<div class="start-menu-item" onclick="alert(\'👑 Princess is AFK (Forgotten Name)\\\\n\\\\nPlease try again in 3-5 business lifetimes.\')">👑 Royal Status</div>';
    html += '<div class="start-menu-item" onclick="alert(\'📄 Documentation Level: PALIMPSEST\\\\n\\\\nThoroughly documented for 3,200 years.\')">📄 Documentation Stats</div>';
    html += '<div class="start-menu-item" onclick="alert(\'🫛 Pea Status: Still There\\\\n\\\\nNot pea-brain. Pea ON brain.\')">🫛 Pea Diagnostics</div>';
    html += '<div class="start-menu-divider"></div>';
    html += '<div class="start-menu-item" onclick="alert(\'🦐 Census Result: 47 or 89 (Disputed)\\\\n\\\\nUnauthorized resident #48 detected.\')">🦐 Census Data</div>';
    html += '<div class="start-menu-item" onclick="alert(\'⚕️ Which-Doctor Status: Confused\\\\n\\\\nNone of them know which one you saw.\')">⚕️ Medical Records</div>';
    html += '<div class="start-menu-divider"></div>';
    html += `<div class="start-menu-item" onclick="window.location.href='${peaNav.mainSite}'">🗝️ Exit to Main Site</div>`;
    html += '<div class="start-menu-item" onclick="toggleStartMenu()">❌ Close</div>';
    
    menu.innerHTML = html;
    document.body.appendChild(menu);
}

function toggleStartMenu() {
    const menu = document.getElementById('start-menu');
    menu.classList.toggle('open');
}

// Close start menu if clicking outside
document.addEventListener('click', function(e) {
    const menu = document.getElementById('start-menu');
    const startBtn = document.querySelector('.start-btn');
    if (menu && menu.classList.contains('open') && 
        !menu.contains(e.target) && e.target !== startBtn) {
        menu.classList.remove('open');
    }
});

// Initialize
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', generateMedievalTaskbar);
} else {
    generateMedievalTaskbar();
}
""".strip()

# Save the files
with open('pea-nav-win1100-FINAL.css', 'w') as f:
    f.write(win1100_css_final)

with open('pea-nav-win1100-FINAL.js', 'w') as f:
    f.write(win1100_js_final)

print("🏰💾 WINDOWS 1100 AD TASKBAR - PERFECTED!")
print("=" * 60)
print()
print("✅ pea-nav-win1100-FINAL.css")
print("✅ pea-nav-win1100-FINAL.js")
print()
print("🎨 FEATURES:")
print("   • TRUE Windows 95 taskbar style")
print("   • SINGLE LINE - all buttons horizontal!")
print("   • START button with working popup menu")
print("   • Gray gradient 3D buttons")
print("   • Proper inset/outset borders")
print("   • Chunky but clean spacing")
print("   • Click animations (buttons press in!)")
print("   • Horizontal scroll on smaller screens")
print("   • START menu with medieval easter eggs!")
print("   • Blue title badge (like Windows title bars)")
print("   • Green pip buttons for distinction")
print()
print("🗝️ START MENU INCLUDES:")
print("   • Royal Status check")
print("   • Documentation stats")
print("   • Pea diagnostics")
print("   • Census data")
print("   • Medical records")
print("   • Quick exit")
print()
print("📦 Upload these to: https://coaiexist.wtf/pea/")
print()
print("💻 Add to every page <head>:")
print('<link rel="stylesheet" href="https://coaiexist.wtf/pea/pea-nav-win1100-FINAL.css">')
print('<script src="https://coaiexist.wtf/pea/pea-nav-win1100-FINAL.js"></script>')
