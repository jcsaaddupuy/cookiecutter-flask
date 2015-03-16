# coding: utf-8
from __future__ import unicode_literals

from flask import make_response
from flask import Blueprint

# webargs
from webargs import Arg
from webargs.flaskparser import use_args


blueprint = Blueprint('default', __name__)


@blueprint.route('/', methods=['GET'])
@use_args({'name': Arg(str, required=False, use=lambda x: x.title())})
def register(args):
    """ Register a new client """
    name = args['name'] or 'world'
    return make_response('Hello %s' % name, 200)
