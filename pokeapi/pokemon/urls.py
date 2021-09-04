""" Pokémon URLs. """
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
	EvolutionChainViewSet,
	PokemonViewSet,
	StatsViewSet,
	SearchPokemonView
)


router = DefaultRouter()
router.register(r'evolution-chain', EvolutionChainViewSet, basename='chain')
router.register(r'pokemon', PokemonViewSet, basename='chain')
router.register(r'stats', StatsViewSet, basename='chain')

urlpatterns = [
	path('', include(router.urls)),
	path('search-pokemon/', SearchPokemonView)
]
