# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import login as django_login
from django.views.generic import TemplateView
from django.conf import settings
from pycrest.errors import APIException

import pycrest
from pycrestHelpers import getAllItems


def login(request):
    return django_login(request, template_name='login.html')


def logout(request):
    django_logout(request)
    return redirect('/')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_public_crest_context(self):
        """fetch some example stuff from public CREST"""

        # use anonymous PyCrest as documented at http://pycrest.readthedocs.org/
        public_crest = pycrest.EVE()
        public_crest()

        tranquility_user_count = public_crest().userCount_str

        # fetch incursions and make them usable inside a Django template
        incursions = []
        for dict_but_isnt in public_crest.incursions().items:
            incursion = {}
            ## changed 'iteritems -> items for py3 support'
            for key, value in dict_but_isnt._dict.items():
                incursion[key] = value._dict if hasattr(value, '_dict') else value
            incursions.append(incursion)

        # for demo purposes only: shortcut to market URL
        endpoint = public_crest._public_endpoint
        type_id = 34          # Tritanium, the "Hello World" of EVE Items...
        region_id = 10000002  # The Forge
        type_url = "{0}inventory/types/{1}/".format(endpoint, type_id)
        # endpoint changed
        # /types/ --> /inventory/types/
        # https://crest-tq.eveonline.com/inventory/types/34/
        buy_orders_url = "{0}market/{1}/orders/buy/?type={2}".format(endpoint, region_id, type_url)
        sell_orders_url = "{0}market/{1}/orders/sell/?type={2}".format(endpoint, region_id, type_url)

        sell_orders = public_crest.get(sell_orders_url)['items']
        buy_orders = public_crest.get(buy_orders_url)['items']

        # sort by price up/down
        sell_orders = sorted(sell_orders, key=lambda k: k['price'])
        buy_orders = sorted(buy_orders, key=lambda k: k['price'], reverse=True)

        # truncate to Top <limit> orders
        limit = 5
        if len(sell_orders) > limit:
            sell_orders = sell_orders[0:limit]

        if len(buy_orders) > limit:
            buy_orders = buy_orders[0:limit]

        return {
            'user_count': tranquility_user_count,
            'incursions': incursions,
            'sell_orders': sell_orders,
            'buy_orders': buy_orders,
        }


    def get_authed_crest_context(self):
        """fetch some market data from authenticated CREST"""

        # here we use pycrest, but we should really TODO -- fix backend to call CREST directly
        # since we already completed the authentication process via python-social-auth
        try:
            authed_crest = pycrest.eve.AuthedConnection(
                res=self.request.user._get_crest_tokens(), # calls backend for authed info
                endpoint=pycrest.EVE()._authed_endpoint,
                oauth_endpoint=pycrest.EVE()._oauth_endpoint,
                client_id=settings.SOCIAL_AUTH_EVEONLINE_KEY,
                api_key=settings.SOCIAL_AUTH_EVEONLINE_SECRET
            )
            authed_crest()
        except: # stale refresh token fix needed, authed_crest().refresh() 
                # doesn't seem to actually fix anything when APIException caught here
            logout(self.request)

        authed_char = authed_crest().decode().character()
        fittings = getAllItems(authed_char.fittings())
        contacts = getAllItems(authed_char.contacts())
        opportunities = getAllItems(authed_char.opportunities())
        lp = getAllItems(authed_char.loyaltyPoints())
        return {
            'loyaltyPoints': lp,
            'fittings': fittings,
            'contacts': contacts,
            'opportunities': opportunities,
        }


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['public_crest'] = self.get_public_crest_context()
        context['authed_crest'] = self.get_authed_crest_context()
        return context
