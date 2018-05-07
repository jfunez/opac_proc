# coding: utf-8
from opac_proc.core.process import ProcessLoadBase
from opac_proc.web import config
from opac_proc.logger_setup import getMongoLogger

if config.DEBUG:
    logger = getMongoLogger(__name__, "DEBUG", "load")
else:
    logger = getMongoLogger(__name__, "INFO", "load")


class ProcessLoadCollection(ProcessLoadBase):
    model_name = 'collection'
    task_for_selected = 'opac_proc.loaders.jobs.task_load_selected_collections'
    task_for_all = 'opac_proc.loaders.jobs.task_load_all_collections'


class ProcessLoadJournal(ProcessLoadBase):
    model_name = 'journal'
    task_for_selected = 'opac_proc.loaders.jobs.task_load_selected_journals'
    task_for_all = 'opac_proc.loaders.jobs.task_load_all_journals'


class ProcessLoadIssue(ProcessLoadBase):
    model_name = 'issue'
    task_for_selected = 'opac_proc.loaders.jobs.task_load_selected_issues'
    task_for_all = 'opac_proc.loaders.jobs.task_load_all_issues'


class ProcessLoadArticle(ProcessLoadBase):
    model_name = 'article'
    task_for_selected = 'opac_proc.loaders.jobs.task_load_selected_articles'
    task_for_all = 'opac_proc.loaders.jobs.task_load_all_articles'


class ProcessLoadPressRelease(ProcessLoadBase):
    model_name = 'press_release'
    task_for_selected = 'opac_proc.loaders.jobs.task_load_selected_press_releases'
    task_for_all = 'opac_proc.loaders.jobs.task_load_all_press_releases'


class ProcessLoadNews(ProcessLoadBase):
    model_name = 'news'
    task_for_selected = 'opac_proc.loaders.jobs.task_load_selected_news'
    task_for_all = 'opac_proc.loaders.jobs.task_load_all_news'
