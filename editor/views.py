from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Document

from transformers import pipeline

def document_list(request):
    documents = Document.objects.all()
    return render(request, "editor/document_list.html", { "documents" : documents})

def document_edit(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return render(request, "editor/document_edit.html", {"document" : document})

@csrf_exempt
def save_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    if request.method == "POST":
        data = json.loads(request.body)
        document.content = data["content"]
        document.save()
        return JsonResponse({"message" : "doc saved sucessfully!!"})
    
def create_document(request):
    new_doc = Document.objects.create(title="Untitled Document", content="")
    return redirect("document_edit", doc_id=new_doc.id)

summarizer = pipeline("summarization", model="t5-small")

@csrf_exempt
def summarize_document(request, doc_id):
    document = Document.objects.get(id=doc_id)
    if request.method == "POST":
        data = json.loads(request.body)
        selected_text = data.get("text", "")

        if not selected_text:
            return JsonResponse({"error": "No text selected"}, status=400)

        summary = summarizer(selected_text, max_length=100, min_length=30, do_sample=False)
        summarized_text = summary[0]["summary_text"]

        return JsonResponse({"summary": summarized_text})
    
    return JsonResponse({"error": "Invalid request"}, status=400)
