from django.urls import path
from .views import document_list, document_edit, create_document, save_document, summarize_document


urlpatterns = [
    path("", document_list, name="home"),
    path("documents/new/", create_document, name="create_document"),
    path("documents/<int:doc_id>/edit/", document_edit, name="document_edit"),
    path("documents/<int:doc_id>/save/", save_document, name="save_document"),
    path("summarize/<int:doc_id>/", summarize_document, name="summarize_document"),
]