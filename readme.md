#  Real-time Collaborative Text Editor with Django & WebSockets

A **real-time collaborative text editor** built using **Django, WebSockets, and Redis**. This application allows multiple users to edit the same document **simultaneously**, with **live updates, active user tracking, and AI-powered summarization**.

---

##  Features
- **Real-time text editing** with WebSockets
- **Multiple users can collaborate simultaneously**
- **Live user tracking with custom nicknames**
- **AI-powered summarization using Hugging Face**
- **WebSockets integration via Django Channels**
- **Redis-backed messaging for fast updates**
- **Minimal UI for smooth collaboration**
- **Documents are saved to PostgreSQL (AWS RDS)**
- **User nicknames are used for tracking who is editing**

---

## Tech Stack
| Technology | Usage |
|------------|------------------------|
| **Django** | Web framework |
| **Django Channels** | WebSockets support |
| **Daphne** | ASGI server for real-time updates |
| **Django Channels** | Backend messaging for WebSockets |
| **PostgreSQL (AWS RDS)** | Database for document storage |
| **Transformers (Hugging Face)** | AI-powered text summarization |
| **T5-small Model** | Summarizes selected text |
| **HTML, CSS, JavaScript** | Frontend for the editor |

---

---

## How Real-time Tracking Works
- When a user joins the document, they are **asked for a nickname**.
- The **nickname is stored in memory** and linked to their WebSocket session.
- As users edit the document, **changes are synced instantly** via WebSockets.
- The active users list updates in **real-time**, showing **who is currently editing**.

---

## Database Integration with AWS RDS (PostgreSQL)
- Documents are **stored in a PostgreSQL database** hosted on **AWS RDS**.
- When a user **edits a document**, the content is **auto-saved periodically**.
- When a document is reopened, **the latest saved version is loaded**.

---

## Summarization Feature (Using Transformers & T5-small)
- Users can **select text and generate a summary** instantly.
- The summarization is powered by **Hugging Face's `t5-small` model**.
- The system **caches summaries for faster performance**.

---

## Quick Start Commands

### **Install Required Dependencies**
Ensure you have Python installed, then install all dependencies using:
```bash
pip install -r requirements.txt


### **Run the Django Development Server**
For basic local testing, you can start Django using:
'''bash
python manage.py runserver


### **Run the ASGI Server with Daphne**
For WebSockets support, use Daphne instead of runserver:
'''bash
daphne -b 0.0.0.0 -p 8000 core.asgi:application
-Daphne allows real-time updates and multiple user collaboration.