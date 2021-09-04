""" Pokémon Views. """
from django.shortcuts import render

from rest_framework import viewsets

from .models import EvolutionChain, Pokemon, Stats
from .serializers import (
	EvolutionChainSerializer,
	PokemonSerializer,
	StatsSerializer
)


class EvolutionChainViewSet(viewsets.ModelViewSet):
	""" Circle view set. """
	queryset = EvolutionChain.objects.all()
	serializer_class = EvolutionChainSerializer


class PokemonViewSet(viewsets.ModelViewSet):
	""" Circle view set. """
	queryset = Pokemon.objects.all()
	serializer_class = PokemonSerializer


class StatsViewSet(viewsets.ModelViewSet):
	""" Circle view set. """
	queryset = Stats.objects.all()
	serializer_class = StatsSerializer


def SearchPokemonView(request):
	name_pakemon = request.GET.get('name')
	ctx = {'message': 'Search Pokémon'}
	if name_pakemon:
		poke = Pokemon.objects.filter(
			name=name_pakemon
		).prefetch_related('stats_set').first()
		if poke:
			order = poke.order
			# Prevolution / Evolutions
			pokes_chain = Pokemon.objects.filter(
				chain=poke.chain
			).prefetch_related('stats_set').exclude(pk=poke.pk)

			fields = ['name', 'image', 'height', 'weight']
			prevolutions = list(pokes_chain.filter(
				order__lte=order
			).values(*fields))
			evolutions = list(pokes_chain.filter(
				order__gte=order
			).values(*fields))

			ctx = {
				'pokemon': {
					'chain': poke.chain,
					'name': poke.name,
					'image': poke.image,
					'height': poke.height,
					'weight': poke.weight,
					'stats': list(poke.stats_set.values('name', 'base'))
				},
				'prevolutions': prevolutions,
				'evolutions': evolutions
			}
		else:
			ctx['message'] = 'Pokémon Not found'

	return render(request, 'search.html', ctx)
