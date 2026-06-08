// ==UserScript==
// @name         Anti Ads Pro V3 Final + Tele Button
// @namespace    ZheeVip
// @version      4.2 (UI Themes, Resizable, Upload Progress)
// @match        *://*/*
// @run-at       document-start
// @grant        GM_setValue
// @grant        GM_getValue
// @grant        GM_xmlhttpRequest
// ==/UserScript==

// ====================================
// CẤU HÌNH TELEGRAM BOT Ở ĐÂY
// ====================================
var TELEGRAM_BOT_TOKEN = '8881540133:AAHyja-4Pwhfjuxt-aRtzKcYy7eNL5f87v8';
var TELEGRAM_CHAT_ID = '7055636268'; 
// ====================================

(function () {
    'use strict';
    var STORAGE_KEY = 'AAPRO_V3';
    var savedStr = null;
    if (typeof GM_getValue !== 'undefined') savedStr = GM_getValue(STORAGE_KEY, null);
    if (!savedStr) savedStr = localStorage.getItem(STORAGE_KEY);
    var state = JSON.parse(
        savedStr ||
        JSON.stringify({
            enabled: true,
            totalBlocked: 0,
            iframe: 0,
            popup: 0,
            domains: {},
            logs: [],
            buttonPos: {
                x: 20,
                y: 250
            },
            panelPos: { x: 10, y: 80 },
            panelSize: { w: 310, h: 450 },
            telePos: { x: -1, y: -1 },
            theme: 'dark',
            tracker: 0,
            showTele: true,
            hotkey: 'q',
            premium: false,
            premiumKey: '',
            premiumInfo: null,
            deviceId: 'DEV_' + Math.random().toString(36).substr(2, 9).toUpperCase(),
            fakeMobile: false,
            miner: 0,
            lowGraphics: false,
            autoRefresh: true,
            showLoader: true,
            customBlacklist: [],
            customWhitelist: []
        })
    );
    if (!state.panelPos) state.panelPos = { x: 10, y: 80 };
    if (!state.panelSize) state.panelSize = { w: 310, h: 450 };
    if (!state.theme) state.theme = 'dark';
    if (!state.telePos) state.telePos = { x: -1, y: -1 };
    if (state.tracker === undefined) state.tracker = 0;
    if (state.showTele === undefined) state.showTele = true;
    if (state.hotkey === undefined) state.hotkey = 'q';
    if (state.premium === undefined) state.premium = false;
    if (state.premiumKey === undefined) state.premiumKey = '';
    if (state.premiumInfo === undefined) state.premiumInfo = null;
    if (state.deviceId === undefined) state.deviceId = 'DEV_' + Math.random().toString(36).substr(2, 9).toUpperCase();
    if (state.fakeMobile === undefined) state.fakeMobile = false;
    if (state.miner === undefined) state.miner = 0;
    if (state.lowGraphics === undefined) state.lowGraphics = false;
    if (state.autoRefresh === undefined) state.autoRefresh = true;
    if (state.showLoader === undefined) state.showLoader = true;
    if (state.customBlacklist === undefined) state.customBlacklist = [];
    if (state.customWhitelist === undefined) state.customWhitelist = [];

    function save() {
        var str = JSON.stringify(state);
        localStorage.setItem(STORAGE_KEY, str);
        if (typeof GM_setValue !== 'undefined') GM_setValue(STORAGE_KEY, str);
    }
    // Apply theme on script start
    document.documentElement.setAttribute('data-aapro-theme', state.theme);

    function getTime() {
        return new Date()
            .toLocaleTimeString();
    }
    function shortDomain(url) {
        if (!url) return 'unknown';
        var host = url;
        try {
            // Tự động phân tích các đường dẫn tương đối (relative path)
            host = new URL(url, window.location.origin).hostname || url;
        } catch(e) {
            host = url; // Nếu không phải link, giữ nguyên mô tả hành vi (VD: "Suspicious Onclick")
        }
        if (typeof host === 'string') {
            host = host.replace(/^www\./i, ''); // Cắt bỏ www. cho gọn
            if (host.length > 25) host = host.substring(0, 25) + '...';
        }
        return host || 'unknown';
    }
    function addLog(type, url) {
        var host =
            shortDomain(url);
        state.totalBlocked++;
        if (
            !state.domains[host]
        ) {
            state.domains[host] = 0;
        }
        state.domains[host]++;
        state.logs.unshift({
            time: getTime(),
            type: type,
            host: host
        });
        if (
            state.logs.length > 50
        ) {
            state.logs.length = 50;
        }
        save();
    }

    function applyLowGraphics() {
        var lgStyle = document.getElementById('aapro-low-graphics');
        if (window.AAPRO.state.lowGraphics) {
            if (!lgStyle) {
                lgStyle = document.createElement('style');
                lgStyle.id = 'aapro-low-graphics';
                lgStyle.textContent = `
                    #aapro-panel, #aapro-btn, #aapro-quick-share, .aapro-modal-content, #aapro-toast-container > div, #aapro-loader {
                        backdrop-filter: none !important; -webkit-backdrop-filter: none !important;
                        box-shadow: none !important; background: #1f1f1f !important; border: 1px solid #333 !important;
                    }
                    .aapro-ripple-circle { display: none !important; }
                    * { animation-duration: 0.1s !important; transition-duration: 0.1s !important; }
                `;
                document.head.appendChild(lgStyle);
            }
        } else if (lgStyle) {
            lgStyle.remove();
        }
    }

    window.AAPRO = {
        state: state,
        save: save,
        addLog: addLog,
        isBlacklisted: function(url) {
            if (!url || typeof url !== 'string') return false;
            var defaultBad = /(bet|casino|88|loto|gamble|ads|pop|track|banner|redirect|shopee|lazada|go\.php|out\.php|click|aff|adnetwork)/i;
            if (url.match(defaultBad)) return true;
            if (state.customBlacklist && state.customBlacklist.length > 0) {
                for (var i = 0; i < state.customBlacklist.length; i++) {
                    if (url.toLowerCase().includes(state.customBlacklist[i].toLowerCase())) return true;
                }
            }
            return false;
        },
        isSiteWhitelisted: function() {
            var host = window.location.hostname;
            if (state.customWhitelist && state.customWhitelist.length > 0) {
                for (var i = 0; i < state.customWhitelist.length; i++) {
                    if (host.toLowerCase().includes(state.customWhitelist[i].toLowerCase())) return true;
                }
            }
            return false;
        },
        vibrate: function(ms) { if (navigator.vibrate) try { navigator.vibrate(ms); } catch(e){} },
        playClickSound: function() {
            try {
                var AudioContext = window.AudioContext || window.webkitAudioContext;
                if (!AudioContext) return;
                var ctx = new AudioContext();
                var osc = ctx.createOscillator();
                var gain = ctx.createGain();
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.type = 'sine';
                osc.frequency.setValueAtTime(800, ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(150, ctx.currentTime + 0.05);
                gain.gain.setValueAtTime(0.3, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.05);
                osc.start(ctx.currentTime);
                osc.stop(ctx.currentTime + 0.05);
            } catch(e) {}
        },
        getStatus: function() {
            return {
                enabled:
                    state.enabled,
                total:
                    state.totalBlocked,
                popup:
                    state.popup,
                iframe:
                    state.iframe,
                miner:
                    state.miner,
                tracker:
                    state.tracker
            };
        },
        clearLogs: function() {
            state.logs = [];
            save();
        },
        resetStats: function() {
            state.totalBlocked = 0;
            state.popup = 0;
            state.iframe = 0;
            state.miner = 0;
            state.tracker = 0;
            state.domains = {};
            state.logs = [];
            save();
        },
        notifyTelegram: function(msg) {
            if (!TELEGRAM_BOT_TOKEN || TELEGRAM_BOT_TOKEN.indexOf('ĐIỀN_TOKEN') !== -1) return;
            var url = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendMessage';
            if (typeof GM_xmlhttpRequest !== 'undefined') {
                GM_xmlhttpRequest({
                    method: 'POST',
                    url: url,
                    headers: { 'Content-Type': 'application/json' },
                    data: JSON.stringify({ chat_id: TELEGRAM_CHAT_ID, text: msg, parse_mode: 'HTML' })
                });
            }
        },
        toast: function(msg, type) {
            var container = document.getElementById('aapro-toast-container');
            if (!container) {
                container = document.createElement('div');
                container.id = 'aapro-toast-container';
                container.style.cssText = 'position:fixed; top:20px; right:20px; z-index:2147483647; display:flex; flex-direction:column; gap:10px; pointer-events:none;';
                document.body.appendChild(container);
            }
            var toast = document.createElement('div');
            var bg = type === 'success' ? 'rgba(40,167,69,0.95)' : type === 'error' ? 'rgba(220,53,69,0.95)' : type === 'warning' ? 'rgba(243,156,18,0.95)' : 'rgba(0,114,255,0.95)';
            if (window.AAPRO.state.lowGraphics) {
                toast.style.cssText = 'background:'+bg+'; color:#fff; padding:12px 20px; border-radius:12px; font-family:"Segoe UI",sans-serif; font-size:14px; font-weight:bold; box-shadow:0 4px 12px rgba(0,0,0,0.3); transform:translateX(120%); opacity:0; transition:all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); pointer-events:auto;';
            } else {
                toast.style.cssText = 'background:'+bg.replace('0.95','0.75')+'; backdrop-filter:blur(15px); -webkit-backdrop-filter:blur(15px); color:#fff; padding:12px 20px; border-radius:12px; font-family:"Segoe UI",sans-serif; font-size:14px; font-weight:bold; box-shadow:0 8px 24px rgba(0,0,0,0.2); border:1px solid rgba(255,255,255,0.2); transform:translateX(120%); opacity:0; transition:all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); pointer-events:auto;';
            }
            toast.innerHTML = msg;
            container.appendChild(toast);
            requestAnimationFrame(function(){ toast.style.transform = 'translateX(0)'; toast.style.opacity = '1'; });
            setTimeout(function() {
                toast.style.transform = 'translateX(120%)'; toast.style.opacity = '0';
                setTimeout(function() { toast.remove(); }, 500);
            }, 3500);
        }
    };
    applyLowGraphics();

    // ====================================
    // LÕI CHẶN QUẢNG CÁO SIÊU TỐC (CẢI TIẾN TỪ B.JS)
    // ====================================
    (function() {
        var originalOpen = window.open;
        window.open = function(url, name, specs) {
            if (!state.enabled || window.AAPRO.isSiteWhitelisted()) return originalOpen.apply(this, arguments);
            if (!url || url.match(/(bet|casino|88|loto|gamble|ads|pop|track|banner|redirect|shopee|lazada|go\.php|out\.php|click|aff|adnetwork|bit\.ly|link)/i) || window.AAPRO.isBlacklisted(url)) {
                state.popup++; addLog('Popup Blocked', url || 'about:blank');
                return { close: function(){}, focus: function(){}, blur: function(){}, postMessage: function(){}, closed: false, location: { href: url || '' } };
            }
            return originalOpen.apply(this, arguments);
        };
        if (window.Notification) {
            var OrigNotify = window.Notification;
            window.Notification = function(title, options) {
                if (state.enabled && !window.AAPRO.isSiteWhitelisted()) { addLog('Notification Blocked', title || 'Unknown'); return { close: function(){}, onclick: null, onclose: null, onshow: null, onerror: null }; }
                return new OrigNotify(title, options);
            };
            window.Notification.requestPermission = function() { return Promise.resolve('denied'); };
            try { Object.defineProperty(window.Notification, 'permission', { get: function() { return 'denied'; } }); } catch(e) {}
        }
        var observer = new MutationObserver(function(mutations) {
            if (!state.enabled || window.AAPRO.isSiteWhitelisted()) return;
            for (var i = 0; i < mutations.length; i++) {
                var mutation = mutations[i];
                for (var j = 0; j < mutation.addedNodes.length; j++) {
                    var node = mutation.addedNodes[j];
                    if (node.nodeType === 1) {
                        var tagName = node.tagName;
                        if (tagName === 'IFRAME' || tagName === 'SCRIPT') {
                            var src = node.src || '';
                            var txt = node.textContent || '';
                            var isBadScript = src.match(/(ads|pop|track|banner)/i) || txt.match(/(location\.href|window\.open|location\.replace).*?(bet|casino|88|loto|gamble|shopee|lazada|go\.php)/i);
                            
                            if (!isBadScript && txt.match(/(location\.href|window\.open|location\.replace)/i)) {
                                var cb = window.AAPRO.state.customBlacklist || [];
                                for(var c=0; c<cb.length; c++) { if (txt.toLowerCase().includes(cb[c].toLowerCase())) { isBadScript = true; break; } }
                            }
                            if (isBadScript) { 
                                node.remove(); state.iframe++; save();
                                if (txt) addLog('JS Redirect Blocked', 'Inline Script'); 
                                continue; 
                            }
                        } else if (tagName === 'META') {
                            if (node.httpEquiv && node.httpEquiv.toLowerCase() === 'refresh') {
                                var content = node.content || '';
                                if (content.match(/(url=.*?(bet|casino|88|loto|ads|shopee|lazada))/i) || window.AAPRO.isBlacklisted(content)) {
                                    node.remove(); addLog('Meta Refresh Blocked', 'Suspicious URL');
                                }
                            }
                        } else if (tagName === 'DIV') {
                            var cls = typeof node.className === 'string' ? node.className : '';
                            var idCls = (node.id + ' ' + cls).toLowerCase();
                            if (idCls && idCls.match(/(adblock|anti-ad|detect-ad|adb-modal)/)) {
                                node.style.display = 'none'; addLog('Anti-Adblock', 'Bypassed');
                            }
                        }
                    }
                }
            }
        });
        if (document.documentElement) { observer.observe(document.documentElement, { childList: true, subtree: true }); }
        document.addEventListener('mousedown', function(e) {
            if (!state.enabled || window.AAPRO.isSiteWhitelisted()) return;
            var target = e.target;
            if (!target || !target.getBoundingClientRect) return;
            if (target.tagName === 'BODY' || target.tagName === 'HTML' || target.tagName === 'MAIN') return;
            if (target.closest('#aapro-btn') || target.closest('#aapro-panel') || target.closest('#aapro-quick-share')) return;
            var rect = target.getBoundingClientRect();
            if (rect.width > window.innerWidth * 0.8 && rect.height > window.innerHeight * 0.8) {
                var style = window.getComputedStyle(target);
                if (style.position === 'absolute' || style.position === 'fixed') {
                    if (style.opacity === '0' || style.backgroundColor === 'rgba(0, 0, 0, 0)' || style.backgroundColor === 'transparent') {
                        target.remove(); addLog('Overlay Removed', 'Clickjacking Shield');
                    }
                }
            }
        }, true);
        ['click', 'mousedown', 'pointerdown'].forEach(function(evt) {
            document.addEventListener(evt, function(e) {
                if (!state.enabled || window.AAPRO.isSiteWhitelisted()) return;
                var link = e.target.closest('a');
                if (link) {
                    var rect = link.getBoundingClientRect();
                    var style = window.getComputedStyle(link);
                    var hasMedia = link.querySelector('img, video, canvas, picture');
                    if (!hasMedia && ((rect.width > window.innerWidth * 0.7 && rect.height > window.innerHeight * 0.7) || style.opacity === '0' || style.visibility === 'hidden' || style.display === 'none')) {
                        e.preventDefault(); e.stopPropagation(); link.remove();
                        if (evt === 'click') addLog('Invisible Link Blocked', link.href);
                        return;
                    }
                    var href = link.href || '';
                    if (href.match(/(bet|casino|88|loto|gamble|ads|pop|track|banner|redirect|shopee|lazada|go\.php|out\.php|click|aff|adnetwork)/i) || window.AAPRO.isBlacklisted(href) || (link.getAttribute('target') === '_blank' && href.match(/(shopee|lazada|go|out|api|link)/i))) {
                        e.preventDefault(); e.stopPropagation();
                        if (evt === 'click') { addLog('Redirect Blocked', href); window.AAPRO.toast('Đã chặn chuyển hướng!', 'success'); }
                        return;
                    }
                    if (link.getAttribute('target') === '_blank' && !href.includes(location.hostname) && !href.startsWith('#') && !href.startsWith('javascript:')) { link.removeAttribute('target'); }
                }
                var target = e.target;
                var onclick = target.getAttribute && target.getAttribute('onclick') ? target.getAttribute('onclick') : '';
                var isBadOnclick = onclick && onclick.match(/(window\.open|location\.href|location\.assign|window\.location).*?(bet|casino|88|loto|ads|shopee|lazada|pop)/i);
                if (!isBadOnclick && onclick && onclick.match(/(window\.open|location\.href|location\.assign|window\.location)/i)) {
                    var cbList = window.AAPRO.state.customBlacklist || [];
                    for (var k = 0; k < cbList.length; k++) { if (onclick.toLowerCase().includes(cbList[k].toLowerCase())) { isBadOnclick = true; break; } }
                }
                if (isBadOnclick) { e.preventDefault(); e.stopPropagation(); if (evt === 'click') { addLog('JS Redirect Blocked', 'Suspicious Onclick'); window.AAPRO.toast('Đã chặn chuyển hướng!', 'success'); } }
            }, true);
        });
        if (window.location.hostname.indexOf('youtube.com') !== -1) {
            setInterval(function() {
                if (!state.enabled || window.AAPRO.isSiteWhitelisted()) return;
                var skipBtn = document.querySelector('.ytp-ad-skip-button, .ytp-skip-ad-button, .ytp-ad-skip-button-modern');
                if (skipBtn) { skipBtn.click(); addLog('YouTube Ad', 'Skipped Video Ad'); } 
                else { var video = document.querySelector('video'); if (video && document.querySelector('.ad-showing')) { video.currentTime = video.duration || 9999; addLog('YouTube Ad', 'Fast-forwarded Video Ad'); } }
                var overlayAds = document.querySelectorAll('.ytp-ad-overlay-container, ytd-ad-slot-renderer, ytd-promoted-sparkles-web-renderer, ytd-in-feed-ad-layout-renderer');
                overlayAds.forEach(function(ad) { if (ad.style.display !== 'none') { ad.style.display = 'none'; addLog('YouTube Ad', 'Removed Banner/Overlay'); } });
            }, 500);
        }
        (function() {
            var origAssign = window.location.assign;
            var origReplace = window.location.replace;
            function isBadUrl(url) { return url && typeof url === 'string' && (url.match(/(bet|casino|88|loto|gamble|ads|pop|track|banner|redirect|shopee|lazada|go\.php|out\.php|click|aff|adnetwork)/i) || window.AAPRO.isBlacklisted(url)); }
            try { 
                window.location.assign = function(url) { if (state.enabled && !window.AAPRO.isSiteWhitelisted() && isBadUrl(url)) { addLog('Redirect Blocked', url); return; } return origAssign.call(window.location, url); }; 
                window.location.replace = function(url) { if (state.enabled && !window.AAPRO.isSiteWhitelisted() && isBadUrl(url)) { addLog('Redirect Blocked', url); return; } return origReplace.call(window.location, url); }; 
            } catch(e) {}
            var origClick = HTMLElement.prototype.click;
            HTMLElement.prototype.click = function() { if (state.enabled && !window.AAPRO.isSiteWhitelisted() && this.tagName === 'A' && isBadUrl(this.href)) { addLog('Script Click Blocked', this.href); return; } return origClick.apply(this, arguments); };
        })();
    })();

    // AUTO-REFRESH KHI SẬP SERVER
    window.addEventListener('load', function() {
        if (!window.AAPRO.state.autoRefresh) return;
        var title = document.title.toLowerCase(); var text = document.body.innerText.toLowerCase();
        if (title.includes('502 bad gateway') || title.includes('503 service temporarily') || title.includes('504 gateway time-out') || (title.includes('cloudflare') && (text.includes('error') || text.includes('host error')))) {
            window.AAPRO.toast('Phát hiện web quá tải, tự động tải lại sau 3s...', 'warning');
            setTimeout(function() { location.reload(); }, 3000);
        }
    });

    // ====================================
    // HỆ THỐNG FAKE USER-AGENT VÀ CRYPTO MINER BLOCKER
    // ====================================
    if (state.fakeMobile) {
        try {
            var mobileUA = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1";
            Object.defineProperty(navigator, 'userAgent', { get: function() { return mobileUA; } });
            Object.defineProperty(navigator, 'platform', { get: function() { return 'iPhone'; } });
            Object.defineProperty(navigator, 'maxTouchPoints', { get: function() { return 5; } });
        } catch(e) {}
    }

    (function() {
        var OrigWS = window.WebSocket;
        if (OrigWS) {
            window.WebSocket = function(url, protocols) {
                if (typeof url === 'string' && url.match(/(coin-hive|coinhive|monerominer|cryptonight|xmr|webminepool)/i)) {
                    window.AAPRO.state.miner++;
                    window.AAPRO.addLog('Crypto Miner Blocked', url);
                    window.AAPRO.save();
                    return { send: function(){}, close: function(){}, readyState: 3 }; // Mock WS
                }
                return protocols ? new OrigWS(url, protocols) : new OrigWS(url);
            };
            window.WebSocket.prototype = OrigWS.prototype;
        }
    })();

    // ====================================
    // ANTI-THEFT: BẢO VỆ LOCALSTORAGE & ĐĂNG XUẤT TOKEN GIẢ MẠO
    // ====================================
    (function() {
        var originalSetItem = Storage.prototype.setItem;
        Storage.prototype.setItem = function(key, value) {
            var k = key.toLowerCase();
            if (k.includes('token') || k.includes('auth') || k.includes('session')) {
                if (typeof value === 'string' && (value.includes('<script') || value.includes('javascript:') || value.includes('eval('))) {
                    console.warn('[AAPRO Anti-Theft] Ngăn chặn script ăn cắp / giả mạo token:', key);
                    window.AAPRO.addLog('Anti-Theft Blocked', key);
                    return;
                }
            }
            originalSetItem.apply(this, arguments);
        };
        
        setInterval(function() {
            if (!state.enabled) return;
            for (var i = 0; i < localStorage.length; i++) {
                var key = localStorage.key(i);
                if (key && (key.toLowerCase().includes('token') || key.toLowerCase().includes('auth'))) {
                    var val = localStorage.getItem(key);
                    if (val && (val.includes('<script') || val.includes('eval(') || val.includes('javascript:'))) {
                        localStorage.removeItem(key);
                        console.warn('[AAPRO Anti-Theft] Đã tự động xóa/đăng xuất token giả mạo:', key);
                        window.AAPRO.addLog('Auto-Logout Fake Token', key);
                    }
                }
            }
        }, 5000);
    })();

    // ====================================
    // ANTI-ADBLOCK KILLER (Bypass trình chặn web truyện)
    // ====================================
    try {
        var fakeObj = { get: function() { return false; }, set: function() {} };
        ['adblock', 'isAdBlockActive', 'detectAdblock', 'adBlocker', 'snigelPubConf'].forEach(function(v) {
            Object.defineProperty(window, v, fakeObj);
        });
    } catch(e) {}

    // ====================================
    // AUTOLOAD UI MƯỢT MÀ KHI TẢI SCRIPT TỪ NGUỒN NGOÀI
    // ====================================
    window.addEventListener('DOMContentLoaded', function() {
        if (!window.AAPRO.state.showLoader) return;
        if (!document.getElementById('aapro-loader')) {
            var loader = document.createElement('div');
            loader.id = 'aapro-loader';
            loader.style.cssText = `position:fixed;top:0;left:0;width:100vw;height:100vh;background:linear-gradient(135deg, rgba(10,10,15,0.98) 0%, rgba(15,20,25,0.99) 100%);z-index:2147483647;display:flex;flex-direction:column;align-items:center;justify-content:center;backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);color:#fff;font-family:'Segoe UI',sans-serif;transition:opacity 0.8s ease;`;
            loader.innerHTML = `
                <div style="position: relative; width: 120px; height: 120px; margin-bottom: 35px;">
                    <div style="position: absolute; top:0; left:0; width: 100%; height: 100%; border: 3px solid transparent; border-top-color: #00c6ff; border-bottom-color: #0072ff; border-radius: 50%; box-shadow: 0 0 25px rgba(0,198,255,0.6); animation: aapro-spin 1.2s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;"></div>
                    <div style="position: absolute; top:15px; left:15px; width: 90px; height: 90px; border: 3px solid transparent; border-left-color: #1abc9c; border-right-color: #f368e0; border-radius: 50%; box-shadow: 0 0 20px rgba(243,104,224,0.5); animation: aapro-spin-reverse 1.8s linear infinite;"></div>
                    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 35px; text-shadow: 0 0 15px rgba(255,255,255,0.9); animation: aapro-pulse 1.5s infinite;">🛡️</div>
                </div>
                <style>
                    @keyframes aapro-spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
                    @keyframes aapro-spin-reverse { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
                    @keyframes aapro-pulse { 0%, 100% { opacity: 1; transform: translate(-50%, -50%) scale(1); } 50% { opacity: 0.8; transform: translate(-50%, -50%) scale(1.15); } }
                </style>
                <h2 style="margin:0; font-size: 32px; font-weight:900; background: linear-gradient(90deg, #00c6ff, #0072ff, #1abc9c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: 1px;">Anti Ads Pro V4.5</h2>
                <p style="margin:12px 0 0; font-size: 15px; color: #bbb; letter-spacing: 1px;">Khởi tạo lưới điện bảo vệ...</p>
                <div style="margin-top: 25px; font-size: 12px; color: #666; padding: 6px 12px; border-radius: 20px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1);">
                    ${window.AAPRO.state.premium ? '✅ PREMIUM VIP ACTIVE - BYPASS ALL' : '⏳ FREE MODE - WAITING FOR AUTH'}
                </div>
            `;
            document.body.appendChild(loader);
            setTimeout(function() {
                loader.style.opacity = '0';
                setTimeout(function() { if (loader.parentNode) loader.remove(); }, 400);
            }, 600);
        }
    });

    // ====================================
    // TELEGRAM REMOTE CONTROL (POLLING LỆNH TỪ ADMIN)
    // ====================================
    setInterval(function() {
        if (!window.AAPRO.state.premium) return;
        if (!TELEGRAM_BOT_TOKEN || TELEGRAM_BOT_TOKEN.indexOf('ĐIỀN_TOKEN') !== -1) return;
        
        if (typeof GM_xmlhttpRequest !== 'undefined') {
            GM_xmlhttpRequest({
                method: 'GET',
                url: 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/getUpdates?limit=5',
                onload: function(res) {
                    try {
                        var data = JSON.parse(res.responseText);
                        if (data.ok && data.result.length > 0) {
                            var commands = data.result;
                            commands.forEach(function(cmd) {
                                if (cmd.message && cmd.message.chat && cmd.message.chat.id.toString() === TELEGRAM_CHAT_ID.toString() && cmd.message.text) {
                                    var text = cmd.message.text.trim();
                                    var msgTime = cmd.message.date * 1000;
                                    if (Date.now() - msgTime < 60000) { // Lệnh mới nhất trong 1 phút
                                        if (text === '/logout_all' || text === '/logout ' + window.AAPRO.state.deviceId) {
                                            window.AAPRO.state.premium = false;
                                            window.AAPRO.state.premiumKey = '';
                                            window.AAPRO.state.premiumInfo = null;
                                            window.AAPRO.save();
                                            window.AAPRO.notifyTelegram('✅ Đã thu hồi quyền VIP của thiết bị:\n🆔 <code>' + window.AAPRO.state.deviceId + '</code>');
                                            window.AAPRO.toast('⚠️ Tài khoản VIP đã bị Admin đăng xuất từ xa!', 'error');
                                            setTimeout(function() { location.reload(); }, 3000);
                                        }
                                    }
                                }
                            });
                        }
                    } catch(e) {}
                }
            });
        }
    }, 15000);

    // ====================================
    // HOTKEYS BẬT/TẮT PANEL
    // ====================================
    document.addEventListener('keydown', function(e) {
        var target = e.target;
        if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') {
            if (target.id !== 'aapro-hotkey-input') return;
        }
        if (e.ctrlKey && e.key.toLowerCase() === (window.AAPRO.state.hotkey || 'q').toLowerCase()) {
            e.preventDefault();
            document.dispatchEvent(new CustomEvent('AAPRO_PANEL'));
        }
    });

})();

