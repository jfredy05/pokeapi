""" Pokémon serializers. """
from rest_framework import serializers
from .models import EvolutionChain, Pokemon, Stats


class EvolutionChainSerializer(serializers.ModelSerializer):
	""" Evolution Chain Serializer. """

	class Meta:
		model = EvolutionChain
		fields = (
			'id', 'id_chain'
		)


class PokemonSerializer(serializers.ModelSerializer):
	""" Evolution Chain Serializer. """

	class Meta:
		model = Pokemon
		fields = (
			'id', 'chain', 'id_pokemon', 'name', 'image',
			'height', 'weight', 'order'
		)


class StatsSerializer(serializers.ModelSerializer):
	""" Evolution Chain Serializer. """

	class Meta:
		model = Stats
		fields = (
			'id', 'pokemon', 'name', 'base', 'effort'
		)
