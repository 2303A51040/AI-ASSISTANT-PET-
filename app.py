from flask import Flask, jsonify, request, render_template_string
from memory_meeting_ai.store import init_db, add_note, recent_notes
from shared.events import publish_event

app = Flask(__name__)
init_db()

PAGE = '''
<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NEXUS Dashboard</title>
<style>body{font-family:Arial;margin:32px auto;max-width:760px;padding:0 16px;background:#101827;color:#eef}
.card{background:#1c2940;padding:18px;border-radius:12px;margin:14px 0}input,textarea,button{padding:10px;margin:5px 0;width:100%;box-sizing:border-box;border-radius:6px}
button{background:#2585d8;color:white;border:0;cursor:pointer}small{color:#b8c7dd}</style></head>
<body><h1>🤖 NEXUS Dashboard</h1><small>Local development dashboard</small>
<div class="card"><h2>Robot status</h2><p id="status">Connected to local dashboard</p>
<button onclick="sendEvent('dashboard_ping')">Send test event</button></div>
<div class="card"><h2>Save a note</h2><input id="title" placeholder="Title"><textarea id="body" placeholder="Note"></textarea>
<button onclick="saveNote()">Save note</button><p id="result"></p></div>
<div class="card"><h2>Recent notes</h2><div id="notes">Loading...</div></div>
<script>
async function load(){let r=await fetch('/api/notes');let d=await r.json();document.getElementById('notes').innerHTML=d.notes.map(n=>'<p><b>'+escapeHtml(n[0])+'</b><br>'+escapeHtml(n[1])+'</p>').join('')||'No notes yet';}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
async function saveNote(){let r=await fetch('/api/notes',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({title:title.value,body:body.value})});let d=await r.json();result.textContent=d.message;load();}
async function sendEvent(type){await fetch('/api/event',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({type})});status.textContent='Test event sent';}
load();
</script></body></html>'''

@app.get("/")
def home():
    return render_template_string(PAGE)

@app.get("/api/notes")
def get_notes():
    return jsonify(notes=recent_notes())

@app.post("/api/notes")
def post_note():
    data = request.get_json(silent=True) or {}
    title, body = str(data.get("title","")).strip(), str(data.get("body","")).strip()
    if not title or not body:
        return jsonify(message="Please enter both title and note."), 400
    add_note(title, body)
    return jsonify(message="Note saved successfully.")

@app.post("/api/event")
def post_event():
    data = request.get_json(silent=True) or {}
    publish_event(str(data.get("type", "dashboard_event")), {"origin": "dashboard"})
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