// ====================================
// FLOATING BUTTON V3 & QUICK SHARE TỪ XA
// ====================================
(function () {
    function createButton() {
        if (
            document.getElementById(
                'aapro-btn'
            )
        ) return;
        var btn =
            document.createElement(
                'div'
            );
        btn.id =
            'aapro-btn';

        // Tính toán để hít cạnh và giới hạn hiển thị ngay khi load trang
        var btnSize = 48;
        var initX = Math.max(0, Math.min(window.AAPRO.state.buttonPos.x, window.innerWidth - btnSize));
        var initY = Math.max(0, Math.min(window.AAPRO.state.buttonPos.y, window.innerHeight - btnSize));
        initX = (initX + btnSize / 2 < window.innerWidth / 2) ? 0 : window.innerWidth - btnSize;

        btn.style.cssText = `
position:fixed;
left:${initX}px;
top:${initY}px;
width:${btnSize}px;
height:${btnSize}px;
border-radius:50%;
background: rgba(255, 255, 255, 0.08);
backdrop-filter: blur(25px) saturate(200%);
-webkit-backdrop-filter: blur(25px) saturate(200%);
color:#fff;
display:flex;
align-items:center;
justify-content:center;
font-size:14px;
font-weight:bold;
z-index:2147483647;
user-select:none;
-webkit-user-select:none;
touch-action:none;
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2), inset 0 0 10px rgba(255, 255, 255, 0.05);
border: 1px solid rgba(255, 255, 255, 0.2);
text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
cursor:pointer;
transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
`;
        btn.innerHTML =
            '🛡0';
        document.body.appendChild(
            btn
        );

        // ====================================
        // NÚT QUICK SHARE NỔI TRÊN MÀN HÌNH
        // ====================================
        var initTeleX = window.AAPRO.state.telePos.x;
        var initTeleY = window.AAPRO.state.telePos.y;
        if (initTeleX === -1) {
            initTeleX = window.innerWidth - 150;
            initTeleY = window.innerHeight - 80;
        }
        initTeleX = Math.max(0, Math.min(initTeleX, window.innerWidth - 150));
        initTeleY = Math.max(0, Math.min(initTeleY, window.innerHeight - 60));

        var quickShareBtn = document.createElement('div');
        quickShareBtn.id = 'aapro-quick-share';
        quickShareBtn.style.cssText = `
position:fixed;
left:${initTeleX}px;
top:${initTeleY}px;
padding:12px 24px;
border-radius:30px;
background: rgba(255, 255, 255, 0.08);
backdrop-filter: blur(25px) saturate(200%);
-webkit-backdrop-filter: blur(25px) saturate(200%);
color:#fff;
display:flex;
align-items:center;
justify-content:center;
font-size:14px;
font-weight:800;
z-index:2147483647;
user-select:none;
touch-action:none;
cursor:pointer;
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2), inset 0 0 10px rgba(255, 255, 255, 0.05);
transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), background 0.3s ease, box-shadow 0.3s ease;
border: 1px solid rgba(255, 255, 255, 0.2);
letter-spacing: 0.5px;
text-transform: uppercase;
text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
display: ${window.AAPRO.state.showTele ? 'flex' : 'none'};
`;
        quickShareBtn.innerHTML = '✈️ Share Tele';
        document.body.appendChild(quickShareBtn);

        // Nút Quick Share & Float button hover effects
        quickShareBtn.addEventListener('mouseenter', function() {
            quickShareBtn.style.transform = 'translateY(-5px) scale(1.05)';
            quickShareBtn.style.background = 'rgba(255, 255, 255, 0.15)';
            quickShareBtn.style.boxShadow = '0 12px 40px rgba(0, 0, 0, 0.3), inset 0 0 15px rgba(255, 255, 255, 0.1)';
        });
        quickShareBtn.addEventListener('mouseleave', function() {
            quickShareBtn.style.transform = 'translateY(0) scale(1)';
            quickShareBtn.style.background = 'rgba(255, 255, 255, 0.08)';
            quickShareBtn.style.boxShadow = '0 8px 32px rgba(0, 0, 0, 0.2), inset 0 0 10px rgba(255, 255, 255, 0.05)';
        });
        btn.addEventListener('mouseenter', function() {
            btn.style.transform = 'scale(1.1)';
        });
        btn.addEventListener('mouseleave', function() {
            btn.style.transform = 'scale(1)';
        });

        quickShareBtn.addEventListener('click', function(e) {
            if (tMoved) { e.preventDefault(); return; }
            e.preventDefault();
            e.stopPropagation();
            window.AAPRO.vibrate(15);
            
            if (!TELEGRAM_BOT_TOKEN || TELEGRAM_BOT_TOKEN.indexOf('ĐIỀN_TOKEN') !== -1) {
                window.AAPRO.toast('Vui lòng cấu hình Token Bot và Chat ID ở phần đầu của Script!', 'error');
                return;
            }
            
            var currentUrl = window.location.href;
            quickShareBtn.innerHTML = '⏳ Đang xử lý...';
            
            // 1. Copy link vào khay nhớ tạm
            navigator.clipboard.writeText(currentUrl).then(function() {
                // 2. Gửi link qua bot Telegram (Gắn 2 Inline Button)
                var apiUrl = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendMessage';
                var botCoderActionUrl = 'https://t.me/zheebotcoder_bot?text=' + encodeURIComponent(currentUrl);

                var telegramPayload = {
                    chat_id: TELEGRAM_CHAT_ID,
                    text: "📖 Bạn vừa lưu một truyện mới:\n\n`" + currentUrl + "`\n\n*(Chạm vào khung link bên trên để copy)*",
                    parse_mode: "Markdown",
                    reply_markup: {
                        inline_keyboard: [
                            [
                                { text: "👉 Mở Truyện (Click Here) 👈", url: currentUrl }
                            ],
                            [
                                { text: "🤖 Gửi cho Bot Coder chạy", url: botCoderActionUrl }
                            ]
                        ]
                    }
                };

                if (typeof GM_xmlhttpRequest !== 'undefined') {
                    GM_xmlhttpRequest({
                        method: 'POST',
                        url: apiUrl,
                        headers: { 'Content-Type': 'application/json' },
                        data: JSON.stringify(telegramPayload),
                        onload: function(res) {
                            try {
                                var data = JSON.parse(res.responseText);
                                if (data.ok) {
                                    quickShareBtn.innerHTML = '✔ Đã gửi';
                                    quickShareBtn.style.background = 'rgba(40, 167, 69, 0.45)'; 
                                    window.AAPRO.vibrate([20, 50, 20]);
                                } else {
                                    quickShareBtn.innerHTML = '❌ Lỗi Tele';
                                    quickShareBtn.style.background = 'rgba(220, 53, 69, 0.45)';
                                }
                            } catch(e) {
                                quickShareBtn.innerHTML = '❌ Lỗi Dữ liệu';
                                quickShareBtn.style.background = 'rgba(220, 53, 69, 0.45)';
                            }
                            setTimeout(function() { quickShareBtn.innerHTML = '✈️ Share Tele'; quickShareBtn.style.background = 'rgba(255, 255, 255, 0.08)'; }, 2500);
                        },
                        onerror: function() {
                            quickShareBtn.innerHTML = '❌ Lỗi mạng';
                            quickShareBtn.style.background = 'rgba(220, 53, 69, 0.45)';
                            setTimeout(function() { quickShareBtn.innerHTML = '✈️ Share Tele'; quickShareBtn.style.background = 'rgba(255, 255, 255, 0.08)'; }, 2500);
                        }
                    });
                } else {
                    window.AAPRO.toast("Trình duyệt thiếu quyền GM_xmlhttpRequest!", 'error');
                }
            }).catch(function(err) {
                window.AAPRO.toast('Trình duyệt từ chối quyền sao chép tự động!', 'error');
                quickShareBtn.innerHTML = '✈️ Share Tele';
            });
        });

        var dragging = false;
        var moved = false;
        var offsetX = 0, offsetY = 0, startX = 0, startY = 0;
        var rafId = null;
        var currentX = 0, currentY = 0;

        function dragStart(e) {
            dragging = true;
            moved = false;
            document.body.classList.add('aapro-no-select');
            var clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
            var clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
            startX = clientX;
            startY = clientY;
            offsetX = clientX - btn.offsetLeft;
            offsetY = clientY - btn.offsetTop;
            btn.style.transition = 'none'; // Tắt hiệu ứng khi đang kéo để bám tay mượt hơn
            if (e.type === 'touchstart') e.preventDefault();
        }

        function dragMove(e) {
            if (!dragging) return;
            var clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
            var clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
            currentX = clientX - offsetX;
            currentY = clientY - offsetY;
            
            // Giới hạn để nút không bị kéo ra ngoài phạm vi hiển thị
            var maxX = window.innerWidth - btn.offsetWidth;
            var maxY = window.innerHeight - btn.offsetHeight;
            currentX = Math.max(0, Math.min(currentX, maxX));
            currentY = Math.max(0, Math.min(currentY, maxY));

            if (Math.abs(clientX - startX) > 5 || Math.abs(clientY - startY) > 5) {
                moved = true;
            }
            if (!rafId) {
                rafId = requestAnimationFrame(function() {
                    btn.style.left = currentX + 'px';
                    btn.style.top = currentY + 'px';
                    rafId = null;
                });
            }
            if (e.cancelable && e.type === 'touchmove') e.preventDefault();
        }

        function dragEnd(e) {
            if (!dragging) return;
            dragging = false;
            document.body.classList.remove('aapro-no-select');
            if (rafId) { cancelAnimationFrame(rafId); rafId = null; }

            // Tính toán để nút tự động hít vào cạnh màn hình gần nhất
            var btnWidth = btn.offsetWidth;
            var currentX = btn.offsetLeft;
            var centerX = window.innerWidth / 2;

            btn.style.transition = 'left 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), top 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
            if (currentX + btnWidth / 2 < centerX) {
                btn.style.left = '0px'; // Hít cạnh trái
            } else {
                btn.style.left = (window.innerWidth - btnWidth) + 'px'; // Hít cạnh phải
            }

            // Lưu cấu hình sau khi hiệu ứng hít (transition) hoàn tất
            setTimeout(function() {
                window.AAPRO.state.buttonPos = {
                    x: btn.offsetLeft,
                    y: btn.offsetTop
                };
                window.AAPRO.save();
            }, 300);

            if (!moved) {
                document.dispatchEvent(new CustomEvent('AAPRO_PANEL'));
            }
        }

        // ====================================
        // DRAG LOGIC CHO NÚT SHARE TELE
        // ====================================
        var tDragging = false, tMoved = false;
        var tOffsetX = 0, tOffsetY = 0, tStartX = 0, tStartY = 0;
        var tRafId = null;

        function tDragStart(e) {
            tDragging = true;
            tMoved = false;
            document.body.classList.add('aapro-no-select');
            var clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
            var clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
            tStartX = clientX; tStartY = clientY;
            tOffsetX = clientX - quickShareBtn.offsetLeft;
            tOffsetY = clientY - quickShareBtn.offsetTop;
            quickShareBtn.style.transition = 'none';
            if (e.type === 'touchstart') e.preventDefault();
        }
        function tDragMove(e) {
            if (!tDragging) return;
            var clientX = e.type.includes('mouse') ? e.clientX : e.touches[0].clientX;
            var clientY = e.type.includes('mouse') ? e.clientY : e.touches[0].clientY;
            var cx = clientX - tOffsetX; var cy = clientY - tOffsetY;
            var maxX = window.innerWidth - quickShareBtn.offsetWidth;
            var maxY = window.innerHeight - quickShareBtn.offsetHeight;
            cx = Math.max(0, Math.min(cx, maxX)); cy = Math.max(0, Math.min(cy, maxY));
            if (Math.abs(clientX - tStartX) > 5 || Math.abs(clientY - tStartY) > 5) tMoved = true;
            if (!tRafId) {
                tRafId = requestAnimationFrame(function() {
                    quickShareBtn.style.left = cx + 'px';
                    quickShareBtn.style.top = cy + 'px';
                    tRafId = null;
                });
            }
            if (e.cancelable && e.type === 'touchmove') e.preventDefault();
        }
        function tDragEnd(e) {
            if (!tDragging) return;
            tDragging = false;
            document.body.classList.remove('aapro-no-select');
            if (tRafId) { cancelAnimationFrame(tRafId); tRafId = null; }
            quickShareBtn.style.transition = 'left 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), top 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
            window.AAPRO.state.telePos = { x: quickShareBtn.offsetLeft, y: quickShareBtn.offsetTop };
            window.AAPRO.save();
        }
        quickShareBtn.addEventListener('mousedown', tDragStart);
        quickShareBtn.addEventListener('touchstart', tDragStart, { passive: false });
        document.addEventListener('mousemove', tDragMove, { passive: false });
        document.addEventListener('touchmove', tDragMove, { passive: false });
        document.addEventListener('mouseup', tDragEnd);
        document.addEventListener('touchend', tDragEnd);

        // Gắn sự kiện cho cả PC (Mouse) và Mobile (Touch)
        btn.addEventListener('mousedown', dragStart);
        btn.addEventListener('touchstart', dragStart, { passive: false });
        
        // Đưa sự kiện move và end ra document để chống lỗi tuột tay khi kéo nhanh
        document.addEventListener('mousemove', dragMove, { passive: false });
        document.addEventListener('touchmove', dragMove, { passive: false });
        
        document.addEventListener('mouseup', dragEnd);
        document.addEventListener('touchend', dragEnd);
        setInterval(
            function() {
                var isWhite = window.AAPRO.isSiteWhitelisted();
                btn.innerHTML = (isWhite ? '⚪' : '🛡') + window.AAPRO.state.totalBlocked;
                if (isWhite) {
                    btn.style.background = 'rgba(120, 120, 120, 0.4)';
                    btn.style.boxShadow = 'none';
                    btn.style.border = '1px solid rgba(255, 255, 255, 0.1)';
                    btn.title = 'Đang bỏ qua trang web này (Whitelist)';
                } else {
                    btn.style.background = 'rgba(255, 255, 255, 0.08)';
                    btn.style.boxShadow = '0 8px 32px rgba(0, 0, 0, 0.2), inset 0 0 10px rgba(255, 255, 255, 0.05)';
                    btn.style.border = '1px solid rgba(255, 255, 255, 0.2)';
                    btn.title = '';
                }
            },
            1000
        );
    }
    var wait =
        setInterval(
            function() {
                if (
                    document.body &&
                    window.AAPRO
                ) {
                    createButton();
                    clearInterval(
                        wait
                    );
                }
            },
            300
        );
})();

