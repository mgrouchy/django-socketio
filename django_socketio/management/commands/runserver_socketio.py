import re
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management.base import BaseCommand, CommandError
from django.core.management.commands.runserver import naiveip_re

from gevent import monkey

from socketio import SocketIOServer


class Command(BaseCommand):

    def get_handler(self):
        return WSGIHandler()

    def handle(self, addrport='', *args, **options):

        if not addrport:
            self.addr = '127.0.0.1'
            self.port = settings.DEFAULT_SOCKETIO_PORT or 9000
        else:
            m = re.match(naiveip_re, addrport)
            if m is None:
                raise CommandError('"%s" is not a valid port number '
                                   'or address:port pair.' % addrport)

            self.addr, _, _, _, self.port = m.groups()

            if not self.port.isdigit():
                raise CommandError("%r is not a valid port number." % self.port)

        self.run(*args, **options)


    def run(self, *args, **options):
        # use gevent to patch the standard lib to get async support
        monkey.patch_all()

        server_address = (self.addr, self.port)

        print "Socket.IO server started on %s:%s" % server_address
        SocketIOServer(server_address, self.get_handler(),
                        resource="socket.io").serve_forever()


