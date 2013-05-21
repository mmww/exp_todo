# encoding: utf-8

import logging
from django.shortcuts import render_to_response, get_object_or_404 
from django.template import RequestContext 
from django.http import HttpResponse  
logger = logging.getLogger(__name__)


def handle_rest_call(request, *args, **kwargs):
    logger.debug('TODO: Implement me: args %s, kwargs %s', args, kwargs)
    return render_to_response('todo_client/index.html', {},  
            context_instance=RequestContext(request))
    #raise NotImplementedError('TODO: Implement me!')