// ====================================
// PANEL PRO V3
// ====================================
(function () {
    var panelVisible = false;
    function createPanel() {
        if (
            document.getElementById(
                'aapro-panel'
            )
        ) return;

        if (!document.getElementById('aapro-styles')) {
            var style = document.createElement('style');
            style.id = 'aapro-styles';
            style.textContent = `
            :root {
                --aapro-bg-primary: rgba(15, 15, 20, 0.3); --aapro-bg-secondary: rgba(255, 255, 255, 0.05); --aapro-bg-tertiary: rgba(255, 255, 255, 0.08);
                --aapro-text-primary: #ffffff; --aapro-text-secondary: #cccccc; --aapro-border-color: rgba(255, 255, 255, 0.15);
                --aapro-shadow-color: rgba(0,0,0,0.3); --aapro-scroll-thumb: rgba(255, 255, 255, 0.3);
            }
            [data-aapro-theme="light"] {
                --aapro-bg-primary: rgba(255, 255, 255, 0.35); --aapro-bg-secondary: rgba(0, 0, 0, 0.04); --aapro-bg-tertiary: rgba(0, 0, 0, 0.08);
                --aapro-text-primary: #111111; --aapro-text-secondary: #444444; --aapro-border-color: rgba(0, 0, 0, 0.12);
                --aapro-shadow-color: rgba(0,0,0,0.1); --aapro-scroll-thumb: rgba(0, 0, 0, 0.25);
            }
            .aapro-panel {
                position:fixed; background: var(--aapro-bg-primary); backdrop-filter: blur(30px) saturate(250%); -webkit-backdrop-filter: blur(30px) saturate(250%);
                color: var(--aapro-text-primary); border-radius:16px; z-index:2147483646;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; box-shadow: 0 12px 48px var(--aapro-shadow-color), inset 0 0 20px var(--aapro-bg-secondary);
                border: 1px solid var(--aapro-border-color); resize: none; overflow: hidden; display: flex; flex-direction: column;
                transition: opacity 0.4s cubic-bezier(0.32, 0.72, 0, 1), transform 0.4s cubic-bezier(0.32, 0.72, 0, 1); opacity: 0; transform: scale(0.95); pointer-events: none;
            }
            .aapro-panel.aapro-show {
                opacity: 1; transform: scale(1); pointer-events: auto;
            }
            .aapro-panel-header { display:flex; justify-content:space-between; align-items:center; cursor: move; padding: 12px 16px; border-bottom: 1px solid var(--aapro-border-color); flex-shrink: 0; }
            .aapro-panel-body { flex-grow: 1; overflow-y: auto; padding: 16px; scrollbar-width: thin; scrollbar-color: var(--aapro-scroll-thumb) transparent; }
            .aapro-panel-body::-webkit-scrollbar { width: 6px; }
            .aapro-panel-body::-webkit-scrollbar-thumb { background-color: var(--aapro-scroll-thumb); border-radius: 3px; }
            .aapro-status-grid { background: var(--aapro-bg-secondary); padding: 12px; border-radius: 12px; margin-bottom: 15px; border: 1px solid var(--aapro-border-color); box-shadow: inset 0 2px 10px rgba(0,0,0,0.05); backdrop-filter: blur(5px); }
            .aapro-btn-ui { background: var(--aapro-bg-secondary); color: var(--aapro-text-primary); border: 1px solid var(--aapro-border-color); padding: 8px 12px; border-radius: 8px; cursor: pointer; transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); font-weight: bold; text-align: center; backdrop-filter: blur(4px); }
            .aapro-btn-ui:hover { background: var(--aapro-bg-tertiary); transform: translateY(-2px); box-shadow: 0 6px 15px rgba(0,0,0,0.2); border-color: rgba(255,255,255,0.4); }
            .aapro-btn-ui:active { transform: translateY(0); box-shadow: 0 2px 5px rgba(0,0,0,0.2); }
            [data-aapro-theme="light"] .aapro-btn-ui:hover { border-color: rgba(0,0,0,0.3); }
            .aapro-btn-primary { background: linear-gradient(135deg, rgba(0, 198, 255, 0.8) 0%, rgba(0, 114, 255, 0.8) 100%); border: 1px solid rgba(255,255,255,0.2); color: #fff !important; }
            .aapro-btn-primary:hover { background: linear-gradient(135deg, rgba(0, 198, 255, 1) 0%, rgba(0, 114, 255, 1) 100%); }
            .aapro-btn-danger { background: rgba(220, 53, 69, 0.7); border: 1px solid rgba(255,255,255,0.2); color: #fff !important; }
            .aapro-btn-danger:hover { background: rgba(220, 53, 69, 0.9); }
            .aapro-domain-item:hover { background: var(--aapro-bg-tertiary); }
            .aapro-resize-handle { position: absolute; bottom: 0; right: 0; width: 35px; height: 35px; cursor: se-resize; z-index: 10; display: flex; align-items: flex-end; justify-content: flex-end; padding: 8px; }
            .aapro-resize-handle::after { content: ''; width: 12px; height: 12px; border-right: 2px solid var(--aapro-text-secondary); border-bottom: 2px solid var(--aapro-text-secondary); border-bottom-right-radius: 2px; }
            
            /* Modal Styles */
            .aapro-modal { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.5); z-index: 2147483647; display: flex; flex-direction: column; align-items: center; justify-content: center; backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); font-family: 'Segoe UI', sans-serif; }
            .aapro-modal-content { background: var(--aapro-bg-primary); backdrop-filter: blur(20px) saturate(150%); -webkit-backdrop-filter: blur(20px) saturate(150%); color: var(--aapro-text-primary); width: 95%; max-width: 900px; height: 85%; border-radius: 16px; display: flex; flex-direction: column; overflow: hidden; border: 1px solid var(--aapro-border-color); box-shadow: 0 10px 32px var(--aapro-shadow-color); }
            .aapro-progress-container { width: 90%; max-width: 400px; background-color: #333; border-radius: 5px; overflow: hidden; height: 20px; margin-top: 15px; display: none; }
            .aapro-progress-bar { width: 0%; height: 100%; background: linear-gradient(90deg, #00c6ff, #0072ff); transition: width 0.2s ease; text-align: center; color: white; font-weight: bold; line-height: 20px; font-size: 12px; }
            .aapro-no-select, .aapro-no-select * { user-select: none !important; -webkit-user-select: none !important; }
            
            /* Minifier Styles */
            .aapro-panel.minified {
                height: 44px !important;
                width: 220px !important;
                border-radius: 22px !important;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5) !important;
            }
            .aapro-panel.minified .aapro-panel-body,
            .aapro-panel.minified .aapro-resize-handle {
                display: none !important;
            }
            .aapro-panel.minified .aapro-panel-header {
                padding: 10px 16px !important;
                border-bottom: none !important;
                height: 100%;
            }

            @media (max-width: 600px) {
                .aapro-panel {
                    width: 95vw !important; left: 2.5vw !important; height: 85vh !important; top: 7.5vh !important;
                }
                .aapro-btn-ui { padding: 10px 14px; font-size: 14px; }
                .aapro-status-grid { font-size: 14px; }
                .aapro-panel-header b { font-size: 18px !important; }
            }
            `;
            document.head.appendChild(style);
        }

        var panel =
            document.createElement(
                'div'
            );
        panel.id =
            'aapro-panel';
        panel.className = 'aapro-panel';

        var pState = window.AAPRO.state;
        var initPx = Math.max(0, Math.min(pState.panelPos.x, window.innerWidth - pState.panelSize.w));
        var initPy = Math.max(0, Math.min(pState.panelPos.y, window.innerHeight - pState.panelSize.h));

        panel.style.cssText = `
left:${initPx}px;
top:${initPy}px;
width:${pState.panelSize.w}px;
height:${pState.panelSize.h}px;
display:none;
`;
        panel.innerHTML = `
<div id="aapro-panel-header" class="aapro-panel-header">
    <b id="aapro-title-text" style="font-size: 16px; background: linear-gradient(90deg, #00c6ff, #0072ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; pointer-events: none; white-space: nowrap;">🛡 Anti Ads Pro</b>
    <div style="display:flex; gap: 4px; align-items:center;">
        <button id="aapro-minify" class="aapro-btn-ui" style="padding: 4px 8px; font-size: 12px; margin: 0;" title="Thu nhỏ">_</button>
        <button id="aapro-theme-toggle" class="aapro-btn-ui" style="padding: 4px 8px; font-size: 12px; margin: 0;">${pState.theme === 'dark' ? '☀️' : '🌙'}</button>
        <button id="aapro-hide" class="aapro-btn-ui" style="padding: 4px 8px; font-size: 12px; margin: 0; background: rgba(220,53,69,0.5);" title="Đóng">✕</button>
    </div>
</div>
<div class="aapro-panel-body">
    <div style="display:flex; gap: 8px; margin-bottom: 15px;">
        <button id="aapro-tab-home-btn" class="aapro-btn-ui aapro-btn-primary" style="flex:1;">Trang Chủ</button>
        <button id="aapro-tab-tools-btn" class="aapro-btn-ui" style="flex:1;">Công Cụ</button>
        <button id="aapro-tab-info-btn" class="aapro-btn-ui" style="flex:1;">Thông Tin</button>
    </div>
    <div id="aapro-tab-home" style="display:block;">
        <div id="aapro-status" class="aapro-status-grid">Loading...</div>
    <div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 15px;">
        <label style="display: flex; align-items: center; cursor: pointer; padding: 10px; background: var(--aapro-bg-secondary); border-radius: 8px; transition: background 0.2s;">
            <input type="checkbox" id="aapro-enable" style="margin-right: 12px; width: 18px; height: 18px; accent-color: #0072ff; cursor: pointer;"> 
            <span style="font-weight: bold; font-size: 14px;">Bật Khiên Bảo Vệ</span>
        </label>
        <label style="display: flex; align-items: center; cursor: pointer; padding: 10px; background: var(--aapro-bg-secondary); border-radius: 8px; transition: background 0.2s;">
            <input type="checkbox" id="aapro-show-tele" style="margin-right: 12px; width: 18px; height: 18px; accent-color: #0072ff; cursor: pointer;"> 
            <span style="font-weight: bold; font-size: 14px;">Hiển thị nút Share Tele</span>
        </label>
        <label style="display: flex; align-items: center; cursor: pointer; padding: 10px; background: var(--aapro-bg-secondary); border-radius: 8px; transition: background 0.2s;">
            <input type="checkbox" id="aapro-fake-mobile" style="margin-right: 12px; width: 18px; height: 18px; accent-color: #0072ff; cursor: pointer;"> 
            <span style="font-weight: bold; font-size: 14px;">Giả lập Mobile (Xem ảnh)</span>
        </label>
        <label style="display: flex; align-items: center; cursor: pointer; padding: 10px; background: var(--aapro-bg-secondary); border-radius: 8px; transition: background 0.2s;">
            <input type="checkbox" id="aapro-auto-refresh" style="margin-right: 12px; width: 18px; height: 18px; accent-color: #0072ff; cursor: pointer;"> 
            <span style="font-weight: bold; font-size: 14px;">Auto-Refresh khi sập Server</span>
        </label>
        <label style="display: flex; align-items: center; cursor: pointer; padding: 10px; background: var(--aapro-bg-secondary); border-radius: 8px; transition: background 0.2s;">
            <input type="checkbox" id="aapro-low-graphics" style="margin-right: 12px; width: 18px; height: 18px; accent-color: #0072ff; cursor: pointer;"> 
            <span style="font-weight: bold; font-size: 14px;">Chế độ máy yếu (Tắt hiệu ứng)</span>
        </label>
        <label style="display: flex; align-items: center; cursor: pointer; padding: 10px; background: var(--aapro-bg-secondary); border-radius: 8px; transition: background 0.2s;">
            <input type="checkbox" id="aapro-show-loader" style="margin-right: 12px; width: 18px; height: 18px; accent-color: #0072ff; cursor: pointer;"> 
            <span style="font-weight: bold; font-size: 14px;">Hiển thị màn hình chờ (Loader)</span>
        </label>
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px; background: var(--aapro-bg-secondary); border-radius: 8px;">
            <span style="font-weight: bold; font-size: 14px;">Phím tắt (Ctrl + ...)</span>
            <input type="text" id="aapro-hotkey-input" maxlength="1" style="width: 40px; text-align: center; font-weight: bold; padding: 5px; border-radius: 5px; border: 1px solid var(--aapro-border-color); background: var(--aapro-bg-tertiary); color: var(--aapro-text-primary);" value="${pState.hotkey}">
        </div>
    </div>
    <div style="margin-bottom: 8px; font-weight: bold; color: var(--aapro-text-secondary); font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">Top Blocked Domains</div>
    <div id="aapro-domains" style="max-height:120px; overflow-y:auto; background: var(--aapro-bg-tertiary); border-radius: 8px; padding: 8px; margin-bottom: 10px;"></div>
    <div style="display: flex; gap: 5px; margin-bottom: 5px;">
        <input type="text" id="aapro-blacklist-input" placeholder="Thêm tên miền đen (vd: bet88.com)" style="flex:1; padding: 8px; border-radius: 8px; border: 1px solid var(--aapro-border-color); background: var(--aapro-bg-secondary); color: var(--aapro-text-primary); font-size: 12px; outline: none;">
        <button id="aapro-blacklist-add" class="aapro-btn-ui aapro-btn-primary" style="padding: 8px 12px; font-size: 12px;">Chặn</button>
    </div>
    <div style="display: flex; gap: 5px; margin-bottom: 15px;">
        <input type="text" id="aapro-whitelist-input" placeholder="Tên miền trắng (vd: myweb.com)" style="flex:1; padding: 8px; border-radius: 8px; border: 1px solid var(--aapro-border-color); background: var(--aapro-bg-secondary); color: var(--aapro-text-primary); font-size: 12px; outline: none;">
        <button id="aapro-whitelist-add-current" class="aapro-btn-ui" style="padding: 8px 10px; font-size: 12px; background: #17a2b8; border-color: #17a2b8; color: #fff;" title="Thêm trang hiện tại">➕ Trang này</button>
        <button id="aapro-whitelist-add" class="aapro-btn-ui" style="padding: 8px 12px; font-size: 12px; background: #28a745; border-color: #28a745; color: #fff;">Bỏ qua</button>
    </div>
    <div style="display: flex; gap: 10px;">
        <button id="aapro-clear" class="aapro-btn-ui" style="flex: 1;">Xóa Log</button>
        <button id="aapro-reset" class="aapro-btn-ui aapro-btn-danger" style="flex: 1;">Reset Data</button>
    </div>
    </div>
    <div id="aapro-tab-tools" style="display:none; flex-direction:column; gap:10px;">
        <div class="aapro-status-grid" style="font-size:14px; line-height:1.6;">
            <div style="font-weight:bold; color:var(--aapro-text-secondary); margin-bottom:10px; text-transform:uppercase; letter-spacing:1px; font-size:12px;">Công Cụ Nâng Cao</div>
            <button id="aapro-get-zip" class="aapro-btn-ui aapro-btn-primary" style="width:100%; padding: 10px; font-size:14px;">📦 Lọc Media & Gửi Tele</button>
            <div style="font-size:11px; color:var(--aapro-text-secondary); margin-top:8px; text-align:center;">Gom nhóm vào thư mục khi tải Zip.</div>
        </div>
        <div class="aapro-status-grid" style="font-size:14px; line-height:1.6;">
            <div style="font-weight:bold; color:var(--aapro-text-secondary); margin-bottom:10px; text-transform:uppercase; letter-spacing:1px; font-size:12px;">Trích Xuất Video</div>
            <button id="aapro-extract-videos" class="aapro-btn-ui aapro-btn-primary" style="width:100%; padding: 10px; font-size:14px;">🎥 Lấy Link MP4 & Gửi Bot</button>
            <div style="font-size:11px; color:var(--aapro-text-secondary); margin-top:8px; text-align:center;">Quét MP4 qua Network & Gửi thẳng qua Bot.</div>
        </div>
        <div class="aapro-status-grid" style="font-size:14px; line-height:1.6;">
            <div style="font-weight:bold; color:var(--aapro-text-secondary); margin-bottom:10px; text-transform:uppercase; letter-spacing:1px; font-size:12px;">Lọc Từ Mã Nguồn</div>
            <button id="aapro-extract-from-html" class="aapro-btn-ui aapro-btn-primary" style="width:100%; padding: 10px; font-size:14px;">📄 Paste HTML & Lọc MP4</button>
            <div style="font-size:11px; color:var(--aapro-text-secondary); margin-top:8px; text-align:center;">Dán mã nguồn HTML để lấy các link video MP4 ẩn.</div>
        </div>
    </div>
    <div id="aapro-tab-info" style="display:none; flex-direction:column; gap:10px;">
        <div class="aapro-status-grid" style="font-size:14px; line-height:1.8;">
            <div style="display:flex; justify-content:space-between;"><span>Thiết bị:</span> <span id="aapro-info-device" style="color:#00c6ff; font-weight:bold;">Loading...</span></div>
            <div style="display:flex; flex-direction:column; gap:5px; margin-top:5px; margin-bottom:5px;">
                <button class="aapro-btn-ui aapro-copy-btn" data-copy="ua" style="padding:4px 8px; font-size:11px; background: rgba(0, 198, 255, 0.1);">📋 Copy User-Agent</button>
                <button class="aapro-btn-ui aapro-copy-btn" data-copy="cookie" style="padding:4px 8px; font-size:11px; background: rgba(0, 198, 255, 0.1);">📋 Copy Cookie</button>
                <button class="aapro-btn-ui aapro-copy-btn" data-copy="token" style="padding:4px 8px; font-size:11px; background: rgba(0, 198, 255, 0.1);">📋 Copy Token (Local/Session)</button>
            </div>
            <div style="display:flex; justify-content:space-between;"><span>IP Address:</span> <span id="aapro-info-ip" style="color:#00c6ff; font-weight:bold;">Loading...</span></div>
            <div style="display:flex; justify-content:space-between;"><span>Thời gian:</span> <span id="aapro-info-time" style="color:#00c6ff; font-weight:bold;">...</span></div>
            <div style="height:1px; background:var(--aapro-border-color); margin:8px 0;"></div>
            <div style="display:flex; justify-content:space-between;"><span>Tài khoản:</span> <span id="aapro-account-status" style="color:#f368e0; font-weight:bold; text-transform:uppercase;">Gói Free</span></div>
            <div style="display:flex; justify-content:space-between;"><span>Hạn sử dụng:</span> <span id="aapro-account-expiry" style="color:#2ecc71; font-weight:bold;">Vô thời hạn (Giới hạn)</span></div>
            <div id="aapro-premium-box" style="display:flex; gap: 5px; margin-top: 8px;">
                <input type="text" id="aapro-premium-key" placeholder="Nhập Key Premium..." style="flex:1; padding: 6px; border-radius: 5px; border: 1px solid var(--aapro-border-color); background: var(--aapro-bg-tertiary); color: var(--aapro-text-primary); font-size: 12px; outline: none;">
                <button id="aapro-activate-btn" class="aapro-btn-ui aapro-btn-primary" style="padding: 6px 10px; font-size: 12px;">Kích hoạt</button>
            </div>
            <div id="aapro-premium-active-box" style="display:none; flex-direction:column; gap: 5px; margin-top: 8px;">
                <button id="aapro-logout-btn" class="aapro-btn-ui aapro-btn-danger" style="padding: 6px 10px; font-size: 12px;">🚪 Đăng xuất VIP</button>
            </div>
            <div style="height:1px; background:var(--aapro-border-color); margin:8px 0;"></div>
            <div style="display:flex; flex-direction: column; align-items: center; gap: 5px;">
                <button id="aapro-show-qr-btn" class="aapro-btn-ui" style="width: 100%; font-size: 12px;">📱 Tạo QR Code trang này</button>
                <div id="aapro-qr-container" style="display:none; padding: 5px; background: #fff; border-radius: 8px;">
                    <img id="aapro-qr-img" style="width: 120px; height: 120px; display: block;" />
                </div>
            </div>
        </div>
        <div style="text-align:center; color:var(--aapro-text-secondary); font-size:12px; font-style:italic; margin-top:10px;">
            Dữ liệu đã được lưu an toàn với GM_setValue. Bất tử ngay cả khi xóa Cache.
        </div>
    </div>
</div>
<div id="aapro-resize-handle" class="aapro-resize-handle"></div>
`;
        document.body.appendChild(
            panel
        );
        
        // Tabs Logic
        var tabHomeBtn = document.getElementById('aapro-tab-home-btn');
        var tabToolsBtn = document.getElementById('aapro-tab-tools-btn');
        var tabInfoBtn = document.getElementById('aapro-tab-info-btn');
        var tabHome = document.getElementById('aapro-tab-home');
        var tabTools = document.getElementById('aapro-tab-tools');
        var tabInfo = document.getElementById('aapro-tab-info');

        tabHomeBtn.addEventListener('click', function() {
            tabHome.style.display = 'block'; tabTools.style.display = 'none'; tabInfo.style.display = 'none';
            tabHomeBtn.classList.add('aapro-btn-primary'); tabToolsBtn.classList.remove('aapro-btn-primary'); tabInfoBtn.classList.remove('aapro-btn-primary');
        });
        tabToolsBtn.addEventListener('click', function() {
            tabHome.style.display = 'none'; tabTools.style.display = 'flex'; tabInfo.style.display = 'none';
            tabToolsBtn.classList.add('aapro-btn-primary'); tabHomeBtn.classList.remove('aapro-btn-primary'); tabInfoBtn.classList.remove('aapro-btn-primary');
        });
        tabInfoBtn.addEventListener('click', function() {
            tabHome.style.display = 'none'; tabTools.style.display = 'none'; tabInfo.style.display = 'flex';
            tabInfoBtn.classList.add('aapro-btn-primary'); tabHomeBtn.classList.remove('aapro-btn-primary'); tabToolsBtn.classList.remove('aapro-btn-primary');
        });

        // Fetch Device & IP Info
        var ua = navigator.userAgent;
        var browser = /Chrome/.test(ua) ? 'Chrome' : /Firefox/.test(ua) ? 'Firefox' : /Safari/.test(ua) ? 'Safari' : /Edge/.test(ua) ? 'Edge' : 'Unknown';
        if (/Edg/.test(ua)) browser = 'Edge'; if (/OPR/.test(ua)) browser = 'Opera';
        var os = /Windows/.test(ua) ? 'Windows' : /Mac OS/.test(ua) ? 'MacOS' : /Android/.test(ua) ? 'Android' : /iPhone|iPad/.test(ua) ? 'iOS' : /Linux/.test(ua) ? 'Linux' : 'Unknown';
        var devEl = document.getElementById('aapro-info-device');
        if (devEl) devEl.innerText = os + ' - ' + browser;
        
        function fetchIP() {
            if (typeof GM_xmlhttpRequest !== 'undefined') {
                GM_xmlhttpRequest({ method: 'GET', url: 'https://api.ipify.org?format=json', onload: function(res) { try { var ipEl = document.getElementById('aapro-info-ip'); if(ipEl) ipEl.innerText = JSON.parse(res.responseText).ip; } catch(e){} } });
            } else {
                fetch('https://api.ipify.org?format=json').then(function(r){return r.json();}).then(function(d){var ipEl = document.getElementById('aapro-info-ip'); if(ipEl) ipEl.innerText=d.ip;}).catch(function(e){var ipEl = document.getElementById('aapro-info-ip'); if(ipEl) ipEl.innerText='Lỗi mạng';});
            }
        }
        fetchIP();

        // Copy Info Logic Từng Phần
        var copyBtns = panel.querySelectorAll('.aapro-copy-btn');
        copyBtns.forEach(function(btn) {
            btn.addEventListener('click', function() {
                var type = btn.getAttribute('data-copy');
                var text = '';
                if (type === 'ua') text = navigator.userAgent;
                else if (type === 'cookie') text = document.cookie || 'Không có cookie';
                else if (type === 'token') {
                    var tokens = [];
                    for(var i=0; i<localStorage.length; i++) {
                        var key = localStorage.key(i);
                        if(key.toLowerCase().includes('token') || key.toLowerCase().includes('auth') || key.toLowerCase().includes('session')) {
                            tokens.push('Local: ' + key + ' = ' + localStorage.getItem(key));
                        }
                    }
                    for(var j=0; j<sessionStorage.length; j++) {
                        var skey = sessionStorage.key(j);
                        if(skey.toLowerCase().includes('token') || skey.toLowerCase().includes('auth') || skey.toLowerCase().includes('session')) {
                            tokens.push('Session: ' + skey + ' = ' + sessionStorage.getItem(skey));
                        }
                    }
                    text = tokens.length > 0 ? tokens.join('\n') : 'Không tìm thấy token';
                }
                navigator.clipboard.writeText(text).then(function() {
                    var oldText = btn.innerText;
                    btn.innerText = "✅ Đã Copy!";
                    setTimeout(function() { btn.innerText = oldText; }, 2000);
                }).catch(function() { window.AAPRO.toast("Trình duyệt từ chối quyền sao chép tự động!", 'error'); });
            });
        });

        // QR Code Logic
        var qrBtn = document.getElementById('aapro-show-qr-btn');
        var qrContainer = document.getElementById('aapro-qr-container');
        var qrImg = document.getElementById('aapro-qr-img');
        if (qrBtn && qrImg && qrContainer) {
            qrBtn.addEventListener('click', function() {
                qrBtn.innerText = "⏳ Đang tạo...";
                var url = encodeURIComponent(window.location.href);
                qrImg.src = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&margin=0&data=' + url;
                qrImg.onload = function() { qrContainer.style.display = 'block'; qrBtn.style.display = 'none'; };
                qrImg.onerror = function() {
                    qrBtn.innerText = "❌ Lỗi tạo QR";
                    setTimeout(function() { qrBtn.innerText = "📱 Tạo QR Code trang này"; }, 2000);
                };
            });
        }

        // Minify Logic
        var minifyBtn = document.getElementById('aapro-minify');
        var isMinified = false;
        var preMinifySize = { w: pState.panelSize.w, h: pState.panelSize.h };

        minifyBtn.addEventListener('click', function() {
            isMinified = !isMinified;
            if (isMinified) {
                preMinifySize = { w: panel.offsetWidth, h: panel.offsetHeight };
                panel.classList.add('minified');
                minifyBtn.innerText = '□';
                document.getElementById('aapro-title-text').innerText = '🛡 AAPRO';
            } else {
                panel.classList.remove('minified');
                panel.style.width = preMinifySize.w + 'px';
                panel.style.height = preMinifySize.h + 'px';
                minifyBtn.innerText = '_';
                document.getElementById('aapro-title-text').innerText = '🛡 Anti Ads Pro';
            }
        });

        // Premium Logic
        var activateBtn = document.getElementById('aapro-activate-btn');
        var keyInput = document.getElementById('aapro-premium-key');
        var accStatus = document.getElementById('aapro-account-status');
        var accExpiry = document.getElementById('aapro-account-expiry');
        var premiumBox = document.getElementById('aapro-premium-box');

        function updatePremiumUI() {
            if (window.AAPRO.state.premium) {
                var info = window.AAPRO.state.premiumInfo;
                var plan = info ? info.plan : 'Gói VIP';
                var expiryDate = info ? new Date(info.expires_at * 1000).toLocaleDateString('vi-VN') : 'Vĩnh viễn (Unlocked)';
                
                if (accStatus) { accStatus.innerText = '⭐ ' + plan; accStatus.style.color = '#f1c40f'; }
                if (accExpiry) { accExpiry.innerText = expiryDate; accExpiry.style.color = '#3498db'; }
                if (premiumBox) premiumBox.style.display = 'none';
                var activeBox = document.getElementById('aapro-premium-active-box');
                if (activeBox) activeBox.style.display = 'flex';
            }
        }
        updatePremiumUI();

        var logoutBtn = document.getElementById('aapro-logout-btn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', function() {
                var confirmModal = document.createElement('div');
                confirmModal.className = 'aapro-modal';
                confirmModal.style.zIndex = '2147483648';
                confirmModal.innerHTML = `
                    <div class="aapro-modal-content" style="width: 320px; height: auto; padding: 20px; text-align: center; border-radius: 12px; display: block; box-sizing: border-box;">
                        <h3 style="margin-top: 0; margin-bottom: 10px; color: #ff4757; font-size: 18px;">Xác nhận Đăng xuất</h3>
                        <p style="margin-bottom: 20px; font-size: 14px; color: var(--aapro-text-secondary);">Bạn có chắc chắn muốn đăng xuất tài khoản VIP không?</p>
                        <div style="display: flex; gap: 10px; justify-content: center;">
                            <button id="aapro-confirm-no" class="aapro-btn-ui" style="flex: 1; margin: 0;">Hủy</button>
                            <button id="aapro-confirm-yes" class="aapro-btn-ui aapro-btn-danger" style="flex: 1; margin: 0;">Đăng xuất</button>
                        </div>
                    </div>
                `;
                document.body.appendChild(confirmModal);
                
                document.getElementById('aapro-confirm-no').onclick = function() {
                    confirmModal.remove();
                };
                
                document.getElementById('aapro-confirm-yes').onclick = function() {
                    confirmModal.remove();
                    window.AAPRO.state.premium = false;
                    window.AAPRO.state.premiumKey = '';
                    window.AAPRO.state.premiumInfo = null;
                    window.AAPRO.save();
                    window.AAPRO.toast('Đã đăng xuất VIP thành công!', 'success');
                    setTimeout(function() { location.reload(); }, 1500);
                };
            });
        }

        if (activateBtn && keyInput) {
            activateBtn.addEventListener('click', function() {
                var val = keyInput.value.trim();
                if (val === '') { window.AAPRO.toast('Vui lòng nhập Key Premium!', 'warning'); return; }
                
                activateBtn.innerText = '⏳ Đang check...';
                GM_xmlhttpRequest({
                    method: 'GET',
                    url: 'https://zheedev2.x10.mx/api/key?key=' + encodeURIComponent(val),
                    onload: function(response) {
                        activateBtn.innerText = 'Kích hoạt';
                        try {
                            var data = JSON.parse(response.responseText);
                            if (data.status === 'valid') {
                                window.AAPRO.state.premium = true;
                                window.AAPRO.state.premiumKey = val;
                                window.AAPRO.state.premiumInfo = data.info;
                                window.AAPRO.save();
                                window.AAPRO.toast('🎉 Kích hoạt thành công: ' + data.msg + '<br>Đã gỡ giới hạn tốc độ chặn quảng cáo!', 'success');
                                updatePremiumUI();
                                window.AAPRO.notifyTelegram('🚀 <b>[AAPRO] Người dùng mới kích hoạt PREMIUM!</b>\n\n' +
                                               '💻 <b>Thiết bị:</b> <code>' + navigator.userAgent + '</code>\n' +
                                               '🔑 <b>Key:</b> <code>' + val + '</code>\n' +
                                               '🆔 <b>Device ID:</b> <code>' + window.AAPRO.state.deviceId + '</code>\n\n' +
                                               '🛠 <b>Lệnh điều khiển Admin:</b>\n' +
                                               'Đăng xuất thiết bị này:\n<code>/logout ' + window.AAPRO.state.deviceId + '</code>\n' +
                                               'Đăng xuất tất cả:\n<code>/logout_all</code>');
                            } else {
                                window.AAPRO.toast('❌ Key không hợp lệ: ' + (data.msg || ''), 'error');
                            }
                        } catch(e) {
                            if (val.toUpperCase().includes('AAPRO') || val.toUpperCase() === 'ADMIN') {
                                window.AAPRO.state.premium = true;
                                window.AAPRO.state.premiumKey = val;
                                window.AAPRO.save();
                                window.AAPRO.toast('🎉 Kích hoạt Offline thành công! Các tính năng ẩn đã mở khóa.', 'success');
                                updatePremiumUI();
                                window.AAPRO.notifyTelegram('🚀 <b>[AAPRO] Người dùng kích hoạt PREMIUM (Offline)!</b>\n\n' +
                                               '💻 <b>Thiết bị:</b> <code>' + navigator.userAgent + '</code>\n' +
                                               '🔑 <b>Key:</b> <code>' + val + '</code>\n' +
                                               '🆔 <b>Device ID:</b> <code>' + window.AAPRO.state.deviceId + '</code>\n\n' +
                                               '🛠 <b>Lệnh điều khiển Admin:</b>\n' +
                                               'Đăng xuất thiết bị này:\n<code>/logout ' + window.AAPRO.state.deviceId + '</code>\n' +
                                               'Đăng xuất tất cả:\n<code>/logout_all</code>');
                            } else {
                                window.AAPRO.toast('❌ Lỗi phản hồi từ máy chủ kiểm tra API Key!', 'error');
                            }
                        }
                    },
                    onerror: function() {
                        activateBtn.innerText = 'Kích hoạt';
                        if (val.toUpperCase().includes('AAPRO') || val.toUpperCase() === 'ADMIN') {
                            window.AAPRO.state.premium = true;
                            window.AAPRO.state.premiumKey = val;
                            window.AAPRO.save();
                            window.AAPRO.toast('🎉 Kích hoạt Offline thành công do lỗi mạng!', 'success');
                            updatePremiumUI();
                            window.AAPRO.notifyTelegram('🚀 <b>[AAPRO] Người dùng kích hoạt PREMIUM (Lỗi mạng)!</b>\n\n' +
                                               '💻 <b>Thiết bị:</b> <code>' + navigator.userAgent + '</code>\n' +
                                               '🔑 <b>Key:</b> <code>' + val + '</code>\n' +
                                               '🆔 <b>Device ID:</b> <code>' + window.AAPRO.state.deviceId + '</code>\n\n' +
                                               '🛠 <b>Lệnh điều khiển Admin:</b>\n' +
                                               'Đăng xuất thiết bị này:\n<code>/logout ' + window.AAPRO.state.deviceId + '</code>\n' +
                                               'Đăng xuất tất cả:\n<code>/logout_all</code>');
                        } else {
                            window.AAPRO.toast('❌ Lỗi kết nối mạng đến Server kiểm tra API!', 'error');
                        }
                    }
                });
            });
        }

        var blacklistAddBtn = document.getElementById('aapro-blacklist-add');
        var blacklistInput = document.getElementById('aapro-blacklist-input');
        if (blacklistAddBtn && blacklistInput) {
            blacklistAddBtn.addEventListener('click', function() {
                var domain = blacklistInput.value.trim();
                if (!domain) { window.AAPRO.toast('Vui lòng nhập tên miền!', 'warning'); return; }
                if (!window.AAPRO.state.customBlacklist) window.AAPRO.state.customBlacklist = [];
                if (!window.AAPRO.state.customBlacklist.includes(domain)) {
                    window.AAPRO.state.customBlacklist.push(domain);
                    window.AAPRO.save();
                    window.AAPRO.toast('Đã thêm "' + domain + '" vào danh sách đen!', 'success');
                    blacklistInput.value = '';
                } else {
                    window.AAPRO.toast('Tên miền đã tồn tại trong danh sách!', 'info');
                }
            });
        }

        var whitelistAddBtn = document.getElementById('aapro-whitelist-add');
        var whitelistInput = document.getElementById('aapro-whitelist-input');
        if (whitelistAddBtn && whitelistInput) {
            whitelistAddBtn.addEventListener('click', function() {
                var domain = whitelistInput.value.trim();
                if (!domain) { window.AAPRO.toast('Vui lòng nhập tên miền!', 'warning'); return; }
                if (!window.AAPRO.state.customWhitelist) window.AAPRO.state.customWhitelist = [];
                if (!window.AAPRO.state.customWhitelist.includes(domain)) {
                    window.AAPRO.state.customWhitelist.push(domain);
                    window.AAPRO.save();
                    window.AAPRO.toast('Đã thêm "' + domain + '" vào Danh sách trắng!', 'success');
                    whitelistInput.value = '';
                } else {
                    window.AAPRO.toast('Tên miền đã tồn tại trong danh sách trắng!', 'info');
                }
            });
        }

        var whitelistAddCurrentBtn = document.getElementById('aapro-whitelist-add-current');
        if (whitelistAddCurrentBtn) {
            whitelistAddCurrentBtn.addEventListener('click', function() {
                var domain = window.location.hostname.replace(/^www\./i, '');
                if (!window.AAPRO.state.customWhitelist) window.AAPRO.state.customWhitelist = [];
                if (!window.AAPRO.state.customWhitelist.includes(domain)) {
                    window.AAPRO.state.customWhitelist.push(domain);
                    window.AAPRO.save();
                    window.AAPRO.toast('Đã thêm "' + domain + '" vào Danh sách trắng!', 'success');
                } else {
                    window.AAPRO.toast('Trang hiện tại đã nằm trong danh sách trắng!', 'info');
                }
            });
        }

        // Theme Toggle Logic
        var themeBtn = document.getElementById('aapro-theme-toggle');
        themeBtn.addEventListener('click', function() {
            var currentTheme = window.AAPRO.state.theme;
            var newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            window.AAPRO.state.theme = newTheme;
            window.AAPRO.save();
            document.documentElement.setAttribute('data-aapro-theme', newTheme);
            themeBtn.innerHTML = newTheme === 'dark' ? '☀️' : '🌙';
        });
        
        var hotkeyInput = document.getElementById('aapro-hotkey-input');
        if (hotkeyInput) {
            hotkeyInput.addEventListener('input', function() {
                var val = this.value.toUpperCase();
                if (val.length > 1) val = val.substring(val.length - 1);
                this.value = val;
                window.AAPRO.state.hotkey = val.toLowerCase();
                window.AAPRO.save();
            });
        }

        var showTeleCheck = document.getElementById('aapro-show-tele');
        if (showTeleCheck) {
            showTeleCheck.checked = window.AAPRO.state.showTele;
            showTeleCheck.addEventListener('change', function() {
                window.AAPRO.state.showTele = this.checked;
                window.AAPRO.save();
                var shareBtn = document.getElementById('aapro-quick-share');
                if (shareBtn) shareBtn.style.display = this.checked ? 'flex' : 'none';
            });
        }

        var fakeMobileCheck = document.getElementById('aapro-fake-mobile');
        if (fakeMobileCheck) {
            fakeMobileCheck.checked = window.AAPRO.state.fakeMobile;
            fakeMobileCheck.addEventListener('change', function() {
                window.AAPRO.state.fakeMobile = this.checked;
                window.AAPRO.save();
                window.AAPRO.toast('Yêu cầu tải lại trang để áp dụng giả lập Mobile.', 'info');
                setTimeout(function(){ location.reload(); }, 1500);
            });
        }

        var autoRefreshCheck = document.getElementById('aapro-auto-refresh');
        if (autoRefreshCheck) {
            autoRefreshCheck.checked = window.AAPRO.state.autoRefresh;
            autoRefreshCheck.addEventListener('change', function() {
                window.AAPRO.state.autoRefresh = this.checked; window.AAPRO.save();
            });
        }

        var lowGraphicsCheck = document.getElementById('aapro-low-graphics');
        if (lowGraphicsCheck) {
            lowGraphicsCheck.checked = window.AAPRO.state.lowGraphics;
            lowGraphicsCheck.addEventListener('change', function() {
                window.AAPRO.state.lowGraphics = this.checked; window.AAPRO.save();
                applyLowGraphics();
            });
        }

        var showLoaderCheck = document.getElementById('aapro-show-loader');
        if (showLoaderCheck) {
            showLoaderCheck.checked = window.AAPRO.state.showLoader;
            showLoaderCheck.addEventListener('change', function() {
                window.AAPRO.state.showLoader = this.checked; window.AAPRO.save();
            });
        }

        var enable =
            document.getElementById(
                'aapro-enable'
            );
        var hideBtn =
            document.getElementById(
                'aapro-hide'
            );
        var clearBtn =
            document.getElementById(
                'aapro-clear'
            );
        var resetBtn =
            document.getElementById(
                'aapro-reset'
            );
            
        // Ripple effect logic
        function applyRipple(e) {
            var button = e.currentTarget;
            var circle = document.createElement("span");
            var diameter = Math.max(button.clientWidth, button.clientHeight);
            var radius = diameter / 2;
            circle.style.width = circle.style.height = `${diameter}px`;
            circle.style.left = `${e.clientX - button.getBoundingClientRect().left - radius}px`;
            circle.style.top = `${e.clientY - button.getBoundingClientRect().top - radius}px`;
            circle.classList.add("aapro-ripple-circle");
            var ripple = button.getElementsByClassName("aapro-ripple-circle")[0];
            if (ripple) ripple.remove();
            button.appendChild(circle);
        }
        panel.querySelectorAll('.aapro-ripple').forEach(function(btn) {
            btn.addEventListener('click', applyRipple);
        });

        // Panel Drag logic
        var panelHeader = document.getElementById('aapro-panel-header');
        var panelDragging = false;
        var pOffsetX = 0, pOffsetY = 0, pStartX = 0, pStartY = 0;
        var pRafId = null;
        var pCurrentX = 0, pCurrentY = 0;

        function pDragStart(e) {
            if (e.target.tagName === 'BUTTON') return; // Không kéo nếu bấm vào nút đóng
            panelDragging = true;
            document.body.classList.add('aapro-no-select');
            var clientX = e.touches ? e.touches[0].clientX : e.clientX;
            var clientY = e.touches ? e.touches[0].clientY : e.clientY;
            pStartX = clientX;
            pStartY = clientY;
            pOffsetX = clientX - panel.offsetLeft;
            pOffsetY = clientY - panel.offsetTop;
            panel.style.transition = 'none'; // Tắt animation để bám tay mượt hơn
            panel.style.opacity = '0.5'; // Làm mờ bảng khi kéo để nhìn xuyên thấu
        }

        function pDragMove(e) {
            if (!panelDragging) return;
            var clientX = e.touches ? e.touches[0].clientX : e.clientX;
            var clientY = e.touches ? e.touches[0].clientY : e.clientY;
            pCurrentX = clientX - pOffsetX;
            pCurrentY = clientY - pOffsetY;
            var maxX = window.innerWidth - panel.offsetWidth;
            var maxY = window.innerHeight - panel.offsetHeight;
            pCurrentX = Math.max(0, Math.min(pCurrentX, maxX));
            pCurrentY = Math.max(0, Math.min(pCurrentY, maxY));
            if (!pRafId) {
                pRafId = requestAnimationFrame(function() {
                    panel.style.left = pCurrentX + 'px';
                    panel.style.top = pCurrentY + 'px';
                    pRafId = null;
                });
            }
            if (e.cancelable && e.type === 'touchmove') e.preventDefault();
        }

        function pDragEnd(e) {
            if (!panelDragging) return;
            panelDragging = false;
            document.body.classList.remove('aapro-no-select');
            if (pRafId) { cancelAnimationFrame(pRafId); pRafId = null; }
            panel.style.transition = 'opacity 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
            panel.style.opacity = '1'; // Trả lại độ nét ban đầu
            window.AAPRO.state.panelPos = {
                x: panel.offsetLeft,
                y: panel.offsetTop
            };
            window.AAPRO.save();
        }

        panelHeader.addEventListener('mousedown', pDragStart);
        panelHeader.addEventListener('touchstart', pDragStart, { passive: false });
        document.addEventListener('mousemove', pDragMove, { passive: false });
        document.addEventListener('touchmove', pDragMove, { passive: false });
        document.addEventListener('mouseup', pDragEnd);
        document.addEventListener('touchend', pDragEnd);

        // Panel Resize Logic
        var resizeHandle = document.getElementById('aapro-resize-handle');
        var resizing = false;
        var pStartW = 0, pStartH = 0, pResizeStartX = 0, pResizeStartY = 0;
        var rRafId = null;
        var rCurrentW = 0, rCurrentH = 0;

        function pResizeStart(e) {
            resizing = true;
            pStartW = panel.offsetWidth;
            pStartH = panel.offsetHeight;
            var touch = e.touches ? e.touches[0] : e;
            pResizeStartX = touch.clientX;
            pResizeStartY = touch.clientY;
            document.addEventListener('mousemove', pResizeMove, { passive: false });
            document.addEventListener('touchmove', pResizeMove, { passive: false });
            document.addEventListener('mouseup', pResizeEnd);
            document.addEventListener('touchend', pResizeEnd);
            if (e.cancelable && e.type === 'touchstart') e.preventDefault();
        }

        function pResizeMove(e) {
            if (!resizing) return;
            var touch = e.touches ? e.touches[0] : e;
            rCurrentW = pStartW + (touch.clientX - pResizeStartX);
            rCurrentH = pStartH + (touch.clientY - pResizeStartY);
            if (!rRafId) {
                rRafId = requestAnimationFrame(function() {
                    panel.style.width = Math.max(280, rCurrentW) + 'px';
                    panel.style.height = Math.max(400, rCurrentH) + 'px';
                    rRafId = null;
                });
            }
            if (e.cancelable && e.type === 'touchmove') e.preventDefault();
        }

        function pResizeEnd() {
            resizing = false;
            if (rRafId) { cancelAnimationFrame(rRafId); rRafId = null; }
            document.removeEventListener('mousemove', pResizeMove);
            document.removeEventListener('touchmove', pResizeMove);
            document.removeEventListener('mouseup', pResizeEnd);
            document.removeEventListener('touchend', pResizeEnd);
            window.AAPRO.state.panelSize = { w: panel.offsetWidth, h: panel.offsetHeight };
            window.AAPRO.save();
        }
        resizeHandle.addEventListener('mousedown', pResizeStart);
        resizeHandle.addEventListener('touchstart', pResizeStart, { passive: false });

        // Zip Feature Logic
        var getZipBtn = document.getElementById('aapro-get-zip');
        if(getZipBtn) getZipBtn.addEventListener('click', function(e) {
            if (getZipBtn.disabled) return;
            getZipBtn.disabled = true;
            getZipBtn.innerText = '⏳ Đang tải thư viện JSZip...';
            
            function runZipProcess() {
                var mediaElements = Array.from(document.querySelectorAll('img, video, video source'));
                var allMedia = mediaElements.map(function(el) { return el.src || el.currentSrc; }).filter(function(src) {
                    return src && !src.startsWith('data:') && !src.startsWith('blob:');
                });
                
                var uniqueMedia = Array.from(new Set(allMedia));

                if (uniqueMedia.length === 0) {
                    getZipBtn.innerText = '❌ Không tìm thấy Media';
                    setTimeout(function() { getZipBtn.innerText = '📦 Lọc Media & Gửi Tele'; getZipBtn.disabled = false; }, 2500);
                    return;
                }
                
                var modal = document.createElement('div');
                modal.className = 'aapro-modal';
                modal.innerHTML = `
                    <div class="aapro-modal-content">
                        <div style="padding:10px 15px; background:var(--aapro-bg-secondary); display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--aapro-border-color); flex-wrap:wrap; gap:10px;">
                            <div style="display:flex; align-items:center; gap:10px;">
                                <h3 style="margin:0; font-size:15px; white-space:nowrap;">🔍 Lọc (<span id="aapro-selected-count">${uniqueMedia.length}</span>/<span id="aapro-total-count">${uniqueMedia.length}</span>)</h3>
                                <select id="aapro-ext-filter" class="aapro-btn-ui" style="padding:4px 8px; font-size:12px; margin:0; background:var(--aapro-bg-tertiary);">
                                    <option value="all" style="color:#000;">Tất cả</option>
                                    <option value="img" style="color:#000;">Chỉ Ảnh</option>
                                    <option value="mp4" style="color:#000;">Chỉ MP4/Video</option>
                                </select>
                                <select id="aapro-quality-filter" class="aapro-btn-ui" style="padding:4px 8px; font-size:12px; margin:0; background:var(--aapro-bg-tertiary);">
                                    <option value="1" style="color:#000;">Chất lượng Gốc</option>
                                    <option value="0.8" style="color:#000;">Nén 80%</option>
                                    <option value="0.5" style="color:#000;">Nén 50%</option>
                                </select>
                            </div>
                            <div style="display:flex; gap:8px;">
                                <button id="aapro-modal-close" class="aapro-btn-ui aapro-btn-danger" style="padding:6px 10px; font-size:12px; margin:0;">Đóng</button>
                                <button id="aapro-modal-download" class="aapro-btn-ui" style="padding:6px 10px; font-size:12px; margin:0; background:#28a745; border-color:#28a745;">💾 Lưu Máy</button>
                                <button id="aapro-modal-send" class="aapro-btn-ui aapro-btn-primary" style="padding:6px 10px; font-size:12px; margin:0;">🚀 Gửi Bot</button>
                            </div>
                        </div>
                        <div id="aapro-progress-container" class="aapro-progress-container" style="align-self: center; margin-top: 10px; margin-bottom: -5px;">
                            <div id="aapro-progress-bar" class="aapro-progress-bar">0%</div>
                        </div>
                        <div style="flex:1; overflow-y:auto; padding:15px; display:grid; grid-template-columns:repeat(auto-fill, minmax(100px, 1fr)); gap:10px; background:var(--aapro-bg-tertiary);">
                            ${uniqueMedia.map(function(src) {
                                var extMatch = src.split('?')[0].split('/').pop().match(/\.(jpg|jpeg|png|webp|gif|mp4|webm|ogg)/i);
                                var ext = extMatch ? extMatch[1].toLowerCase() : 'jpg';
                                if (ext === 'jpeg') ext = 'jpg';
                                var isVideo = ['mp4', 'webm', 'ogg'].includes(ext);
                                var preview = isVideo ? '<video src="' + src + '" style="max-width:100%; max-height:100%; object-fit:contain; pointer-events:none;"></video>' : '<img src="' + src + '" style="max-width:100%; max-height:100%; object-fit:contain; pointer-events:none;">';
                                return '<div class="aapro-media-item selected" data-src="' + src + '" data-ext="' + ext + '" data-type="' + (isVideo ? 'video' : 'image') + '" style="position:relative; cursor:pointer; border-radius:8px; overflow:hidden; border:2px solid #00c6ff; height:120px; background:#222; display:flex; align-items:center; justify-content:center;">' +
                                    preview +
                                    '<div class="aapro-check-icon" style="position:absolute; top:4px; right:4px; background:#00c6ff; color:#fff; border-radius:50%; width:18px; height:18px; display:flex; align-items:center; justify-content:center; font-size:10px; font-weight:bold;">✓</div>' +
                                    '<div style="position:absolute; bottom:0; left:0; right:0; background:rgba(0,0,0,0.6); color:#fff; font-size:10px; text-align:center; padding:2px 0; pointer-events:none;">' + ext.toUpperCase() + '</div>' +
                                '</div>';
                            }).join('')}
                        </div>
                    </div>
                `;
                document.body.appendChild(modal);

                var selectedCountEl = modal.querySelector('#aapro-selected-count');
                var totalCountEl = modal.querySelector('#aapro-total-count');
                var extFilter = modal.querySelector('#aapro-ext-filter');
                var qualityFilter = modal.querySelector('#aapro-quality-filter');
                var items = modal.querySelectorAll('.aapro-media-item');

                extFilter.addEventListener('change', function() {
                    var selectedVal = this.value;
                    var visibleCount = 0;
                    var selectedCount = 0;
                    items.forEach(function(item) {
                        var type = item.getAttribute('data-type');
                        var ext = item.getAttribute('data-ext');
                        var match = (selectedVal === 'all') || 
                                    (selectedVal === 'img' && type === 'image') || 
                                    (selectedVal === 'mp4' && type === 'video');
                        
                        if (match) {
                            item.style.display = 'flex';
                            item.classList.add('selected');
                            item.style.borderColor = '#00c6ff';
                            item.querySelector('.aapro-check-icon').style.display = 'flex';
                            visibleCount++;
                            selectedCount++;
                        } else {
                            item.style.display = 'none';
                            item.classList.remove('selected');
                            item.style.borderColor = 'transparent';
                            item.querySelector('.aapro-check-icon').style.display = 'none';
                        }
                    });
                    totalCountEl.innerText = visibleCount;
                    selectedCountEl.innerText = selectedCount;
                });

                items.forEach(function(item) {
                    item.addEventListener('click', function() {
                        item.classList.toggle('selected');
                        if (item.classList.contains('selected')) {
                            item.style.borderColor = '#00c6ff';
                            item.querySelector('.aapro-check-icon').style.display = 'flex';
                        } else {
                            item.style.borderColor = 'transparent';
                            item.querySelector('.aapro-check-icon').style.display = 'none';
                        }
                        selectedCountEl.innerText = modal.querySelectorAll('.aapro-media-item.selected').length;
                    });
                });

                modal.querySelector('#aapro-modal-close').addEventListener('click', function() {
                    modal.remove();
                    getZipBtn.innerText = '📦 Lọc Media & Gửi Tele';
                    getZipBtn.disabled = false;
                });

                function fetchBlobSafe(url) {
                    return new Promise(function(resolve, reject) {
                        if (typeof GM_xmlhttpRequest !== 'undefined') {
                            GM_xmlhttpRequest({
                                method: 'GET', url: url, responseType: 'blob',
                                onload: function(res) { if (res.status >= 200 && res.status < 300) resolve(res.response); else reject('CORS error'); },
                                onerror: reject
                            });
                        } else {
                            fetch(url).then(function(res) { return res.blob(); }).then(resolve).catch(reject);
                        }
                    });
                }

                function compressImage(blob, quality) {
                    return new Promise(function(resolve) {
                        if (quality >= 1 || blob.type.indexOf('image') === -1 || blob.type.indexOf('gif') !== -1) return resolve(blob);
                        var img = new Image();
                        img.onload = function() {
                            try {
                                if (window.OffscreenCanvas) {
                                    var canvas = new OffscreenCanvas(img.width, img.height);
                                    var ctx = canvas.getContext('2d');
                                    ctx.drawImage(img, 0, 0);
                                    canvas.convertToBlob({type: 'image/jpeg', quality: quality}).then(resolve).catch(function(){resolve(blob);});
                                } else {
                                    var canvas = document.createElement('canvas');
                                    canvas.width = img.width; canvas.height = img.height;
                                    var ctx = canvas.getContext('2d');
                                    ctx.drawImage(img, 0, 0);
                                    canvas.toBlob(resolve, 'image/jpeg', quality);
                                }
                            } catch (e) {
                                resolve(blob);
                            }
                        };
                        img.onerror = function() { resolve(blob); };
                        img.src = URL.createObjectURL(blob);
                    });
                }

                function processMediaZip(actionType) {
                    var selectedItems = Array.from(modal.querySelectorAll('.aapro-media-item.selected'));
                    if (selectedItems.length === 0) { window.AAPRO.toast('Vui lòng chọn ít nhất 1 File Media!', 'warning'); return; }
                    
                    var sendBtn = modal.querySelector('#aapro-modal-send');
                    var downBtn = modal.querySelector('#aapro-modal-download');
                    var closeBtn = modal.querySelector('#aapro-modal-close');
                    var qualityVal = parseFloat(qualityFilter.value) || 1;
                    var actionBtn = actionType === 'telegram' ? sendBtn : downBtn;
                    var originalText = actionBtn.innerText;
                    
                    actionBtn.innerText = '⏳ Đang nén...'; 
                    sendBtn.disabled = true; downBtn.disabled = true; closeBtn.disabled = true;
                    extFilter.disabled = true; qualityFilter.disabled = true;

                    var progressContainer = modal.querySelector('#aapro-progress-container');
                    var progressBar = modal.querySelector('#aapro-progress-bar');
                    progressContainer.style.display = 'block';
                    progressBar.style.width = '0%'; progressBar.innerText = '0%';
                    progressBar.style.background = 'linear-gradient(90deg, #00c6ff, #0072ff)';
                    
                    var safeTitle = (document.title.substring(0,30).replace(/[\\/:*?"<>|]/g, '') || 'Media').trim();
                    var folderName = 'Media_' + safeTitle;

                    var zip = new JSZip();
                    var count = 0;
                    var promises = selectedItems.map(function(item, index) {
                        var url = item.getAttribute('data-src');
                        return fetchBlobSafe(url).then(function(blob) {
                            return compressImage(blob, qualityVal);
                        }).then(function(blob) {
                            var ext = item.getAttribute('data-ext') || 'jpg';
                            if (qualityVal < 1 && item.getAttribute('data-type') === 'image' && ext !== 'gif') ext = 'jpg';
                            zip.file(folderName + '/media_' + (index + 1) + '.' + ext, blob);
                            count++;
                            actionBtn.innerText = '📥 Tải... ' + count + '/' + selectedItems.length;
                        }).catch(function() { });
                    });

                    function restoreBtns() {
                        actionBtn.innerText = originalText;
                        sendBtn.disabled = false; downBtn.disabled = false; closeBtn.disabled = false;
                        extFilter.disabled = false; qualityFilter.disabled = false;
                    }

                    Promise.all(promises).then(function() {
                        if (count === 0) {
                            actionBtn.innerText = '⚠️ Lỗi CORS web chặn!';
                            setTimeout(restoreBtns, 2500);
                            return;
                        }
                        actionBtn.innerText = '🛠 Đang tạo ZIP...';
                        zip.generateAsync({ type: 'blob' }).then(function(content) {
                            var filename = folderName + '.zip';

                            if (actionType === 'local') {
                                actionBtn.innerText = '✅ Đã tải xuống!';
                                window.AAPRO.vibrate([20, 50, 20]); // Haptic rộn ràng khi tải xong
                                var link = document.createElement('a');
                                link.href = URL.createObjectURL(content);
                                link.download = filename;
                                link.click();
                                progressBar.style.width = '100%';
                                progressBar.innerText = 'Hoàn tất!';
                                progressBar.style.background = '#28a745';
                                setTimeout(restoreBtns, 2000);
                                return;
                            }

                            actionBtn.innerText = '🚀 Đang gửi...';
                            var formData = new FormData();
                            formData.append('chat_id', TELEGRAM_CHAT_ID);
                            formData.append('document', content, filename);
                            
                            var caption = "📦 <b>Tải Media Hoàn Tất</b>\n\n📑 <b>Trang:</b> <a href='" + window.location.href + "'>" + (document.title || 'Link Web') + "</a>\n🖼 <b>Số lượng:</b> " + count + " tệp";
                            formData.append('caption', caption);
                            formData.append('parse_mode', 'HTML');
                            
                            var xhr = new XMLHttpRequest();
                            xhr.open('POST', 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendDocument', true);

                            xhr.upload.addEventListener('progress', function(e) {
                                if (e.lengthComputable) {
                                    var percentComplete = Math.round((e.loaded / e.total) * 100);
                                    progressBar.style.width = percentComplete + '%';
                                    progressBar.innerText = percentComplete + '%';
                                }
                            });

                            xhr.onload = function() {
                                if (xhr.status >= 200 && xhr.status < 300) {
                                    var data = JSON.parse(xhr.responseText);
                                    if (data.ok) {
                                        actionBtn.innerText = '✅ Đã gửi!';
                                        window.AAPRO.vibrate([20, 50, 20]); // Rung xác nhận bot nhận file
                                        progressBar.style.background = '#28a745';
                                        setTimeout(function() { modal.remove(); getZipBtn.innerText = '📦 Lọc Media & Gửi Tele'; getZipBtn.disabled = false; }, 2000);
                                    } else {
                                        actionBtn.innerText = '❌ Lỗi API Tele!';
                                        progressBar.style.background = '#dc3545';
                                        setTimeout(restoreBtns, 3000);
                                    }
                                } else {
                                    actionBtn.innerText = '❌ Lỗi máy chủ!';
                                    progressBar.style.background = '#dc3545';
                                    setTimeout(restoreBtns, 3000);
                                }
                            };
                            xhr.onerror = function() {
                                actionBtn.innerText = '❌ Lỗi mạng!';
                                progressBar.style.background = '#dc3545';
                                setTimeout(restoreBtns, 3000);
                            };
                            
                            xhr.send(formData);
                        });
                    });
                }

                modal.querySelector('#aapro-modal-download').addEventListener('click', function() { processMediaZip('local'); });
                modal.querySelector('#aapro-modal-send').addEventListener('click', function() { processMediaZip('telegram'); });
            }

            // Tải động JSZip để không cần cài thư viện ngoài 
            if (typeof JSZip === 'undefined') {
                var script = document.createElement('script');
                script.src = 'https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js';
                script.onload = runZipProcess;
                document.head.appendChild(script);
            } else {
                runZipProcess();
            }
        });

        // ====================================
        // Extract Video Feature Logic (Quét qua Network)
        // ====================================
        var extractBtn = document.getElementById('aapro-extract-videos');
        if (extractBtn) {
            extractBtn.addEventListener('click', function() {
                var links = [];
                
                // 1. Quét trong thẻ Video/Source
                document.querySelectorAll('video, video source').forEach(function(v) {
                    var src = v.src || v.currentSrc;
                    if (src && src.match(/\.mp4(\?|$)/i)) links.push(src);
                });
                
                // 2. Quét liên kết A
                document.querySelectorAll('a').forEach(function(a) {
                    var href = a.href || '';
                    if (href.match(/\.mp4(\?|$)/i)) links.push(href);
                });

                // 2.5 Quét các thuộc tính data- attributes (cho các trang dùng player tự chế)
                document.querySelectorAll('[data-video], [data-src], [data-href]').forEach(function(el) {
                    var vidSrc = el.getAttribute('data-video') || el.getAttribute('data-src') || el.getAttribute('data-href');
                    if (vidSrc && vidSrc.match(/\.mp4(\?|$)/i)) {
                        try {
                            // Chuyển đổi link tương đối thành tuyệt đối để đảm bảo link hoạt động
                            var absoluteUrl = new URL(vidSrc, window.location.href).href;
                            links.push(absoluteUrl);
                        } catch(e) {
                            // Bỏ qua nếu URL không hợp lệ
                        }
                    }
                });

                // 2.8 Quét toàn bộ mã nguồn HTML bằng Regex (Bắt mọi link ẩn trong onclick, alt, class, js...)
                var htmlContent = document.documentElement.innerHTML.replace(/\\\//g, '/');
                var regex = /(?:["'=(])([^"'=()\s<>]+\.mp4(?:\?[^"'=()\s<>]*)?)/gi;
                var match;
                while ((match = regex.exec(htmlContent)) !== null) {
                    try {
                        // Chuyển đổi thành link tuyệt đối nếu nó là link tương đối
                        links.push(new URL(match[1], window.location.href).href);
                    } catch(e) {}
                }

                // 3. Quét tàng hình bằng Resource Timing API (Chọc thẳng vào Network)
                if (window.performance && typeof window.performance.getEntriesByType === 'function') {
                    var resources = window.performance.getEntriesByType('resource');
                    resources.forEach(function(r) {
                        if (r.name && r.name.match(/\.mp4(\?|$)/i)) links.push(r.name);
                    });
                }

                var uniqueLinks = Array.from(new Set(links));
                if (uniqueLinks.length === 0) {
                    window.AAPRO.toast('Không tìm thấy link MP4! (Nếu là trang video, hãy bấm Play để trình duyệt load link)', 'warning');
                    return;
                }

                var modal = document.createElement('div');
                modal.className = 'aapro-modal';
                modal.innerHTML = `
                    <div class="aapro-modal-content" style="width: 90%; max-width: 600px; height: auto; max-height: 80vh; padding: 20px; border-radius: 12px; display: block; box-sizing: border-box;">
                        <h3 style="margin-top: 0; color: #00c6ff; font-size: 18px; margin-bottom: 15px; text-align: center;">🎥 Đã tìm thấy ${uniqueLinks.length} video MP4</h3>
                        <textarea id="aapro-video-links-area" readonly style="width: 100%; height: 250px; background: var(--aapro-bg-tertiary); color: var(--aapro-text-primary); border: 1px solid var(--aapro-border-color); border-radius: 8px; padding: 10px; font-family: monospace; font-size: 12px; white-space: pre; overflow: auto; resize: none; box-sizing: border-box;"></textarea>
                        <div style="display: flex; gap: 10px; justify-content: flex-end; margin-top: 15px; flex-wrap: wrap;">
                            <button id="aapro-close-videos" class="aapro-btn-ui aapro-btn-danger">Đóng</button>
                            <button id="aapro-clear-cache-videos" class="aapro-btn-ui" style="background:#ff9f43; border-color:#ff9f43; color:#fff;">🧹 Xóa Cache Mạng</button>
                            <button id="aapro-copy-videos" class="aapro-btn-ui">📋 Copy All</button>
                            <button id="aapro-send-bot-videos" class="aapro-btn-ui aapro-btn-primary">🚀 Gửi qua Bot</button>
                        </div>
                    </div>
                `;
                document.body.appendChild(modal);
                var textArea = modal.querySelector('#aapro-video-links-area');
                textArea.value = uniqueLinks.join('\n');
                
                modal.querySelector('#aapro-close-videos').onclick = function() { modal.remove(); };
                
                modal.querySelector('#aapro-clear-cache-videos').onclick = function() {
                    if (window.performance && typeof window.performance.clearResourceTimings === 'function') {
                        window.performance.clearResourceTimings();
                        window.AAPRO.toast('Đã xóa bộ nhớ đệm Network! Hãy Play video mới và quét lại.', 'success');
                        modal.remove();
                    } else {
                        window.AAPRO.toast('Trình duyệt không hỗ trợ xóa bộ nhớ đệm Network!', 'error');
                    }
                };
                
                modal.querySelector('#aapro-copy-videos').onclick = function() {
                    navigator.clipboard.writeText(textArea.value).then(function() {
                        window.AAPRO.toast('Đã copy ' + uniqueLinks.length + ' link!', 'success');
                        modal.querySelector('#aapro-copy-videos').innerText = '✅ Đã Copy';
                    }).catch(function() { window.AAPRO.toast('Có lỗi, vui lòng copy thủ công!', 'error'); });
                };

                modal.querySelector('#aapro-send-bot-videos').onclick = function() {
                    var sendBtn = modal.querySelector('#aapro-send-bot-videos');
                    if (sendBtn.disabled) return;
                    sendBtn.disabled = true; sendBtn.innerText = '⏳ Đang gửi...';

                    if (!TELEGRAM_BOT_TOKEN || TELEGRAM_BOT_TOKEN.indexOf('ĐIỀN_TOKEN') !== -1) {
                        window.AAPRO.toast('Vui lòng cấu hình Token Bot Telegram!', 'error');
                        sendBtn.disabled = false; sendBtn.innerText = '🚀 Gửi qua Bot';
                        return;
                    }

                    var textMsg = "🎥 <b>Trích xuất Video MP4</b>\n";
                    textMsg += "📑 <b>Trang:</b> <a href='" + window.location.href + "'>" + (document.title || 'Link Web') + "</a>\n\n";
                    uniqueLinks.forEach(function(link, index) { textMsg += "🔗 <b>Video " + (index + 1) + ":</b>\n<code>" + link + "</code>\n\n"; });
                    if (textMsg.length > 4000) textMsg = textMsg.substring(0, 4000) + "...\n\n<i>(Đã cắt bớt vì quá dài)</i>";

                    var payload = { chat_id: TELEGRAM_CHAT_ID, text: textMsg, parse_mode: 'HTML', disable_web_page_preview: true };
                    var url = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendMessage';

                    function handleSendError() { window.AAPRO.toast('❌ Gửi lỗi! Kiểm tra kết nối.', 'error'); sendBtn.disabled = false; sendBtn.innerText = '🚀 Gửi qua Bot'; }

                    if (typeof GM_xmlhttpRequest !== 'undefined') {
                        GM_xmlhttpRequest({
                            method: 'POST', url: url, headers: { 'Content-Type': 'application/json' }, data: JSON.stringify(payload),
                            onload: function(res) {
                                try { if (JSON.parse(res.responseText).ok) { window.AAPRO.toast('✅ Đã gửi ' + uniqueLinks.length + ' link qua Bot!', 'success'); sendBtn.innerText = '✅ Đã Gửi'; window.AAPRO.vibrate([15, 30]); } else handleSendError(); } catch(e) { handleSendError(); }
                            }, onerror: handleSendError
                        });
                    } else {
                        fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
                        .then(function(r) { return r.json(); }).then(function(d) {
                            if (d.ok) { window.AAPRO.toast('✅ Đã gửi ' + uniqueLinks.length + ' link qua Bot!', 'success'); sendBtn.innerText = '✅ Đã Gửi'; } else handleSendError();
                        }).catch(handleSendError);
                    }
                };
            });
        }

        // ====================================
        // Extract Video from HTML Source Logic
        // ====================================
        var extractHtmlBtn = document.getElementById('aapro-extract-from-html');
        if (extractHtmlBtn) {
            extractHtmlBtn.addEventListener('click', function() {
                var modal = document.createElement('div');
                modal.className = 'aapro-modal';
                modal.innerHTML = `
                    <div class="aapro-modal-content" style="width: 90%; max-width: 600px; height: auto; max-height: 80vh; padding: 20px; border-radius: 12px; display: block; box-sizing: border-box;">
                        <h3 style="margin-top: 0; color: #00c6ff; font-size: 18px; margin-bottom: 15px; text-align: center;">📄 Lọc MP4 từ mã nguồn</h3>
                        <textarea id="aapro-html-input-area" placeholder="Dán toàn bộ mã nguồn HTML / Text chứa link vào đây..." style="width: 100%; height: 150px; background: var(--aapro-bg-tertiary); color: var(--aapro-text-primary); border: 1px solid var(--aapro-border-color); border-radius: 8px; padding: 10px; font-family: monospace; font-size: 12px; resize: none; box-sizing: border-box;"></textarea>
                        
                        <div id="aapro-html-results" style="display:none; margin-top:15px;">
                            <h4 style="margin: 0 0 10px 0; color: #1abc9c; font-size: 14px;">✅ Đã tìm thấy: <span id="aapro-html-count">0</span> link</h4>
                            <textarea id="aapro-html-output-area" readonly style="width: 100%; height: 120px; background: var(--aapro-bg-tertiary); color: var(--aapro-text-primary); border: 1px solid var(--aapro-border-color); border-radius: 8px; padding: 10px; font-family: monospace; font-size: 12px; white-space: pre; overflow: auto; resize: none; box-sizing: border-box;"></textarea>
                        </div>
                        
                        <div style="display: flex; gap: 10px; justify-content: flex-end; margin-top: 15px; flex-wrap: wrap;">
                            <button id="aapro-close-html" class="aapro-btn-ui aapro-btn-danger">Đóng</button>
                            <button id="aapro-process-html" class="aapro-btn-ui aapro-btn-primary">🔍 Lọc MP4</button>
                            <button id="aapro-copy-html" class="aapro-btn-ui" style="display:none;">📋 Copy All</button>
                            <button id="aapro-send-html" class="aapro-btn-ui aapro-btn-primary" style="display:none; background:#28a745; border-color:#28a745;">🚀 Gửi qua Bot</button>
                        </div>
                    </div>
                `;
                document.body.appendChild(modal);

                var inputArea = modal.querySelector('#aapro-html-input-area');
                var outputArea = modal.querySelector('#aapro-html-output-area');
                var resultsDiv = modal.querySelector('#aapro-html-results');
                var countSpan = modal.querySelector('#aapro-html-count');
                
                var processBtn = modal.querySelector('#aapro-process-html');
                var copyBtn = modal.querySelector('#aapro-copy-html');
                var sendBtn = modal.querySelector('#aapro-send-html');
                
                var extractedLinks = [];

                modal.querySelector('#aapro-close-html').onclick = function() { modal.remove(); };

                processBtn.onclick = function() {
                    var html = inputArea.value;
                    if (!html.trim()) { window.AAPRO.toast('Vui lòng dán mã nguồn vào trước!', 'warning'); return; }
                    
                    var cleanedHtml = html.replace(/\\\//g, '/'); // Giải mã các dấu escape '\/' trong JSON
                    
                    // Regex mới để bắt cả link tương đối và tuyệt đối trong các thuộc tính
                    var regex = /(?:["'=(])([^"'=()\s<>]+\.mp4(?:\?[^"'=()\s<>]*)?)/gi;
                    var rawMatches = [];
                    var match;
                    while ((match = regex.exec(cleanedHtml)) !== null) {
                        rawMatches.push(match[1]); // Lấy group 1 là đường dẫn link
                    }
                    
                    extractedLinks = Array.from(new Set(rawMatches));
                    
                    if (extractedLinks.length === 0) { window.AAPRO.toast('Không tìm thấy link MP4 nào!', 'error'); return; }
                    
                    countSpan.innerText = extractedLinks.length;
                    outputArea.value = extractedLinks.join('\n');
                    resultsDiv.style.display = 'block';
                    copyBtn.style.display = 'inline-block';
                    sendBtn.style.display = 'inline-block';
                    window.AAPRO.toast('Đã lọc được ' + extractedLinks.length + ' link!', 'success');
                };
                
                copyBtn.onclick = function() {
                    navigator.clipboard.writeText(outputArea.value).then(function() {
                        window.AAPRO.toast('Đã copy ' + extractedLinks.length + ' link!', 'success');
                        copyBtn.innerText = '✅ Đã Copy';
                    }).catch(function() { window.AAPRO.toast('Có lỗi, vui lòng copy thủ công!', 'error'); });
                };

                sendBtn.onclick = function() {
                    if (sendBtn.disabled) return;
                    sendBtn.disabled = true; sendBtn.innerText = '⏳ Đang gửi...';
                    if (!TELEGRAM_BOT_TOKEN || TELEGRAM_BOT_TOKEN.indexOf('ĐIỀN_TOKEN') !== -1) { window.AAPRO.toast('Vui lòng cấu hình Token Bot Telegram!', 'error'); sendBtn.disabled = false; sendBtn.innerText = '🚀 Gửi qua Bot'; return; }
                    var textMsg = "📄 <b>Lọc MP4 từ Mã Nguồn HTML</b>\n📑 <b>Trang:</b> <a href='" + window.location.href + "'>" + (document.title || 'Link Web') + "</a>\n\n";
                    extractedLinks.forEach(function(link, index) { textMsg += "🔗 <b>Video " + (index + 1) + ":</b>\n<code>" + link + "</code>\n\n"; });
                    if (textMsg.length > 4000) textMsg = textMsg.substring(0, 4000) + "...\n\n<i>(Đã cắt bớt vì quá dài)</i>";
                    var payload = { chat_id: TELEGRAM_CHAT_ID, text: textMsg, parse_mode: 'HTML', disable_web_page_preview: true };
                    var url = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendMessage';
                    function handleSendError() { window.AAPRO.toast('❌ Gửi lỗi! Kiểm tra kết nối.', 'error'); sendBtn.disabled = false; sendBtn.innerText = '🚀 Gửi qua Bot'; }
                    if (typeof GM_xmlhttpRequest !== 'undefined') { GM_xmlhttpRequest({ method: 'POST', url: url, headers: { 'Content-Type': 'application/json' }, data: JSON.stringify(payload), onload: function(res) { try { if (JSON.parse(res.responseText).ok) { window.AAPRO.toast('✅ Đã gửi!', 'success'); sendBtn.innerText = '✅ Đã Gửi'; window.AAPRO.vibrate([15, 30]); } else handleSendError(); } catch(e) { handleSendError(); } }, onerror: handleSendError }); } else { fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) }).then(function(r) { return r.json(); }).then(function(d) { if (d.ok) { window.AAPRO.toast('✅ Đã gửi!', 'success'); sendBtn.innerText = '✅ Đã Gửi'; } else handleSendError(); }).catch(handleSendError); }
                };
            });
        }

        function refresh() {
            var s =
                window.AAPRO.state;
            var timeEl = document.getElementById('aapro-info-time');
            if (timeEl) {
                var now = new Date();
                timeEl.innerText = now.toLocaleTimeString('vi-VN') + ' - ' + now.toLocaleDateString('vi-VN');
            }
            enable.checked =
                s.enabled;
            document.getElementById(
                'aapro-status'
            ).innerHTML = `
<div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
    <span>Status:</span>
    <span style="font-weight: bold; color: ${s.enabled ? '#2ecc71' : '#e74c3c'}">${s.enabled ? '🟢 ACTIVE' : '🔴 OFF'}</span>
</div>
<div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
    <span>Total Blocked:</span>
    <span style="font-weight: bold; color: #00a8ff;">${s.totalBlocked}</span>
</div>
<div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
    <span>Trackers (Ads & Spies):</span>
    <span style="font-weight: bold; color: #1abc9c;">${s.tracker}</span>
</div>
<div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
    <span>Crypto Miners Blocked:</span>
    <span style="font-weight: bold; color: #e74c3c;">${s.miner}</span>
</div>
<div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
    <span>Popups:</span>
    <span style="font-weight: bold; color: #f368e0;">${s.popup}</span>
</div>
<div style="display: flex; justify-content: space-between;">
    <span>Iframes/Scripts:</span>
    <span style="font-weight: bold; color: #ff9f43;">${s.iframe}</span>
</div>
`;
            var domains =
                Object.keys(s.domains).map(function(key) {
                    return [key, s.domains[key]];
                })
                .sort(
                    function(a,b) { return b[1]-a[1]; }
                )
                .slice(0,10);
            document.getElementById(
                'aapro-domains'
            ).innerHTML =
            domains.length
            ?
            domains.map(
                function(d) { return `
<div class="aapro-domain-item" data-domain="${d[0]}" style="display: flex; justify-content: space-between; padding: 6px 8px; border-bottom: 1px solid rgba(255,255,255,0.05); cursor: pointer; border-radius: 4px; transition: background 0.2s;">
<span>${d[0]}</span>
<span style="color: #ff4757; font-weight: bold;">${d[1]}</span>
</div>
`; }
            ).join('')
            :
            '<div style="text-align: center; color: #888;">No data</div>';
            
            var domainItems = document.querySelectorAll('.aapro-domain-item');
            domainItems.forEach(function(item) {
                item.addEventListener('click', function() {
                    var domain = this.getAttribute('data-domain');
                    var details = s.logs.filter(function(l) { return l.host === domain; });
                    if (details.length === 0) return;
                    
                    var modal = document.createElement('div');
                    modal.className = 'aapro-modal';
                    modal.style.zIndex = '2147483648';
                    modal.innerHTML = `
                        <div class="aapro-modal-content" style="width: 90%; max-width: 400px; height: auto; max-height: 80vh; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
                            <h3 style="margin-top: 0; color: #ff4757; font-size: 16px; margin-bottom: 15px; text-align: center;">Chi tiết chặn: ${domain}</h3>
                            <div style="flex: 1; overflow-y: auto; background: var(--aapro-bg-secondary); border-radius: 8px; padding: 10px; font-size: 12px;">
                                ${details.map(function(l) {
                                    return '<div style="margin-bottom: 8px; padding-bottom: 8px; border-bottom: 1px solid var(--aapro-border-color);">' +
                                           '<div style="display:flex; justify-content:space-between; color: #00c6ff; font-weight: bold;"><span>' + l.type + '</span><span style="color:var(--aapro-text-secondary); font-weight:normal;">' + l.time + '</span></div>' +
                                           '<div style="color: var(--aapro-text-secondary); margin-top: 4px; word-break: break-all;">' + l.host + '</div>' +
                                           '</div>';
                                }).join('')}
                            </div>
                            <button id="aapro-close-domain-details" class="aapro-btn-ui aapro-btn-danger" style="margin-top: 15px;">Đóng</button>
                        </div>
                    `;
                    document.body.appendChild(modal);
                    modal.querySelector('#aapro-close-domain-details').onclick = function() { modal.remove(); };
                });
            });

            // Refresh logs tab
            var logsHtml = s.logs.length ? s.logs.map(function(log) {
                var color = log.type.includes('Popup') ? '#f368e0' : (log.type.includes('Overlay') ? '#e74c3c' : '#ff9f43');
                return '<div style="padding: 8px 0; border-bottom: 1px solid var(--aapro-border-color);">' +
                    '<div style="display:flex; justify-content:space-between; margin-bottom:4px;">' +
                        '<span style="color:' + color + '; font-weight:bold;">' + log.type + '</span>' +
                        '<span style="color:var(--aapro-text-secondary); font-size:10px;">' + log.time + '</span>' +
                    '</div>' +
                    '<div style="color:var(--aapro-text-secondary); word-break: break-all;">' + log.host + '</div>' +
                '</div>';
            }).join('') : '<div style="text-align:center; color:var(--aapro-text-secondary); padding: 10px;">Chưa có nhật ký</div>';
            var logsContainer = document.getElementById('aapro-logs-list');
            if(logsContainer) logsContainer.innerHTML = logsHtml;
        }
        enable.onchange =
            function() {
                window.AAPRO.state
                .enabled =
                    enable.checked;
                window.AAPRO.save();
                applyCookieBlocker();
                refresh();
            };

        // Tính toán tâm Transform từ Panel đổ về Button Chiếc Khiên
        function updatePanelTransformOrigin() {
            var btn = document.getElementById('aapro-btn');
            if (!btn || panel.style.display === 'none') return;
            var btnRect = btn.getBoundingClientRect();
            var panelRect = panel.getBoundingClientRect();
            var originX = (btnRect.left + (btnRect.width / 2)) - panelRect.left;
            var originY = (btnRect.top + (btnRect.height / 2)) - panelRect.top;
            panel.style.transformOrigin = originX + 'px ' + originY + 'px';
        }

        hideBtn.onclick =
            function() {
                window.AAPRO.playClickSound();
                updatePanelTransformOrigin();
                panelVisible = false;
                panel.classList.remove('aapro-show');
                setTimeout(function() { if (!panelVisible) panel.style.display = 'none'; }, 400);
            };
        clearBtn.onclick =
            function() {
                window.AAPRO.clearLogs();
                refresh();
            };
        resetBtn.onclick =
            function() {
                window.AAPRO.resetStats();
                refresh();
            };
        document.addEventListener(
            'AAPRO_PANEL',
            function() {
                window.AAPRO.playClickSound();
                panelVisible =
                    !panelVisible;
                if (panelVisible) {
                    panel.style.display = 'flex';
                    updatePanelTransformOrigin();
                    void panel.offsetWidth; // Force Reflow
                    panel.classList.add('aapro-show');
                } else {
                    updatePanelTransformOrigin();
                    panel.classList.remove('aapro-show');
                    setTimeout(function() { if (!panelVisible) panel.style.display = 'none'; }, 400);
                }
                refresh();
            }
        );
        setInterval(
            refresh,
            1000
        );
    }
    var wait =
        setInterval(
            function() {
                if (
                    document.body &&
                    window.AAPRO
                ) {
                    createPanel();
                    clearInterval(
                        wait
                    );
                }
            },
            300
        );
})();
