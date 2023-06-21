from base.utils import importFile
from celery import task


@task
def importFileTask(excel_upload):
    importFile(excel_upload)